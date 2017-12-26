def valid_year(year):
    if year and year.isdigit():
        year=int(year)
    if year>0 and year<=2050:
        return year

print(valid_year('2000'))
