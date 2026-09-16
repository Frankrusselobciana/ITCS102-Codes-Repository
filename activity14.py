age = int(input("Enter your age  -->  "))
is_employed = bool(input("Are you employed? (True / False) -->  "))
credit_score = int(input("Enter your current credit score --->  "))
annual_income = float(input("How much is your annual income? --->  "))
has_collateral = bool(input("Do you have collateral? (True / False) --->  "))

base_rate = 0.0

if age >= 21 and is_employed == True:
	print("Applicant pass baseline requirement")
	if credit_score >= 750: #tier1
		print("You have high credit score")
		if annual_income >= 100000:
			base_rate = 4.5
			print("You have high salary and high credit score, your interest rate is",base_rate)
		else:
		    base_rate = 5.0
		    print("You got a loyalty discount, final rate is",base_rate)
	elif credit_score >= 600 and credit_score < 750:
		if has_collateral == True:
		    base_rate = 7.0
		    print("Approved, Reduce the rate to",base_rate)
		elif annual_income <= 40000:
		    print("Low Salary with Fair Credit Score")
		    base_rate = 9.5
		    print("Approved, increase the risk rate to",base_rate)
		else:
		    print("Fair credit score with no collateral")
		    base_rate = 8.0
		    print("Base interest rate",base_rate)
	elif credit_score < 600:
		    print("Rejected: Credit score is too low")
	else:
	    print("Failed")

