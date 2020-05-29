from datetime import timedelta

class SingleDigitDates():
    
    def __init__(self, start):
        self.date = start
        while not self.valid():
            self.date = self.date + timedelta(days=1)
    
    def valid(self):
        digits = set()
        digits.update([c for c in str(self.date.month)])
        digits.update([c for c in str(self.date.day)])
        digits.update([c for c in str((self.date.year % 100))])
        return len(digits) == 1

    def next(self):
        d = self.date
        self.date = self.date + timedelta(days=1)
        while not self.valid():
            self.date = self.date + timedelta(days=1)
        return d
