
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
df=pd.read_csv('index/Health_Set.csv')
df['RiskLevel']=df['RiskLevel'].replace(['low risk'],0)
df['RiskLevel']=df['RiskLevel'].replace(['mid risk'],1)
df['RiskLevel']=df['RiskLevel'].replace(['high risk'],2)
x=df[["Age","SystolicBP","DiastolicBP","BS","HeartRate"]]
y=df['RiskLevel']
Forest=RandomForestClassifier(n_estimators=20)
Forest.fit(x,y)
Column_names=["Age","SystolicBP","DiastolicBP","BS","HeartRate"]