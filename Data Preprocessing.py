import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("/Titanic.csv")  # or the exact filename you downloaded

# Show basic structure
print(data.shape)
print(data.columns)
print(data.info())
print(data.describe())

# Check missing values
print(data.isnull().sum())

# Fill missing Age with median
data['Age'] = data['Age'].fillna(data['Age'].median())

# Fill missing Embarked with mode
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

# Drop Cabin column (too many missing values)
data = data.drop(columns=['Cabin'])

# View unique values in categorical columns
print(data['Sex'].unique())        # ['male', 'female']
print(data['Embarked'].unique())   # ['S', 'C', 'Q']

# Convert 'Sex' column to 0 and 1
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# Use one-hot encoding for 'Embarked'
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Select numerical columns to scale
cols_to_scale = ['Age', 'Fare']

data[cols_to_scale] = scaler.fit_transform(data[cols_to_scale])

# Boxplots to detect outliers
plt.figure(figsize=(10, 5))
sns.boxplot(x=data['Fare'])
plt.title("Boxplot of Fare")
plt.show()

sns.boxplot(x=data['Age'])
plt.title("Boxplot of Age")
plt.show()

# Function to remove outliers using IQR
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

# Apply to Age and Fare
data = remove_outliers(data, 'Age')
data = remove_outliers(data, 'Fare')

#final checking
print(data.info())
print(data.head())
