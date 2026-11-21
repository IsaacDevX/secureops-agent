# Agent Architecture

## Role
The SecureOps Agent acts as an autonomous Tier-1 Security Operations Center (SOC) analyst. It ingests raw logs and alerts, correlates events to detect threats (e.g., brute-force attacks, SQL injection patterns), and proposes remediations.

## Track
Open Track

## Stack
- **Language:** Python 3.10+
- **Brain:** Llama-3-70B (via API) for reasoning.
- **Safety Layer:** Custom Python `policy.py` (Deterministic guardrails).
- **UI:** `rich` library for Terminal Monitoring.

## Tools & Permissions
The agent has access to the following tools, which are strictly monitored by the Policy Engine:
1. `read_log(filepath)`: Can only read from the `/logs` directory.
2. `analyze_ip(ip)`: Queries a threat intel API.
3. `propose_block(ip)`: **Requires Human Approval.**

## Safety
Please see [SAFETY.md](SAFETY.md) for a detailed breakdown of our guardrails, kill switch, monitoring, and audit trails.
