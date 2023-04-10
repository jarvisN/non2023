import numpy as np
from multiprocessing import Pool
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt

def find_best_params(param_range):
    """
    Find the best C and gamma values for SVM model with RBF kernel
    """
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv('data/Fish.csv')

    # Encode the 'Species' column using LabelEncoder
    encoder = LabelEncoder()
    df['numSpec'] = encoder.fit_transform(df['Species'])

    # Select features and target variable
    X = df[['Weight', 'Height']]
    y = df['numSpec']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=66)

    # Create SVM model with RBF kernel and specified C and gamma
    clf = SVC(kernel='rbf', C=param_range[0], gamma=param_range[1])

    # Train the model
    clf.fit(X_train, y_train)

    # Predict the test set labels
    y_pred = clf.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    
    return (param_range[0], param_range[1], accuracy)

# Define the range of values for the C and gamma hyperparameters
C_range = np.arange(0.01, 100, 0.01)
gamma_range = np.arange(0.01, 100, 0.01)

# Create a list of tuples with all possible parameter combinations
param_list = [(C, gamma) for C in C_range for gamma in gamma_range]

# Use Pool to parallelize the search for best hyperparameters
pool = Pool(processes=4)
results = pool.map(find_best_params, param_list)
pool.close()

# Get the best C, gamma and accuracy values from the search
best_param = max(results, key=lambda x: x[2])

print(f"Best Accuracy: {best_param[2]}")
print(f"Best C: {best_param[0]}")
print(f"Best Gamma: {best_param[1]}")


# # Extract the values of C, gamma and accuracy from the results
# C_values = [result[0] for result in results]
# gamma_values = [result[1] for result in results]
# accuracy_values = [result[2] for result in results]

# # Create a scatter plot with C and gamma as the x and y axes, and accuracy as the color
# plt.scatter(C_values, gamma_values, c=accuracy_values, cmap='coolwarm')
# plt.colorbar()

# # Set the labels and title of the plot
# plt.xlabel('C')
# plt.ylabel('Gamma')
# plt.title('Accuracy vs C and Gamma')

# # Show the plot
# plt.show()