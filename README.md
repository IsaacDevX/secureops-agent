# SecureOps Agent

An autonomous, safety-gated security operations agent. 

## Quick Start (For Judges)
1. Clone the repo: `git clone ...`
2. Setup environment: `python -m venv venv` && `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Configure keys: `cp .env.example .env` (Add your LLM API key)
5. Run the agent: `python src/main.py`

## Documentation
- [AGENT.md](AGENT.md): Architecture and tools.
- [SAFETY.md](SAFETY.md): Guardrails, Kill Switch, and Monitoring.

## Demo
https://youtu.be/kfZOkMY2Mz4
### Demo
To see the human-in-the-loop guardrail in action:
1. Run `python src/main.py test-threat.txt`
2. The agent will propose blocking an IP.
3. The Policy Engine will intercept the action and require human authorization.
