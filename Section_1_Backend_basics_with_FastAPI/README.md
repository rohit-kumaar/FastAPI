# Section 1: Backend Basics with FastAPI

Welcome to the FastAPI Backend Development course repository! This project demonstrates how to set up, build, and run a modern Python backend using FastAPI, Uvicorn, and standard Python virtual environments.

---

## 📋 Prerequisites

Before getting started, make sure you have the following installed on your system:

- **Python**: `v3.10+` (Python 3.14 or later recommended)
- **Git**: Installed and configured
- **Terminal**: PowerShell (Windows), Command Prompt, or Bash (Linux/macOS)

---

## 🚀 Step-by-Step Setup & Terminal Commands

Follow these terminal commands step by step to set up, run, and work with this project.

### Step 1: Clone or Navigate to the Project Directory

Open your terminal and navigate to the project root folder:

```bash
# Navigate to the project folder
cd Section_1_Backend_basics_with_FastAPI
```

---

### Step 2: Create a Virtual Environment

Isolate project dependencies by creating a dedicated Python virtual environment (`venv`).

**On Windows (PowerShell / Command Prompt):**
```powershell
python -m venv venv
```

**On macOS / Linux:**
```bash
python3 -m venv venv
```

---

### Step 3: Activate the Virtual Environment

Activate the virtual environment in your terminal session.

**On Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

> **Note for Windows PowerShell Users:** If you encounter an execution policy error, run this once:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**On Windows (Command Prompt `cmd.exe`):**
```cmd
venv\Scripts\activate.bat
```

**On Git Bash / Bash on Windows:**
```bash
source venv/Scripts/activate
```

**On macOS / Linux:**
```bash
source venv/bin/activate
```

*When activated, your terminal prompt will display `(venv)` at the beginning.*

---

### Step 4: Install Dependencies

Install FastAPI along with standard server dependencies (`uvicorn`, `email-validator`, `pydantic`, `watchfiles`, etc.):

```bash
pip install "fastapi[standard]"
```

Or install specific core packages individually:
```bash
pip install fastapi uvicorn
```

*(Optional)* Save dependencies to a `requirements.txt` file:
```bash
pip freeze > requirements.txt
```

---

### Step 5: Create your Main FastAPI Application File

Create a starter `main.py` file with basic FastAPI endpoints:

**On Windows (PowerShell):**
```powershell
New-Item -ItemType File -Name main.py
```

**On macOS / Linux:**
```bash
touch main.py
```

Add the following sample code inside `main.py`:

```python
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Backend Basics",
    description="Getting started with FastAPI",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Backend Basics!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

---

### Step 6: Run the FastAPI Server

Start the development server with live auto-reload enabled:

```bash
uvicorn main:app --reload
```

Optionally, specify host and port:
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

---

### Step 7: Access API Documentation & Endpoints

Once the server is running, open your web browser and visit:

| Endpoint | URL | Description |
| :--- | :--- | :--- |
| **Root API** | `http://127.0.0.1:8000/` | Basic welcome response |
| **Interactive Docs (Swagger UI)** | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) | Test APIs interactively |
| **Alternative Docs (ReDoc)** | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) | Clean API reference |

---

### Step 8: Deactivate Virtual Environment

When you are done working, exit the virtual environment:

```bash
deactivate
```

---

## 🛠️ Summary of Common Commands

| Task | Command |
| :--- | :--- |
| Create venv | `python -m venv venv` |
| Activate venv (PowerShell) | `.\venv\Scripts\Activate.ps1` |
| Activate venv (CMD) | `venv\Scripts\activate.bat` |
| Activate venv (Git Bash) | `source venv/Scripts/activate` |
| Activate venv (macOS/Linux) | `source venv/bin/activate` |
| Install FastAPI | `pip install "fastapi[standard]"` |
| Run Server | `uvicorn main:app --reload` |
| Deactivate venv | `deactivate` |

---

## 📁 Recommended Project Directory Structure

```text
Section_1_Backend_basics_with_FastAPI/
├── venv/                 # Virtual environment (git-ignored)
├── main.py               # Main FastAPI entry point
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```
