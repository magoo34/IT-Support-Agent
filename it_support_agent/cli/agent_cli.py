import typer
from agent.engine import SupportAgentEngine

app = typer.Typer()
engine = SupportAgentEngine()

@app.command()
def troubleshoot(user: str, message: str, hostname: str = "Unknown"):
    response = engine.run(user, message, hostname)
    typer.echo(response)

if __name__ == "__main__":
    app()
