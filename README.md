<div style="background-color: white; padding: 20px;">

<h2 align="center">Gainsight AI</h2>
<h4 align="center">Voice-of-Customer Intelligence Engine</h4>

<div align="center">

[![Python version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Flask version](https://img.shields.io/badge/flask-3.1.2-red.svg)](https://flask.palletsprojects.com/)
[![Google Gemini](https://img.shields.io/badge/gemini-2.5--flash-green.svg)](https://ai.google.dev/)

<h4>Transform unstructured customer feedback into actionable business intelligence using AI-powered analysis.</h4>

<p align="center">
  <a href="https://devcavi19.pythonanywhere.com">
    <img src="https://img.shields.io/badge/Project%20Link-Live%20Demo-blueviolet?style=for-the-badge" alt="Project Link"/>
  </a>
</p>

</div>

-----------------------------------------

### Project Overview

* Gainsight AI is a web application that helps businesses process and analyze customer feedback at scale. Modern businesses collect massive amounts of feedback from support tickets, social media, reviews, and surveys, but struggle to extract meaningful insights manually.

* This tool leverages **Google Gemini AI** to automatically categorize feedback into critical issues requiring immediate attention, feature requests and product gaps, overall sentiment analysis, and quick wins for easy improvements.

* Built with the assistance of **Claude Opus 4.5**, an advanced AI coding assistant that helped accelerate development and ensure code quality.

------------------------------------------

### Features

#### AI-Powered Analysis

* **P0 Issue Detection** - Identifies critical bugs and broken functionality needing immediate attention
* **Product Gap Analysis** - Discovers missing features customers are requesting
* **Sentiment Pulse** - Visual sentiment score from -100 (negative) to +100 (positive) with emoji indicators
* **Quick Wins** - Highlights small improvements with high customer impact
* **Key Themes** - Extracts recurring topics and patterns from feedback

<br>

------------------------------------------

#### Input & Upload Options

* **Multi-Format Upload** - Supports JSON, CSV, and TXT file uploads
* **Clipboard Paste** - One-click paste functionality for quick input
* **Visual Dashboard** - Color-coded cards for easy interpretation of results

<br>

------------------------------------------

### Technical Stack

#### Backend
* **Python 3.10** - Programming language
* **Flask** - Web framework
* **Google Generative AI** - Gemini API for AI analysis
* **python-dotenv** - Environment variable management

#### Frontend
* **Jinja2** - HTML templating
* **Tailwind CSS** - Utility-first CSS framework (via CDN)
* **Vanilla JavaScript** - File parsing, clipboard API, notifications

#### AI Model
* **Google Gemini** (`gemini-2.5-flash` by default)

#### Development Tools
* **Claude Opus 4.5** - AI coding assistant for development support

------------------------------------------

### Prerequisites

1. [Python 3.10+](https://www.python.org/downloads/)
2. [Google Gemini API Key](https://makersuite.google.com/app/apikey)
3. Required Python packages (see requirements.txt)

------------------------------------------

### Installation

* Step I: Clone the Repository
```sh
      $ git clone <repository-url>
      $ cd gainsight-ai
```

* Step II: Create and activate virtual environment
```sh
      $ python -m venv env
      $ source env/bin/activate  # On Windows: env\Scripts\activate
```

* Step III: Install the required packages
```sh
      $ pip install -r requirements.txt
```

* Step IV: Set up environment variables

Create a `.env` file in the project root:
```sh
      GOOGLE_API_KEY=your-gemini-api-key-here
      GEMINI_MODEL=gemini-2.5-flash
```

* Step V: Run the application
```sh
      $ python app.py
```

* Step VI: Open in browser
```
      http://localhost:5000
```

------------------------------------------

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GOOGLE_API_KEY` | Your Google Gemini API key | ✅ Yes | - |
| `GEMINI_MODEL` | Gemini model to use | No | `gemini-2.5-flash` |

------------------------------------------

### File Structure

```
gainsight-ai/
├── app.py                 # Main Flask application with routes and AI integration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── project.md             # Project specification
├── mock-feedback.json     # Sample feedback data for testing
├── .env                   # Environment variables (create this)
├── env/                   # Python virtual environment
└── templates/
    ├── base.html          # Base template with navbar and footer
    ├── index.html         # Feedback input portal
    └── results.html       # Analysis results dashboard
```

------------------------------------------

### Usage

1. **Input Feedback** - Paste customer feedback directly, use the clipboard button, or upload a file
2. **Analyze** - Click "Analyze Feedback" to process with AI
3. **Review Results** - View categorized insights on the results dashboard
4. **Take Action** - Address P0 issues first, then product gaps, and implement quick wins

#### Supported File Formats

* **JSON** - Array of objects with `feedback`, `comment`, `review`, or `text` fields
* **CSV** - Files with columns named `feedback`, `comment`, `review`, etc.
* **TXT** - Plain text with one feedback per line

------------------------------------------

### Deliverables

1. **Web Portal** - Clean, responsive feedback input interface
2. **AI Integration** - Google Gemini-powered feedback analysis
3. **Visual Results Dashboard** - Color-coded insight cards with:
   - Sentiment gauge (-100 to +100)
   - P0 Issues (red)
   - Product Gaps (yellow)
   - Quick Wins (green)
   - Key Themes (tags)
4. **File Upload Support** - JSON, CSV, TXT file parsing
5. **Error Handling** - Graceful error messages and fallbacks

------------------------------------------

### Acknowledgments

* [Google Gemini AI](https://ai.google.dev/) - AI capabilities
* [Tailwind CSS](https://tailwindcss.com/) - Styling framework
* [Flask](https://flask.palletsprojects.com/) - Web framework

------------------------------------------

</div>
