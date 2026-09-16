
age = int(input("Input your Age --> "))
is_employed = bool(input("Are you currently employed --> "))
credit_score = float(input("Credit Score --> "))
annual_income = float(input("What is your annual salary --> "))
has_collateral = bool(input("Do you have collateral (True/False) --> "))

base_rate = 0.0

if age >= 21 and is_employed == True:
    print("Accepted baseline Criteria")
    if annual_income >= 100000 :
        print("You have a high credit")
        base_rate = 4.5
        print("Your base rate is ", base_rate)
    else :
            base_rate = 5.0
            print("Your base rate is ", base_rate)
            if credit_score >= 600 and credit_score < 750 :
                print("Your credit score is less than 750")
            elif has_collateral == True :
                    print("You have a collateral ")
                    base_rate = 7.0
                    print("your base rate is ", base_rate)
            elif annual_income <= 40000 :
                        print("low annaul income")
                        base_rate = 9.0
                        print("your base rate is ", base_rate)
            else :
                            base_rate = 8.0
                            print("your base rate is ", base_rate)
                            if credit_score <= 600 :
                                print("Rejected : Credit score too low")
                            else:
                                    print("Rejected base line Criteria")