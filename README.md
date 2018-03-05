# Federal-STEM-funding
**Machine Learning on Federal STEM Education Funding Data to predict whether or not the funding will increase in next year.**

Following steps are performed in the jupyter notebook **Funding Prediction.ipynb**:
1.  Cleaning of data as it contained missing values and spurious values.
2.  Encoding of categorical variables and merging of subcolumns to remove sparcity and dimensionality of data.
3.  Creating feature '% Growth' which is percentage growth in funding between 2008 and 2009. Also creation of Target variable       based on the values of '% Growth'
4.  Plotting of univariate distributions of features.
5.  Calculation of mutual_info_score between features and target variable.
6.  Splitting data in 70:30 ratio for the purpose of training and testing. Further splitting train data for the purpose of         validation.
7.  Training XGBoost model on train data and hyperparameter tuning of parameters.
8.  Evaluating the performance of model on test data.

**Tests.py**
Tests with expected output and input for the functions used in the above notebook
