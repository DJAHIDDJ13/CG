import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

leap_year = int(input())
inputs = input().split()
source_day_of_week = inputs[0]
source_month = inputs[1]
source_day_of_month = int(inputs[2])
inputs = input().split()
target_month = inputs[0]
target_day_of_month = int(inputs[1])

months_names = ['Jan', 'Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

months_len = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = {n:l for n,l in zip(months_names, months_len)}
months_cumul = {}
cumul = 0
for m in months:
    months_cumul[m] = cumul
    cumul += months[m]
get_day = lambda m, d: months_cumul[m] + d-1

weekdays = ['Monday', 'Tuesday', "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

numdays = 366 if leap_year else 365
strt = get_day(source_month, source_day_of_month)
day = weekdays.index(source_day_of_week)
days = ['']*numdays
for i in list(range(strt, numdays)) + list(range(0, strt)):
    days[i] = weekdays[(day+i-strt)%7]
print(days[get_day(target_month, target_day_of_month)])