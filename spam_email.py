# Importing necessary libraries
import pandas as pd                          # pandas library for working with data
from sklearn.model_selection import train_test_split  # function for splitting data into training and test sets
from sklearn.feature_extraction.text import CountVectorizer  # tool for converting text to numbers
from sklearn import svm                       # Support Vector Machine algorithm for classification

# Reading the data from a CSV file
spam = pd.read_csv('C:\\Users\\danielkalu\\Downloads\\spam.csv')

# Separating the email text (features) and labels (whether spam or not)
z = spam['EmailText']
y = spam["Label"]

# Splitting the data into training and test sets
z_train, z_test, y_train, y_test = train_test_split(z, y, test_size=0.2)

# Creating a CountVectorizer object to convert email text into numbers
cv = CountVectorizer()
features = cv.fit_transform(z_train)

# Creating a Support Vector Machine (SVM) model
model = svm.SVC()

# Training the SVM model with the training data and labels
model.fit(features, y_train)

# Converting the test email text into numbers using the same CountVectorizer object
features_test = cv.transform(z_test)

# Testing the SVM model's accuracy on the test set
accuracy = model.score(features_test, y_test)
print("Model Accuracy:", accuracy)

