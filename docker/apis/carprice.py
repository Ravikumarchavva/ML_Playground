import joblib
model=joblib.load('./docker/apis/models/churn.pkl')
print(model)