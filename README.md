# 📚 Content Recommendation System

> **Major in Artificial Intelligence**
> **Indian Institute of Technology Ropar (IIT Ropar)**
> **November 2024 – June 2026**

An **AI-powered academic content recommendation system** designed to help engineering students discover relevant, high-quality textbooks and learning resources based on their **engineering branch, semester, and subject**.

The system uses **Google Gemini AI** to curate and rank relevant academic resources, provide concise explanations for recommendations, and offer direct access to available purchasing and educational resources.

---

## 🎓 Project Overview

This project was developed as the **final project of my Major in Artificial Intelligence conducted at IIT Ropar**, during the period **November 2024 to June 2026**.

The primary objective was to explore the application of **Artificial Intelligence and Large Language Models (LLMs)** in personalized academic content recommendation.

Instead of requiring students to search through large numbers of books and online resources manually, the system provides a focused set of recommendations based on the student's:

* Engineering branch
* Semester
* Subject
* Academic requirements

The recommendation engine uses **Google Gemini models** to generate and curate relevant textbook recommendations with explanations.

---

## ✨ Key Features

* 🤖 **AI-Powered Recommendations**
  Uses Google Gemini models to generate relevant academic content recommendations.

* 🎓 **Academic Personalization**
  Recommendations are tailored according to engineering branch, semester, and subject.

* ⭐ **Reputation-Based Ranking**
  Prioritizes well-established and widely recommended textbooks based on academic reputation and student preferences.

* 📖 **Detailed Book Information**
  Provides book titles, authors, and concise descriptions explaining why a resource may be useful.

* 🛒 **Purchase Links**
  Provides direct links to purchase recommended books through Amazon India where available.

* 🌐 **Free Resource Links**
  Provides links to freely available educational resources where applicable.

* ⚡ **Responsive Web Interface**
  Built with a lightweight and responsive frontend using HTML5, CSS3, and JavaScript.

* 🔄 **AI Model Fallback**
  Supports multiple Gemini models with fallback handling to improve reliability.

---

## 🧠 How It Works

The system follows a simple recommendation workflow:

```text
┌───────────────────────┐
│   Student Input       │
│                       │
│ Branch                │
│ Semester              │
│ Subject               │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Flask Backend       │
│                       │
│ Request Processing    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Google Gemini AI    │
│                       │
│ Content Analysis &    │
│ Recommendation        │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Recommended Resources │
│                       │
│ • Books               │
│ • Authors             │
│ • Descriptions        │
│ • Purchase Links      │
│ • Free Resources      │
└───────────────────────┘
```

---

## 🛠️ Technology Stack

### Backend

* **Python**
* **Flask**

### Artificial Intelligence

* **Google Gemini API**
* Gemini Flash models

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript**

### Development Tools

* Git
* GitHub
* Python Virtual Environment

---

## 📁 Project Structure

```text
content-recommendation-system/
│
├── app.py                  # Flask server & recommendation engine
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore configuration
│
├── templates/
│   └── index.html          # Main frontend interface
│
├── static/
│   ├── style.css           # UI styling
│   └── script.js            # Frontend logic & API requests
│
└── README.md               # Project documentation
```

The original project structure includes the Flask application, dependency file, frontend templates, static assets, and project documentation.

---

## 📋 Prerequisites

Before running the project, make sure you have:

* **Python 3.9 or later**
* A **Google Gemini API Key**

The original project specifies Python 3.9+ and a Gemini API key as the primary prerequisites.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/content-recommendation-system.git

cd content-recommendation-system
```

### 2. Create a Virtual Environment

#### Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Add your Google Gemini API key to the application configuration.

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

> **Important:** Never upload your actual API key to GitHub. Use environment variables or a `.env` file for production/development deployments.

The original implementation supports configuring the Gemini API key directly or through an environment variable.

### 5. Run the Application

```bash
python app.py
```

### 6. Open the Application

Once the Flask server starts, open:

```text
http://127.0.0.1:5000
```

The original project runs the Flask application locally on port `5000`.

---

## 📡 API

### `POST /get_books`

The API accepts the student's academic information and returns relevant textbook recommendations.

### Request

```json
{
  "branch": "Computer Science",
  "semester": "3",
  "subject": "Data Structures"
}
```

### Response

```json
[
  {
    "title": "Introduction to Algorithms",
    "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
    "description": "Recommended reference for algorithms and data structures.",
    "buy_link": "https://www.amazon.in/...",
    "free_link": "https://..."
  }
]
```

The implemented API endpoint is `/get_books` and accepts branch, semester, and subject information to generate recommendations.

---

## 🎯 Project Objectives

The major objectives of this project were:

1. To explore the use of **Artificial Intelligence in academic recommendation systems**.
2. To develop a personalized system for recommending educational content.
3. To utilize **Large Language Models** for intelligent content curation.
4. To reduce the time students spend searching for suitable academic resources.
5. To provide recommendations that are relevant to a student's academic context.
6. To develop and deploy an AI-powered application using a web-based interface.

---

## 🔬 Major Project Learning Outcomes

Through this project, I gained practical experience in:

* Artificial Intelligence
* Large Language Models (LLMs)
* Generative AI
* Prompt-based recommendation systems
* Google Gemini API integration
* Python backend development
* Flask web application development
* REST API integration
* Frontend and backend communication
* Git and GitHub
* Building an end-to-end AI application

---

## 🏫 Academic Context

| Detail           | Information                                      |
| ---------------- | ------------------------------------------------ |
| **Project Type** | Final Project                                    |
| **Program**      | Major in Artificial Intelligence                 |
| **Institution**  | Indian Institute of Technology Ropar (IIT Ropar) |
| **Duration**     | November 2024 – June 2026                        |
| **Domain**       | Artificial Intelligence / Generative AI          |
| **Project Area** | Content Recommendation System                    |

---

## 📌 Future Improvements

Possible future enhancements include:

* 👤 User profiles and personalized recommendation history
* ⭐ User feedback and rating-based recommendations
* 🧠 Hybrid recommendation using AI + traditional recommendation algorithms
* 📊 Recommendation analytics and performance evaluation
* 🔎 Semantic search for academic resources
* 📚 Support for research papers, courses, videos, and other learning materials
* 🔐 Secure API key management
* ☁️ Cloud deployment
* 📱 Improved mobile experience

---

## 📄 License

This project is distributed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Supratim Gogoi**

B.Tech — Computer Science & Engineering
Final Project — Major in Artificial Intelligence
**IIT Ropar | 2024–2026**

---

## ⭐ Acknowledgement

This project was completed as part of the **Major in Artificial Intelligence conducted by IIT Ropar**, serving as my final project during the program from **November 2024 to June 2026**.

---

> **Built with Python, Flask & Generative AI 🤖📚**
