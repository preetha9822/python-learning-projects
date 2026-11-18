import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,recall_score,precision_score

df=pd.read_csv("loan_data.csv")
X=df.drop("default",axis=1)
y=df["default"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

print("Always-guess-no-default accuracy:",round(1-y_test.mean(),3))

model=RandomForestClassifier(n_estimators=100,random_state=42,class_weight="balanced")
model.fit(X_train,y_train)
pred=model.predict(X_test)
probs=model.predict_proba(X_test)[:,1]
for t in [0.5,0.4,0.3,0.2]:
    pred_t=(probs >=t).astype(int)
    print("threshold",t,"recall",round(recall_score(y_test,pred_t),2),
                                       "precision",round(precision_score(y_test,pred_t),2))
print("Model accuracy:",round(accuracy_score(y_test,pred),3))
print(classification_report(y_test,pred))
print(pd.Series(model.feature_importances_,index=X.columns).sort_values(ascending=False))
