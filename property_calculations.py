
def mortgage_monthly(price,years,percent):
    #This implements an approach to finding a monthly mortgage amount from the purchase price,
    #years and percent. 
    #Sample input: (300000,20,4) = 2422
    #
    percent = percent /100
    down = down_payment(price,20)
    loan = price - down
    months = years*12
    interest_monthly = percent/12
    interest_plus = interest_monthly + 1
    exponent = (interest_plus)**(-1*months)
    subtract = 1 - exponent
    division = interest_monthly / subtract
    payment = division * loan
    
    
    return(payment)

def down_payment(price,percent):
    #This function takes the price and the downpayment rate and returns the downpayment amount 
    #Ie down_payment(100,20) returns 20
    amt_down = price*(percent/100)
    return(amt_down)

def net_operating(rent, tax_rate, price):
    
    #Takes input as monthly mortgage amount and monthly rental amount
    #Uses managment expense, amount for repairs, vacancy ratio
    #Example input: net_operating(1000,1,400,200)
    #879.33
    #1000 - 16.67 (tax) - 100 (managment) - 4 (repairs)
    
    mortgage_amt = mortgage_monthly(price,20,3)
    prop_managment = rent * 0.10
    prop_tax = (price * (tax_rate/100)/12)
    prop_repairs = (price * 0.02)/12
    vacancy = (rent*0.02)
    #These sections are a list of all the expenses used and formulas for each
    
    net_income = rent - prop_managment - prop_tax - prop_repairs - vacancy - mortgage_amt
    #Summing up expenses
    output = [prop_managment, prop_tax, prop_repairs, vacancy, net_income]
  
    
    return output

def cap_rate(monthly_income, price):
    #This function takes net income, and price and calculates the cap rate
    #
    cap_rate = ((monthly_income*12) / price)*100
    
    return cap_rate
