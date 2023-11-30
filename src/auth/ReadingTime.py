import re


class ReadingTime:
    def __init__(self, text):
        self.text = text
    
    def calculate_reading_time(self, ppm=200):
        words = re.findall(r'\b\w+\b', self.text)

        number_words = len(words)

        estimated_time_minutes = number_words / ppm

        return estimated_time_minutes
