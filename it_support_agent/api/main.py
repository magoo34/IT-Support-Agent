from fastapi import FastAPI
from agent.engine import SupportAgentEngine

app = FastAPI()
engine = SupportAgentEngine()

@app.get("/")
def root():
    return {"status": "running", "agent": "IT Support Troubleshooting Agent"}

@app.get("/troubleshoot")
def troubleshoot(user: str, message: str, hostname: str = "Unknown"):
    response = engine.run(user, message, hostname)
    return {"response": response}
