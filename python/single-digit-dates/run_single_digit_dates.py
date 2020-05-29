from datetime import date
from single_digit_dates import SingleDigitDates
d = date(12,1,1)
s = SingleDigitDates(d)
print(s.next())
print(s.next())


