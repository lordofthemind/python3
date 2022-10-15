def calc():
    print("This is a monthly payment loan calculator.")
    print("")

    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    year = int(input("Enter years: "))
    
    mnthly_IR = apr / 1200
    mnths = year * 12
    mnthly_pmnt = principal * mnthly_IR /(1 - (1 + mnthly_IR) ** (-mnths))
    print("The monthly payment for thid loan is "+ str(mnthly_pmnt))


calc()