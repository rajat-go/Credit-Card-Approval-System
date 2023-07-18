from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('credit_data.csv')

# Preprocess the data
X = data.drop('Credit_Approval', axis=1)
y = data['Credit_Approval']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the machine learning model
model = RandomForestClassifier()
model.fit(X_train, y_train)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        age = int(request.form['age'])
        income = int(request.form['income'])
        education = int(request.form['education'])
        employment_years = int(request.form['employment_years'])
        debt_ratio = float(request.form['debt_ratio'])
        credit_limit = int(request.form['credit_limit'])
        num_credit_cards = int(request.form['num_credit_cards'])
        num_late_payments = int(request.form['num_late_payments'])

        # Create a new data sample
        new_data = pd.DataFrame({
            'Age': [age],
            'Income': [income],
            'Education': [education],
            'Employment_Years': [employment_years],
            'Debt_Ratio': [debt_ratio],
            'Credit_Limit': [credit_limit],
            'Num_Credit_Cards': [num_credit_cards],
            'Num_Late_Payments': [num_late_payments]
        })

        # Make a prediction using the trained model
        prediction = model.predict(new_data)[0]

        # Convert the prediction to a meaningful result
        result = 'Approved' if prediction == 1 else 'Not Approved'

        # Render the result page with the prediction
        return render_template('result.html', prediction=result)
    
    # Render the main page with the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
