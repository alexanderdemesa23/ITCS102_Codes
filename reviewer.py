
age = int(input("Age --> "))
monthly_rev = float(input("Your Monthly Revenue --> "))
cs = int(input("Your credit Score is --> "))
years_in_business = float(input("Years in business --> "))
has_def = bool(input("Has a default ---> "))
col_name = input("Collateral name --> ")
coll_value = float(input("Collateral value --> "))

max_loan = 0.0
base_rate = 0.0

if age >= 21 and years_in_business >= 2.0 and has_def == False : 
    print("Baseline Accepted")
    if cs >= 720 : #Tier1
        print("Credit Score too high")
        max_loan = monthly_rev * 3
        if monthly_rev >= 50000 :
            print("Your monthly revenue is above 50k")
            base_rate = max_loan * 0.015
            print("Your base rate is ", base_rate)
        else:
            print("Your montly revenue is below 50k")
            base_rate = max_loan * 0.025
            print("Your base rate is ", base_rate)
            
            if coll_value >=  max_loan :
                print("Collateral ", col_name, "with a value of ", coll_value, "is Accepted")
            else:
                print("Rejected : Insufficient collateral value for ", col_name)
                
                if coll_value % 5000 != 0 :
                    base_rate += 250
                    print("Additional charge added to base fee, total base fee is ", base_rate)
                else:
                    print("collateral value divisible by 5000")                  
    elif cs <= 620 and cs < 720 : #Tier2
        print("Credit Score is equal of above 620")
        max_loan = monthly_rev * 1.5
        if years_in_business >= 5.0 :
            print("Your years in business is graterthan or equal to 5")
            base_rate = max_loan * 0.02
            print("Your Base rate ", base_rate)
        else:
            print("Your years in business is lessthan to 5")
            base_rate = max_loan * 0.035
            print("Your Base rate ", base_rate)
    elif cs < 620 : #Tier3
        print("Your crdit score is too low")
    else:
        print("Rejected : Credit Score below requirements")             
else:
    print("Baseline Decline")