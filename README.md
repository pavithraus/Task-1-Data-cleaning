# Task-1-Data-cleaning
# Resources used
Dataset-[Titanic.csv](https://www.kaggle.com/datasets/rushikeshlavate/titanic-datset)-

The dataset contains about passengers(age,sex,fae,class and some)data who were on board the Titanic.-

# objectives
1.Import the dataset and explore basic info (nu ls, data types).
2.Handle missing values using mean/median/imputation.
3.Convert categorical features into numerical using encoding.
4.Normalize/standardize the numerical features.
5.Visualize outliers using boxplots and remove them.
# Steps Performed:
1. Import & Explore Data
 > Loaded the dataset using pandas
 > Inspected shape, data types, and summary statistics
2. Handle Missing Values
 >Filled missing values in:
  Age using median
  Embarked using mode
 >Dropped the Cabin column due to excessive missing data
3. Encode Categorical Variables
 >Converted Sex to binary (0 = male, 1 = female)
 >One-hot encoded Embarked (used drop_first=True to avoid multicollinearity)
4. Normalize Numerical Features
 >Standardized Age and Fare using StandardScaler from Scikit-learn
5. Outlier Detection & Removal
 >Visualized outliers using boxplots
 >Removed outliers from Age and Fare using the IQR method
# At final
 Our cleaned dataset is ready for further process:
   > EDA
   > Ml model training 
 
