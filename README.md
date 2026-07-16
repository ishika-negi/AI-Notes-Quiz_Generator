# 📄 AI PDF Notes & Quiz Generator

An AI-powered web application that transforms PDF documents into concise study notes and automatically generates quiz questions with answers using a Large Language Model (LLM). The application provides an intuitive interface for uploading PDFs and instantly receiving structured learning material, making studying more efficient and interactive.

---

## 📌 Overview

Reading lengthy PDFs and creating notes manually can be time-consuming. This project simplifies the learning process by allowing users to upload a PDF document and automatically generate:

*  Well-structured study notes
*  AI-generated quiz questions with answers

The application leverages **LangChain** for prompt orchestration, **DeepSeek LLM** for content generation, and **PyMuPDF** for extracting text from PDF documents.

---

## ✨ Features

*  Upload multiple PDF documents through an interactive web interface
*  Automatically generate concise and structured study notes
*  Generate quiz questions with answers from the uploaded document
*  AI-powered content generation using the DeepSeek LLM
*  Fast and user-friendly Streamlit interface
*  Supports educational documents, lecture notes, and study materials

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Frontend

* Streamlit

### AI Framework

* LangChain

### Large Language Model

* DeepSeek LLM

### PDF Processing

* PyMuPDF (fitz)

### Environment Variables

* python-dotenv

---

## 🏗️ Project Architecture

```text
                 Upload PDF
                      │
                      ▼
            Extract Text (PyMuPDF)
                      │
                      ▼
              LangChain Pipeline
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
    Generate Notes          Generate Quiz
          │                       │
          └───────────┬───────────┘
                      ▼
              Display Results
                (Streamlit UI)
```

---



## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/AI-PDF-Notes-Quiz-Generator.git
```

### 2️⃣ Navigate to the project folder

```bash
cd AI-PDF-Notes-Quiz-Generator
```

### 3️⃣ Create a virtual environment (Recommended)

```bash
python -m venv venv
```

### 4️⃣ Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 5️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Configure environment variables

Create a `.env` file in the project directory.

Example:

```env
DEEPSEEK_API_KEY=your_api_key_here
```

> Replace the variable name if your project uses a different environment variable.

### 7️⃣ Run the application

```bash
streamlit run AI_pdf_notes_generator.py
```

---

## 🚀 How to Use

1. Launch the Streamlit application.
2. Upload a PDF document.
3. Click the **Generate** button.
4. Wait for the AI to process the document.
5. View the generated study notes.
6. Review the quiz questions and answers.

---

## 📸 Application Screenshots



### Home Page

```
<img width="1276" height="422" alt="image" src="https://github.com/user-attachments/assets/859562e0-94c4-4b38-9c8e-a9f8b76c5092" />

```

### PDF Upload

```
<img width="865" height="348" alt="image" src="https://github.com/user-attachments/assets/e7f2b0db-1eb6-4c07-9b58-e712d9d0ef5f" />

```

### Generated Notes

```
<img width="1076" height="727" alt="image" src="https://github.com/user-attachments/assets/273b186b-eace-41fb-9787-b026e9dd49ea" />

```

### Quiz Generation

```
<img width="928" height="342" alt="image" src="https://github.com/user-attachments/assets/c51b2b7a-4c16-4da5-8ad5-5b4260d09320" />

```

---

## 💡 Use Cases

* Student exam preparation
* Lecture note summarization
* Learning from eBooks
* Quick revision before interviews
* Educational content generation
* Self-paced learning

---

## 🔮 Future Enhancements

* Export notes as PDF
* Flashcard generation
* Difficulty-based quizzes
* Chat with uploaded PDFs using Retrieval-Augmented Generation (RAG)
* Multi-language support
* Save previous sessions

---

## 📚 Key Concepts Demonstrated

* Large Language Models (LLMs)
* Prompt Engineering
* LangChain Pipelines
* PDF Text Extraction
* AI-powered Content Generation
* Streamlit Application Development
* Environment Variable Management

---

## 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Ishika Negi**

If you found this project useful, consider giving it a ⭐ on GitHub.
