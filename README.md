# 📚 Engineering Book Recommender

An AI-powered academic assistant for engineering students in India. Select your engineering branch, semester, and subject to get curated, high-reputation textbook recommendations powered by Google Gemini AI, complete with concise rationales, direct purchase links on Amazon India, and links to free digital versions.

---

## ✨ Features

- **🤖 AI-Powered Curation**: Integrates Google Gemini models (`gemini-3.5-flash-lite`, `gemini-3.5-flash`, `gemini-flash-latest`) with automatic fallback for high reliability.
- **🏛️ Academic Alignment**: Tailored specifically for Indian university engineering curricula (Computer Science, Mechanical, Electrical, Civil, Chemical, etc.).
- **⭐ Reputation-Ranked**: Ranks recommendations with classic, community-favored textbooks first (based on academic consensus and student forums).
- **🛒 Direct Access Links**: Provides direct links to buy on Amazon India alongside free educational versions where available.
- **⚡ Clean & Responsive UI**: Fast and intuitive web interface built with Flask, HTML5, CSS3, and vanilla JavaScript.

---

## 📁 Project Structure

```text
engineering_books/
├── app.py              # Flask server and Gemini API recommendation engine
├── requirements.txt    # Python package dependencies
├── .gitignore          # Git ignore rules for virtual environments & caches
├── templates/
│   └── index.html      # Main frontend HTML template
├── static/
│   ├── style.css       # Styling & responsive design
│   └── script.js       # Asynchronous API requests & dynamic DOM rendering
└── README.md           # Project documentation
```

---

## 📋 Prerequisites

- **Python 3.9+** installed on your system ([Download Python](https://www.python.org/downloads/))
- **Google Gemini API Key** ([Get a free key from Google AI Studio](https://aistudio.google.com/))

---

## 🚀 Getting Started & How to Run

Follow these steps to set up and run the application locally:

### 1. Clone or Download the Repository

```bash
git clone https://github.com/your-username/engineering-books-recommender.git
cd engineering-books-recommender
```

### 2. Create and Activate a Virtual Environment

- **Windows (PowerShell / Command Prompt):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\activate
  ```

- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your Gemini API Key

Open [`app.py`](app.py) and update the `API_KEY` with your Google Gemini API key:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

*(Alternatively, you can set it via an environment variable `GEMINI_API_KEY`)*.

### 5. Start the Server

```bash
python app.py
```

### 6. Open in Browser

Once started, navigate to:
```
http://127.0.0.1:5000
```

---

## 📡 API Reference

### `POST /get_books`

Fetches textbook recommendations for a given branch, semester, and subject.

#### Request Body (JSON)

```json
{
  "branch": "Computer Science",
  "semester": "3",
  "subject": "Data Structures"
}
```

#### Response Example (JSON)

```json
[
  {
    "title": "Introduction to Algorithms",
    "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
    "description": "Widely regarded as the bible of algorithms, covering data structures and design techniques in exhaustive detail.",
    "buy_link": "https://www.amazon.in/...",
    "free_link": "https://..."
  },
  {
    "title": "Data Structures and Algorithms Made Easy",
    "author": "Narasimha Karumanchi",
    "description": "A favorite among engineering students for exam preparation and campus interview problem sets.",
    "buy_link": "https://www.amazon.in/...",
    "free_link": "https://..."
  }
]
```

---

## 🛠️ Built With

- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)
- **AI Model**: [Google Gemini API](https://ai.google.dev/)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more details.
