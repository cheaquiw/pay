# Calculate Gross Pay
def pay(regHours, rate):
        grossPay = regHours * rate
        return grossPay

# Calculate Net Pay
def netPay(gross):
    unionDues = 29.64 + 5.00
    fica = gross * .061997953829479
    ficaMed = gross * 0.0145004608948451
    fwt = gross * 0.0947113582723028
    swtOR = gross * 0.0607773422068253
    wbf = gross * 0.0006584212072406074
    return gross - unionDues - fica - ficaMed - fwt - swtOR - wbf

# Check Input for Correct Value of Hours
def checkInput(day, number):
    while True:
        try:
            hours = float(input(day + '\nNumber of ' + number + '?\n'))
        except ValueError:
            continue
        if 0.00 <= hours <= 24:
            return hours

# Check Input for Correct Value of Minutes
def minuteCheck(day, number):
    while True:
        try:
            minutes = float(input(day + '\nNumber of ' + number + '?\n'))
        except ValueError:
            continue
        if 0.00 <= minutes <= 60:
            return minutes

# Modify Hours to Meet Minimum Pay
def minimum(hours):
    if hours < 8:
        return 8
    else:
        return hours

# Get Variables for Calculation for Total Hours
def hoursConversion(day):
    hours = checkInput(day, 'regular hours')
    minutes = minuteCheck(day, 'regular minutes')
    otHours = checkInput(day, 'Over Time hours')
    otMinutes = minuteCheck(day, 'Over Time minutes')
    makeupTime = minuteCheck(day, 'makeup time in minutes')
    return float((hours + minutes / 60) + ((otHours + otMinutes / 60) - makeupTime / 60) * 1.5)

# Hours for Daly Input
day1 = hoursConversion('Week 1 Monday')
day2 = hoursConversion('Week 1 Tuesday')
day3 = hoursConversion('Week 1 Wednesday')
day4 = hoursConversion('Week 1 Thursday')
day5 = hoursConversion('Week 1 Friday')
day6 = hoursConversion('Week 2 Monday')
day7 = hoursConversion('Week 2 Tuesday')
day8 = hoursConversion('Week 2 Wednesday')
day9 = hoursConversion('Week 2 Thursday')
day10 = hoursConversion('Week 2 Friday')

# Calculates Total Number of Hours
hoursOfPay = minimum(day1) + minimum(day2) + minimum(day3) + minimum(day4) + minimum(day5) + minimum(day6) + minimum(
    day7) + minimum(day8) + minimum(day9) + minimum(day10)

rateOfPay = 20.11

print('Gross Pay: ' + str(round(pay(hoursOfPay, rateOfPay), 2)))

print('Net Pay: ' + str(round(netPay(pay(hoursOfPay, rateOfPay)), 2)))