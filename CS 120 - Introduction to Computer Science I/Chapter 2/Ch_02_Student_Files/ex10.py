OVERTIME_RATE = 1.5

hourlyWage = float(input("Enter hourly wage: "))
regularHours = float(input("Enter regular hours: "))
overtimeHours = float(input("Enter overtime hours: "))

regularPay = hourlyWage * regularHours
overtimePay = overtimeHours * hourlyWage * OVERTIME_RATE
weeklyPay = regularPay + overtimePay

print("Weekly Pay: $" + str(weeklyPay))
