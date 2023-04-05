from sklearn import datasets
from sklearn import svm

# Load iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# print(X) # data 1D axies 

# Create a SVM Classifier
clf = svm.SVC(kernel='linear', C=1, gamma='auto')

# Train the model using the whole dataset
clf.fit(X, y)

# Predict the class for a new input
x_new = [[5.0, 9.6, 1.3, 0.25]] # x ที่ต้องการทดสอบ
y_new = clf.predict(x_new) # คำนวณค่า y ที่คาดการณ์ได้จากโมเดล SVM
print("Predicted class for x_new:", y_new)
