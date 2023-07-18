import pandas as pd
import numpy as np

# Generate random data
np.random.seed(0)
data = pd.DataFrame({
    'Age': np.random.randint(18, 75, size=1000),
    'Income': np.random.randint(20000, 200000, size=1000),
    'Education': np.random.randint(1, 5, size=1000),
    'Employment_Years': np.random.randint(1, 30, size=1000),
    'Debt_Ratio': np.random.uniform(0.1, 0.6, size=1000),
    'Credit_Limit': np.random.randint(10000, 100000, size=1000),
    'Num_Credit_Cards': np.random.randint(1, 6, size=1000),
    'Num_Late_Payments': np.random.randint(0, 3, size=1000)
})

# Add condition for credit approval
data['Credit_Approval'] = np.where(
    (data['Age'] >= 20) & (data['Age'] <= 60) &
    (data['Income'] >= 20000) &
    (data['Employment_Years'] >= 2) &
    (data['Debt_Ratio'] <= 0.5) &
    (data['Credit_Limit'] >= 15000) &
    (data['Num_Credit_Cards'] >= 1) &
    (data['Num_Late_Payments'] == 0),
    1, 0
)

# Save the dataset to a CSV file
data.to_csv('credit_data.csv', index=False)
