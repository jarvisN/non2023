import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

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

# Create SVM model with linear kernel and C=1
clf = SVC(kernel='linear', C=1)

# Train the model
clf.fit(X_train, y_train)

# Predict the test set labels
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
