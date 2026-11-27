import json
import os
from datetime import datetime

def log_audit(step, thought, tool, args, policy_result, execution_result):
    os.makedirs("traces", exist_ok=True)
    trace = {
        "timestamp": datetime.utcnow().isoformat(),
        "step": step,
        "thought": thought,
        "tool_call": {"tool": tool, "args": args},
        "policy_check": policy_result,
        "execution": execution_result
    }
    with open("traces/audit.jsonl", "a") as f:
        f.write(json.dumps(trace) + "\n")

def read_email(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def block_ip(ip_address):
    return f"Successfully blocked IP: {ip_address} (Simulated)" 