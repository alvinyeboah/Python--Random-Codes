import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

dataset_path = "winningnumbers.csv"  
data = pd.read_csv(dataset_path)


X = data[['Number_1', 'Number_2', 'Number_3', 'Number_4', 'Number_5']].values
y = data['Number_6'].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


num_sets = 5
predicted_sets_1_to_70 = []
predicted_number_1_to_25_list = []  
for _ in range(num_sets):
    random_index = np.random.randint(len(X_test)) 
    test_data = [X_test[random_index]] 
    
    
    predicted_set = model.predict(test_data)
    predicted_set = np.clip(np.round(predicted_set), 1, 70).astype(int)
    predicted_sets_1_to_70.append(predicted_set)

for _ in range(1):
    random_index = np.random.randint(len(X_test))  
    test_data = [X_test[random_index]] 
    predicted_number_1_to_25 = np.random.randint(1, 25)
    predicted_number_1_to_25_list.append(predicted_number_1_to_25)

# Step 6: Display the predicted numbers
print("Predicted 5 sets of 5 numbers between 1 and 70:")
for set_numbers in predicted_sets_1_to_70:
    print(set_numbers.tolist())

print("Predicted 6th number between 1 and 25 for each set:", predicted_number_1_to_25_list)
