from datetime import datetime
from loguru import logger

class Note:
    def __init__(self, date_note: datetime, title_note: str, note: str):
        self.date_note = date_note
        self.title_note = title_note
        self.note = note

    @logger.catch
    def set(self, date_note, title_note, note):
        self.date_note = date_note
        self.title_note = title_note
        self.note = note

    @logger.catch
    def get(self):
        data_note = {}
        data_note['date_created'] = self.date_note
        data_note['title_note'] = self.title_note
        data_note['note'] = self.note
        return data_note

    @logger.catch
    def __str__(self):
        return f'{self.date_note} {self.title_note} {self.note}'

