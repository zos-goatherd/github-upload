# program that calculates total pay based on user input of pay-rate and hours
# worked. Applies 1.5 rate for hours over 40


def computepay(hours, rate):
    '''Calculates total pay based on hours worked and pay rate. Calculates tim
    and a half for hours over 40

    Arguments:
    hours -- number of hours worked
    rate -- pay rate in dollars

    Returns: float
    '''

    payDiff = 1.5
    overRate = rate * payDiff
    overPay = 0.0
    if hours > 40.0:
        overPay = overRate * (hours - 40.0)
        totalPay = overPay + (40.0 * rate)
    else:
        totalPay = hours * rate
    return(totalPay)


hoursWorkedSt = input("Enter Hours: ")
payRateSt = input("Enter Rate: ")

try:
    hoursWorked = float(hoursWorkedSt)
    payRate = float(payRateSt)
except Exception:
    print("Error, please enter numeric input")
    hoursWorked = 0
    payRate = 0

print("Pay", computepay(hoursWorked, payRate))
