# program that calculates total pay based on user input of pay-rate and hours worked. Applies 1.5 rate for hours over 40

payDiff = 1.5
hoursWorkedSt = input("Enter Hours: ")
payRateSt = input("Enter Rate: ")
hoursWorked = float(hoursWorkedSt)
payRate = float(payRateSt)
overRate = payRate * payDiff
overPay = 0.0 
if hoursWorked > 40 :
    overPay = overRate * (hoursWorked - 40)
    totalPay = overPay + (40 * payRate)
else:
    totalPay = hoursWorked * payRate
print("Pay", totalPay)
