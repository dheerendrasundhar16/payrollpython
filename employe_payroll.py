def calculate_basic_salary(hourly_rate, hours_worked):
    basic_salary = hourly_rate * hours_worked
    return basic_salary

print("basicsalaray")
hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter the number of hours worked in a week: "))

basic_salary = calculate_basic_salary(hourly_rate, hours_worked)
print(f"Basic Salary: {basic_salary:.2f}")
#overtime
def calculate_overtime_pay(hourly_rate, hours_worked):
    regular_hours = 40
    overtime_rate = 1.5 * hourly_rate
    overtime_pay = 0
    
    if hours_worked > regular_hours:
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * overtime_rate
        
    return overtime_pay

# Input
hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter the number of hours worked in a week: "))

overtime_pay = calculate_overtime_pay(hourly_rate, hours_worked)
print(f"Overtime Pay: {overtime_pay:.2f}")
#total pay
def calculate_total_pay(hourly_rate, hours_worked, tax_rate):
    basic_salary = hourly_rate * hours_worked
    tax_deduction = basic_salary * (tax_rate / 100)
    total_pay = basic_salary - tax_deduction
    return total_pay, basic_salary, tax_deduction

# Input
print("basic totalpay ")
hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter the number of hours worked in a week: "))
tax_rate = float(input("Enter your tax rate (as a percentage): "))

total_pay, basic_salary, tax_deduction = calculate_total_pay(hourly_rate, hours_worked, tax_rate)
print(f"Basic Salary: {basic_salary:.2f}")
print(f"Tax Deduction: {tax_deduction:.2f}")
print(f"Total Pay (after tax): {total_pay:.2f}")
#bonus
def calculate_bonus_and_total_pay(hourly_rate, hours_worked, bonus_percentage):
    basic_salary = hourly_rate * hours_worked
    bonus = basic_salary * (bonus_percentage / 100)
    total_pay = basic_salary + bonus
    return total_pay, basic_salary, bonus

# Input
print("bonusand total pay")
hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter the number of hours worked in a week: "))
bonus_percentage = float(input("Enter your bonus percentage: "))

total_pay, basic_salary, bonus = calculate_bonus_and_total_pay(hourly_rate, hours_worked, bonus_percentage)
print(f"Basic Salary: {basic_salary:.2f}")
print(f"Bonus: {bonus:.2f}")
print(f"Total Pay (including bonus): {total_pay:.2f}")
#totalpayroll
def calculate_total_payroll(hourly_rate, hours_worked, bonus_percentage, tax_rate):
    # Basic Salary Calculation
    basic_salary = hourly_rate * hours_worked
    
    # Overtime Pay Calculation
    regular_hours = 40
    overtime_rate = 1.5 * hourly_rate
    overtime_pay = 0
    if hours_worked > regular_hours:
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * overtime_rate
    
    # Bonus Calculation
    bonus = basic_salary * (bonus_percentage / 100)
    
    # Tax Deduction Calculation
    tax_deduction = basic_salary * (tax_rate / 100)
    
    # Total Pay Calculation
    total_pay = basic_salary + overtime_pay + bonus - tax_deduction
    return total_pay, basic_salary, overtime_pay, tax_deduction, bonus

# Input
print("total payroll")
hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter the number of hours worked in a week: "))
bonus_percentage = float(input("Enter your bonus percentage: "))
tax_rate = float(input("Enter your tax rate (as a percentage): "))

total_pay, basic_salary, overtime_pay, tax_deduction, bonus = calculate_total_payroll(hourly_rate, hours_worked, bonus_percentage, tax_rate)
print(f"Basic Salary: {basic_salary:.2f}")
print(f"Overtime Pay: {overtime_pay:.2f}")
print(f"Bonus: {bonus:.2f}")
print(f"Tax Deduction: {tax_deduction:.2f}")
print(f"Total Pay: {total_pay:.2f}")
#monthlysalary
def calculate_monthly_salary(hourly_rate, hours_worked_per_week):
    weekly_salary = hourly_rate * hours_worked_per_week
    monthly_salary = weekly_salary * 4  # Assuming 4 weeks in a month
    return monthly_salary

# Input
print("monthly payroll")
hourly_rate = float(input("Enter your hourly rate: "))
hours_worked_per_week = float(input("Enter the number of hours worked per week: "))

monthly_salary = calculate_monthly_salary(hourly_rate, hours_worked_per_week)
print(f"Monthly Salary: {monthly_salary:.2f}")