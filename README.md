# 🚀 GenAI Day 1: AI Agents & Prompt Engineering

Welcome to the **GenAI Day 1** project repository. This collection contains four comprehensive tasks demonstrating advanced AI agent orchestration, prompt engineering patterns, and real-world AI applications.

**Developed by [Ashutosh Ranjan](https://github.com/ashu-ranjan)**

---

## 📂 Repository Structure

This repository is organized into four main tasks, each showcasing a different aspect of Generative AI development:

### 1. [Task 1: Reasoning Agent Web App](./Task_1)
- **Concept**: Implements a **ReAct (Reason + Act)** loop for grounded question answering.
- **Tech Stack**: Flask, Python, DuckDuckGo API.
- **Key Features**:
    - Thought → Action → Observation sequence.
    - Intelligent web search triggers only when needed.
    - Step-by-step reasoning transparency in the UI.

### 2. [Task 2: Math CoT Solver](./Task_2)
- **Concept**: A high-speed **Chain-of-Thought (CoT)** mathematical reasoning engine.
- **Tech Stack**: FastAPI, Groq/OpenAI, Modern Neon UI.
- **Key Features**:
    - Cyberpunk-themed "Neon Dark" interface.
    - Automatic mathematical verification.
    - Hidden internal reasoning with structured user-facing summaries.

### 3. [Task 3: Code Review Agent](./Task_3)
- **Concept**: An intelligent agent for automated **Python code analysis**.
- **Tech Stack**: FastAPI, OpenAI, AST (Abstract Syntax Trees).
- **Key Features**:
    - Static analysis combined with multi-round AI review.
    - File upload support for `.py` files.
    - Detailed feedback on complexity, style (PEP 8), and security.

### 4. [Task 4: Customer Support Chatbot (3 Patterns)](./Task_4)
- **Concept**: A production-ready support bot demonstrating **three distinct prompt architectures**.
- **Tech Stack**: FastAPI, OpenAI, Neon Yellow UI.
- **Key Patterns**:
    - 🔧 **ReAct**: Tool-using agent with explicit reasoning traces.
    - 🧠 **Chain-of-Thought**: Logical analysis with concise summaries.
    - ✨ **Self-Reflecting**: Multi-phase draft → critique → revise cycle for premium quality.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- [OpenAI API Key](https://platform.openai.com/) (Required for Tasks 2, 3, and 4)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ashu-ranjan/GenAI_Day1.git
   cd GenAI_Day1
   ```

2. **Setup Task Environments**:
   Each task folder contains its own `requirements.txt`. It is recommended to use virtual environments:
   ```bash
   cd Task_X
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Configure API Keys**:
   Create a `.env` file in the task directory (or root) as specified in the individual task READMEs:
   ```env
   OPENAI_API_KEY=your_actual_key_here
   ```

---

## 🛠️ Security & Best Practices

- **API Security**: All `.env` files and sensitive credentials are automatically ignored via the root `.gitignore`.
- **Modular Design**: Each task is a self-contained application but follows common coding standards.
- **Modern UI/UX**: Interfaces are designed to be responsive, accessible, and visually stunning.

---

## 🤝 Contributing & Feedback

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

---

**Built with ❤️ by Ashutosh Ranjan using FastAPI, OpenAI, and Modern Web Tech**
