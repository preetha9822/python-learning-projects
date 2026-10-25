import math
emi=0.0
total_payment=0.0
total_int=0.0
principal=float((input("Loat amount: ")))
annual_rate=float(input("Yearly interest rate(%): "))
years=int(input("Laon period (years): "))
def calculate_emi(principal,annual_rate,years) :  
    r=annual_rate/12/100
    n=years*12
    emi=principal*r*(1+r)** n/((1+r)** n-1)
    total_payment=emi*n
    total_int=total_payment-principal
    print(f"Monthly EMI:{math.ceil(emi)}")
    print(f"Toatal Payment:{total_payment:.2f}")
    print(f"Total interest:{total_int:.2f}")
calculate_emi(principal,annual_rate,years)

