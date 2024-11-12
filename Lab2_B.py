owed_taxes = 0 #initiates the variable for the tax owed by the user
total_income = float(input("Enter your total income this year: ")) #gets the users year income and stores it in the variable total_income

#checks the users tax bracket based on there inputted year income and calculates the tax accordingly which then gets stored in the variable owed_tax
if (total_income > 0) and (total_income <= 11000):
    owed_taxes = total_income * 0.1
elif (total_income > 11000) and (total_income <= 44725):
    owed_taxes = ((total_income - 11000) * 0.12) + (11000 * 0.1)
elif (total_income > 44725) and (total_income <= 95375):
    owed_taxes = ((total_income - 44725) * 0.22) + ((44725 - 11000) * 0.12) + (11000 * 0.1)
elif (total_income > 95375) and (total_income <= 182100):
    owed_taxes = ((total_income - 95375) * 0.24) + ((95375 - 44725) * 0.22) + ((44725 - 11000) * 0.12) + (11000 * 0.1)
elif (total_income > 182100) and (total_income <= 231250):
    owed_taxes = ((total_income - 182100) * 0.32) + ((182100 - 95375) * 0.24) + ((95375 - 44725) * 0.22) + ((44725 - 11000) * 0.12) + (11000 * 0.1)
elif (total_income > 231250) and (total_income <= 578125):
    owed_taxes = ((total_income - 231250) * 0.35) + ((231250 - 182100) * 0.32) + ((182100 - 95375) * 0.24) + ((95375 - 44725) * 0.22) + ((44725 - 11000) * 0.12) + (11000 * 0.1)
elif (total_income > 578125):
    owed_taxes = ((total_income - 578125) * 0.37) + ((578125 - 231250) * 0.35) + ((231250 - 182100) * 0.32) + ((182100 - 95375) * 0.24) + ((95375 - 44725) * 0.22) + ((44725 - 11000) * 0.12) + (11000 * 0.1)

print(f"You owe ${owed_taxes:.2f} this year.") #displays the tax the user owes due to their income