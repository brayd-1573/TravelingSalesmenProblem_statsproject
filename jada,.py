import pandas as pd
import time
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Load the dataset
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([10, 20, 30])

# Set the learning rates to test
learning_rates = [0.1, 0.05, 0.01, 0.005, 0.001]

# Initialize lists to store the results
results = []
for rate in learning_rates:
    # Create a Gradient Boosting Regressor object
    gb_regressor = GradientBoostingRegressor(loss='squared_error', learning_rate=rate, n_estimators=100, max_depth=3)

    # Train the model on the dataset and measure the time taken
    start_time = time.time()
    gb_regressor.fit(X, y)
    end_time = time.time()

    # Predict the values for a new dataset
    X_new = np.array([[2, 3, 4], [5, 6, 7]])
    y_pred = gb_regressor.predict(X_new)

    # Compute the mean squared error
    mse = mean_squared_error([15, 25], y_pred)

    # Append the results to the list
    results.append([rate, mse, end_time - start_time])

# Create a Pandas DataFrame to store the results
df = pd.DataFrame(results, columns=['Learning Rate', 'Mean Squared Error', 'Computation Time'])

# Print the results table
print(df)
