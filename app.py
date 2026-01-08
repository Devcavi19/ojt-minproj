import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# Configure Gemini if API key is available (allows app to load for WSGI)
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))


def analyze_feedback_with_gemini(feedback_text: str) -> dict:
    """
    Send feedback to Gemini API and get categorized analysis.
    Returns P0 Issues, Product Gaps, and Sentiment Pulse.
    """
    prompt = f"""You are a Voice-of-Customer (VoC) Intelligence Engine. Analyze the following customer feedback and categorize it into actionable insights.

FEEDBACK TO ANALYZE:
{feedback_text}

Respond ONLY with a valid JSON object in this exact format (no markdown, no explanation):
{{
    "p0_issues": [
        {{
            "title": "Brief title of the critical issue",
            "description": "Detailed description",
            "urgency": "critical"
        }}
    ],
    "product_gaps": [
        {{
            "title": "Missing feature or improvement",
            "description": "What customers are asking for",
            "frequency": "how often mentioned (high/medium/low)"
        }}
    ],
    "sentiment": {{
        "score": 0,
        "label": "positive/neutral/negative",
        "summary": "Brief summary of overall customer sentiment"
    }},
    "quick_wins": [
        {{
            "title": "Easy improvement that could make customers happier",
            "impact": "high/medium/low"
        }}
    ],
    "key_themes": ["theme1", "theme2", "theme3"]
}}

Rules:
- Score sentiment from -100 (very negative) to +100 (very positive)
- P0 Issues are critical bugs or broken functionality that need immediate attention
- Product Gaps are features customers want but don't exist
- Quick Wins are small improvements with high impact
- Key Themes are recurring topics in the feedback
- If no items exist for a category, return an empty array []
"""

    try:
        if not GOOGLE_API_KEY:
            return {
                "success": False,
                "error": "GOOGLE_API_KEY not configured. Please set the environment variable."
            }
        
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        
        # Extract JSON from response
        response_text = response.text.strip()
        
        # Remove markdown code blocks if present
        if response_text.startswith("```"):
            lines = response_text.split("\n")
            response_text = "\n".join(lines[1:-1])
        
        result = json.loads(response_text)
        return {"success": True, "data": result}
    
    except json.JSONDecodeError as e:
        return {
            "success": False,
            "error": f"Failed to parse AI response: {str(e)}",
            "raw_response": response_text if 'response_text' in locals() else None
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"API Error: {str(e)}"
        }


@app.route("/")
def index():
    """Render the feedback input portal."""
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """Process feedback and return categorized results."""
    feedback_text = request.form.get("feedback", "").strip()
    
    if not feedback_text:
        flash("Please enter some feedback to analyze.", "error")
        return redirect(url_for("index"))
    
    # Analyze with Gemini
    result = analyze_feedback_with_gemini(feedback_text)
    
    if result["success"]:
        return render_template(
            "results.html",
            data=result["data"],
            original_feedback=feedback_text
        )
    else:
        flash(result["error"], "error")
        return render_template(
            "results.html",
            error=result["error"],
            original_feedback=feedback_text
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
