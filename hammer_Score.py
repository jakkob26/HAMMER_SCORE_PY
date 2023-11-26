print('Welcone to see your HAMMER FINANICAL SCORE')


income = input("What's your total yearly income? ")

income = int(income)

spending = input("Do you go over your budget? If so, how much? ")

spending = int(spending)

if spending > 0:
    spendingScore = 0
    print('Spending score is 0/10')
else:
    spendingScore = 10
    print('Spending score is 10/10')


debt = input("How much are you in debt? ")

debt = int(debt)

if debt > 0:
    debtScore = 0
    print('Debt score is 0/10')
else:
    debtScore = 10
    print('Debt score is 10/10')


emergency = input("How much do you have in your emergency fund? ")

emergency = int(emergency)

if emergency > 0:
    emergencyScore = 10
    print('Emergency score is 10/10')
else:
    emergencyScore = 0
    print('Emergency score is 0/10')


retirement = input("Whats in your retirement? ")

retirement = int(retirement)

if retirement > 0:
    retirementScore = 10 
    print('Retirement score is 10/10')
else:
    retirementScore = 0
    print('Retirement Score is 0/10')


realEstate = input("Do you own any real estate? ")

print(type(realEstate))

if realEstate == 'yes' or 'Yes': 
    realEstateScore = 10
    print("Real Estate score is 10/10")
else:
    realEstateScore = 0
    print('Real Estate score is 0/10')
    

