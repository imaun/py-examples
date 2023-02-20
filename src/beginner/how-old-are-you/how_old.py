import datetime

# HOW OLD ARE YOU ??
now = datetime.datetime.now()
year = int(input('Eneter Birthday (Year) : '))
month = int(input('Eneter Birthday (Month) : '))
day = int(input('Eneter Birthday (Day) : '))

birthday = datetime.datetime(year, month, day)

diff = now - birthday
print(type(diff))

passed_years = int(diff.days / 365)
m1 = diff.days - (passed_years * 365)
passed_months = int(m1 / 30)
days_passed = m1 - (passed_months * 30)

print(
    f'You are {passed_years} year(s), {passed_months} month(s) and {days_passed} day(s) old.')
