# Federal-STEM-funding
Machine Learning on Federal STEM Education Funding Data to Predict whether or not the funding will increase in next year.
Following steps are performed in the jupyter notebook attached:
i.    Cleaning of data as it contained missing values and spurious values.
ii.   Encoding of categorical variables and merging of subcolumns to remove sparcity and dimensionality of data.
iii.  Creating feature '% Growth' which is percentage growth in funding between 2008 and 2009. Also creation of Target variable       based on the values of '% Growth'
iv.   Plotting of univariate distributions of features.
 v.   Calculation of mutual_info_score between features and target variable.
vi.   Splitting data in 70:30 ratio for the purpose of training and testing. Further splitting train data for the purpose of         validation.
vii.  Training XGBoost model on train data and hyperparameter tuning of parameters.
viii. Evaluating the performance of model on test data.
