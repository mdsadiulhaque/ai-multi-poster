# AI Multi-Poster Backend

## Setup
1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run locally:
```bash
uvicorn app.main:app --reload
```

4. Environment variables:
Copy `.env.example` to `.env` and fill in your API keys.

## Deployment
You can deploy this backend to Railway, Render, or any cloud provider that supports Python.
