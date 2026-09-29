owner_age = int(input("Enter Your age --->  "))
revenue = float(input("Your monthly revenue --->  "))
credit = int(input("Your credit score --->  "))
years = float(input("Year in business ---->   "))
has_default = bool(input("Are you bankrupt? --->  "))
collateral_name = str(input("what collateral do you have ---->  "))
value = float(input("Value of your collateral --->  "))


base_fee = 0
loan = 0

if owner_age >= 21 and years >= 2.0 and has_default == False:
    print("Application passed")
    if credit >= 720:
        loan = 3 * revenue
        print("Maximum loan is set to", loan)
        print("High credit score")
        if revenue >= 50000:
            print("Revenue is higher than 50k")
            base_fee = loan * 0.015
            print("Base rate fee is set to", base_fee)
        else:
            print("Revenue lower that 50k")
            base_fee = loan * 0.025
            print("base rate fee is set to", base_fee)
            
        if value >= loan:
            print("Collateral", collateral_name, "with a value of ", value, "is ACCEPTED")
        else:
            print("Rejected: Insufficient collateral value for ", collateral_name)

        surge_fee_rate = loan * base_fee
        print("Additional Charge of ", surge_fee_rate)
        if loan % 500 != 0:
            print("Additional Charge Added")
            surge_fee_rate += 250
            print("Update base fee is ", surge_fee_rate)



    elif credit >= 620 and credit < 720:
        print("Credit score within range of 620 to 720")
        loan = 1.5 * revenue
        print("Maximum loan for this credit score is", loan)
        if years >= 5:
            print("years is more that 5 years")
            loan = loan * 0.02
        else:
            print("years is less that 5 years")
            base_fee = loan * 0.035
            print("base fee is set to", base_fee)

        if value >= loan:
            print("Collateral", collateral_name, "with a value of ", value, "is ACCEPTED")
        else:
            print("Rejected: Insufficient collateral value for ", collateral_name)
            
        surge_fee_rate = loan * base_fee
        print("Additional Charge of ", surge_fee_rate)
        if loan % 500 != 0:
            print("Additional Charge Added")
            surge_fee_rate += 250
            print("Update base fee is ", surge_fee_rate)


    else:
        print("Rejected: credit score below requirement")
            
else:
    print("Application did not passed")
