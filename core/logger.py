
import csv
from core.models import LogEntry

class CSVLogger:
    def __init__(self, file_path='log.csv'):
        self.file_path = file_path

    def write_entry(self, entry: LogEntry):
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([entry.timestamp, entry.text])
