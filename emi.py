import math

def calculate_emi(principal,annual_rate,years) :  
    r=annual_rate/12/100
    n=years*12
    emi=principal*r*(1+r)** n/((1+r)** n-1)
    total_payment=emi*n
    total_int=total_payment-principal
    return emi,total_payment,total_int

principal=float((input("Loat amount: ")))
annual_rate=float(input("Yearly interest rate(%): "))
years=int(input("Laon period (years): "))

emi,total_payment,total_int=calculate_emi(principal,annual_rate,years)
print(f"Monthly EMI:{math.ceil(emi)}")
print(f"Toatal Payment:{total_payment:.2f}")
print(f"Total interest:{total_int:.2f}")

