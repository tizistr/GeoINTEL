
from ui.view import LoggerView
from core.logger import CSVLogger
from core.models import LogEntry
from adapters.voice_input import VoiceInput

class VoiceLoggerController:
    def __init__(self):
        self.logger = CSVLogger()
        self.voice = VoiceInput()
        self.view = LoggerView(self.handle_voice_input)

    def handle_voice_input(self):
        text = self.voice.listen_and_transcribe()
        log_entry = LogEntry.create(text)
        self.logger.write_entry(log_entry)
        self.view.update_log_display(f"{log_entry.timestamp}: {log_entry.text}")

    def run(self):
        self.view.run()
