
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogEntry:
    timestamp: str
    text: str

    @staticmethod
    def create(text: str):
        return LogEntry(timestamp=datetime.now().isoformat(), text=text)
