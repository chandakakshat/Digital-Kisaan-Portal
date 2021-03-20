import numpy as np        
import pandas as pd       
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier


def recommend_helper():
    
    train_data = pd.read_csv("crop.csv")
    
    le = LabelEncoder()
    train_data.crop = le.fit_transform(train_data.crop)
    
    X = train_data.drop('crop', axis = 1)
    y = train_data['crop']  
    
    X_train, X_val, y_train, y_val = train_test_split(X,y,test_size=0.3)
    
    model = RandomForestClassifier(n_estimators=150)
    
    model.fit(X_train, y_train)
    
    return model, le


def recommend(N, P, K, T, H, ph, R):
    
    A = [N, P, K, T, H, ph, R] 
    
    model, le = recommend_helper()
    
    S = np.array(A)
    X = S.reshape(1, -1)
    
    pred = model.predict(X)
    
    crop_pred = le.inverse_transform(pred)

    return crop_pred[0]



print(recommend(17.0000001, 36.000000, 196.00000, 23.871923, 90.499390, 5.882156, 10))