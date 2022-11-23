# house hunting program

annual_salary = float(input("Enter your annual salary: "))
percent_to_save = float(input("Enter the percent of your salary to save as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary / 12
current_savings = 0.0
portion_saved = monthly_salary * percent_to_save
months = 0

def investment(current_savings: float) -> float:
    """
      getting the investment monthly
    """
    return current_savings * (0.04 / 12)

while current_savings != portion_down_payment:
    if current_savings >= portion_down_payment:
        break
    current_savings += portion_saved + investment(current_savings)
    months += 1

print("Number of months: ", months)