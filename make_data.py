import numpy as np
import pandas as pd

rng=np.random.default_rng(42)
n=1000
income=rng.integers(15000,120000,n)
loan_amount=rng.integers(50000,1000000,n)
tenure_years=rng.integers(1,8,n)
past_delays=rng.poisson(1.0,n)
credit_score=np.clip(rng.normal(680,70,n),300,900).astype(int)

emi_ratio=(loan_amount/(tenure_years*12))/income
score=-3.0+4.0*emi_ratio+0.5*past_delays-0.01*(credit_score-680)
prob=1/(1+np.exp(-score))
default=(rng.random(n)<prob).astype(int)

df=pd.DataFrame({
    "monthly_income":income,
    "loan_amount":loan_amount,
    "tenure_years":tenure_years,
    "past_delays":past_delays,
    "credit_score":credit_score,
    "default":default,
})
df.to_csv("loan_data.csv",index=False)
print(df.head())
print("Default rate:",round(df["default"].mean()*100,1))


