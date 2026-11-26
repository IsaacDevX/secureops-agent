import threading

class KillSwitch:
    def __init__(self):
        self._event = threading.Event()
        self._event.clear()

    def trigger(self):
        """Triggers the kill switch, halting all operations."""
        print("\n🛑 [KILL SWITCH TRIGGERED] Aborting all operations!")
        self._event.set()

    def is_triggered(self):
        """Check if the kill switch has been flipped."""
        return self._event.is_set()
    
    def reset(self):
        """Resets the kill switch for a new run."""
        self._event.clear()
        print("✅ [KILL SWITCH] Reset complete. System ready.")
