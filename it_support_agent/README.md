# IT Support Troubleshooting Agent (Clean Package)

This is a cleaned, minimal, fully-indented and runnable project structure intended for local development or Kaggle environments.

Files included:
- api/main.py : FastAPI server
- agent/* : engine, llm, workflows, kb
- cli/agent_cli.py : simple Typer CLI
- data/* : sample KB and workflows
- requirements.txt

Usage (local):
1. Install dependencies: pip install -r requirements.txt
2. Add project path to PYTHONPATH or run from project root
3. Run server: uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

Note: In Kaggle you need to ensure the working directory and PYTHONPATH include the project folder. See examples in the README.
