# house hunting program
# We need to calculate the months it will take to get the down payment
# The user will get a raise after every six months

annual_salary = float(input("Enter your annual salary: "))
percent_to_save = float(input("Enter the percent of your salary to save as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

portion_down_payment = total_cost * 0.25
current_savings = 0.0
months = 0

def monthly_salary(annual_salary: float) -> float:
    """ calculating the monthly salary from annual income """
    return annual_salary / 12

def investment(current_savings: float) -> float:
    """
      getting the investment monthly
    """
    return current_savings * (0.04 / 12)

def semi_raise_amount(semi_annual_raise: float) -> float:
    """Get semi annual raise amount """
    return annual_salary * semi_annual_raise


portion_saved = monthly_salary(annual_salary) * percent_to_save

while current_savings != portion_down_payment:
    if current_savings >= portion_down_payment:
        break
    if months % 6 == 0 and months > 0: 
        """ 
          we check if the reminder of six divide by months == 0 and also check that the months value is greater than 0
          We reassign the values of annual salary and portion saved
        """
        annual_salary += semi_raise_amount(semi_annual_raise)
        portion_saved = monthly_salary(annual_salary) * percent_to_save
        
    current_savings += portion_saved + investment(current_savings)
    
    months += 1

print("Number of months: ", months)