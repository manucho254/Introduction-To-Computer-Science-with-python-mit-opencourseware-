# house hunting program
# We need to calculate the months it will take to get the down payment
# The user will get a raise after every six months

annual_salary = float(input("Enter your annual salary: "))

total_cost = 1_000_000.0
semi_annual_raise = .07

portion_down_payment = total_cost * 0.25
current_savings = 0.0
months = 36

def monthly_salary(annual_salary: float) -> float:
    """ calculating the monthly salary from annual income """
    return annual_salary / 12

def investment(current_savings: float) -> float:
    """
      getting the investment monthly
    """
    return current_savings * (0.04 / 12)

def semi_raise_amount() -> float:
    """Get semi annual raise amount """
    return annual_salary * semi_annual_raise



epsilon = 100
num_guesses = 0
low = 0
high = portion_down_payment
guess = abs(high + low) / 2.0

while abs(guess**months-portion_down_payment) >= abs(epsilon):
    print('low = ' + str(low) + ' high = ' + str(high) + ' guess = ' + str(guess))
    if guess**months < portion_down_payment:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
    
print("num guesses = ", num_guesses)
print(guess, "is close to cube root of ", portion_down_payment)

print("Number of months: ", months)