import threading

class KillSwitch:
    def __init__(self):
        self._stop_event = threading.Event()

    def trigger(self):
        print("\n🚨 [KILL SWITCH ACTIVATED] 🚨")
        self._stop_event.set()

    def is_active(self):
        return self._stop_event.is_set()
    
    def reset(self):
        self._stop_event.clear() 