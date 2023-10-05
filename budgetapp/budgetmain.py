import budget
from budget import create_spend_chart
from unittest import main

#THIS IS THE FIRST TEST DATA FROM BUDGET MAIN WHICH IMPORTS BUDGET PROGRAM
exec('{}={}'.format('food', '{}{}'.format('budget', '.category("food")')))
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
print('')

exec('{}={}'.format('clothing', '{}{}'.format('budget', '.category("clothing")')))
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

exec('{}={}'.format('auto', '{}{}'.format('budget', '.category("auto")')))
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

food.spent()
print(food)
print(auto)
print(clothing)

#THIS WILL PRINT THE SPEND CHART
print(create_spend_chart([food, clothing, auto]))

#THIS WILL RUN THE UNITTEST FROM BUDGETEST AUTOMATICALLY
main(module='budgetest', exit=False)
