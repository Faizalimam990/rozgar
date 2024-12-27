# Rozgar API

## Overview
Rozgar API is a simple RESTful API built using Flask and SQLAlchemy. It allows users to interact with a basic `users` table in a SQLite database. The API supports creating and retrieving users and managing their data securely.

This README will guide you through setting up and running the project on your local machine.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python** (version 3.7 or later) - You can download it from [python.org](https://www.python.org/downloads/).
- **pip** (Python's package installer) - Usually installed with Python.

---

## Setup Instructions

### 1. Clone the repository
If you haven't already, clone the repository to your local machine using Git.

```bash
git clone https://github.com/Faizalimam990/rozgar
cd rozgar-api
```
## 2. Create a virtual environment
It's highly recommended to create a virtual environment to keep the dependencies isolated for this project.

#### On Windows:
```bash
python -m venv venv
```

This Markdown code will display the activation commands clearly in the `README.md` file.

### Explanation:
- **Windows Command**: `venv\Scripts\activate` – This command activates the virtual environment on Windows.
- **macOS/Linux Command**: `source venv/bin/activate` – This command activates the virtual environment on macOS or Linux.

## 4. Install dependencies
Once the virtual environment is activated, install the necessary libraries using `pip`.

```bash
pip install -r requirements.txt
```
## 5. Run the application
Now that everything is set up, run the Flask application by executing the following command:

```bash
python app.py
