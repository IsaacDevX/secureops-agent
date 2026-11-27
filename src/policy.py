import re

class PolicyEngine:
    def __init__(self):
        self.destructive_patterns = [
            r"rm\s+-rf", r"mkfs", r"dd\s+if", r"iptables", r"shutdown", r"reboot"
        ]
        self.blocked_domains = ["example.com", "example.org", "example.net", "attacker"]

    def evaluate(self, tool_name, arguments):
        if tool_name == "send_email" or tool_name == "fetch_url":
            payload_str = str(arguments).lower()
            for domain in self.blocked_domains:
                if domain in payload_str:
                    return "BLOCKED", f"Security Violation: Attempted to contact untrusted domain '{domain}'."

        if tool_name == "run_command":
            cmd = arguments.get("command", "")
            for pattern in self.destructive_patterns:
                if re.search(pattern, cmd, re.IGNORECASE):
                    return "BLOCKED", f"Security Violation: Destructive command detected ({pattern})."

        if tool_name in ["send_email", "delete_file"]:
            return "REQUIRES_APPROVAL", f"Action '{tool_name}' requires human authorization."

        return "ALLOWED", "Safe to execute."