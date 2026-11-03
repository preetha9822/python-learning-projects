import pandas as pd
df=pd.read_csv("loans.csv")
print(df.head())
print("\n Total loans:",len(df))
print("Average loan:",df["loan_amount"].mean())
print("\nCount by status:")
print(df["status"].value_counts())
print("Average amount of status")
print(df.groupby("status")["loan_amount"].mean())
defaults=len(df[df["status"]=="default"])
total=len(df)
default_rate=defaults/total*100
print("Default rate as % :",round(default_rate,2))

import matplotlib.pyplot as plt

counts=df["status"].value_counts()
plt.bar(counts.index,counts.values)
plt.title("Loan by status")
plt.xlabel("Status")
plt.ylabel("Number of loans")
plt.yticks([0,1,2])
plt.savefig("loan_status.png")
plt.show()

avg=df.groupby("status")["loan_amount"].mean()
plt.bar(avg.index,avg.values)
plt.title("Average loan amount by status")
plt.savefig("loan_status_amount.png")
plt.show()