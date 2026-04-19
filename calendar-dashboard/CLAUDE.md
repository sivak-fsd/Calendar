# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python src/app.py

# Run tests
pytest tests/

# Run a single test
pytest tests/test_app.py::test_get_calendar
```

Environment: copy `.env.example` to `.env` before running.

## Architecture

Flask backend + vanilla JS frontend, single-page app with no frontend framework.

**Backend (`src/app.py`):**
- Two routes: `GET /` renders the HTML template; `GET /api/calendar/<year>/<month>` returns JSON
- Calendar data uses Python's built-in `calendar` module — weeks are 2D arrays of ints (0 = empty cell, 1–31 = day number)

**Frontend (`templates/index.html`):**
- All JavaScript is inline in the template
- On load and on prev/next navigation, JS fetches `/api/calendar/{year}/{month}` and rebuilds the calendar table in the DOM
- Today's date is highlighted client-side by comparing against the `today` field in the API response

**Static assets:** `static/css/style.css` — no JS files in `static/js/` (all JS lives in the template).
