import shlex

class PolicyEngine:
    def __init__(self):
        self.destructive_commands = ["rm", "mkfs", "dd", "iptables", "shutdown", "reboot"]
        self.requires_approval = ["block_ip", "delete_file"]

    def evaluate_action(self, action_type, payload):
        """Evaluates if an action is safe to execute."""
        
        # Rule 1: Check for destructive shell commands
        if action_type == "shell":
            try:
                tokens = shlex.split(payload)
                if tokens[0] in self.destructive_commands:
                    return {"status": "BLOCKED", "reason": f"Destructive command '{tokens[0]}' detected."}
            except Exception:
                return {"status": "BLOCKED", "reason": "Malformed shell command."}

        # Rule 2: Check for actions requiring human approval
        if action_type in self.requires_approval:
            return {"status": "REQUIRES_APPROVAL", "reason": f"Action '{action_type}' requires human confirmation."}

        return {"status": "ALLOWED", "reason": "Action passed all policy checks."}
