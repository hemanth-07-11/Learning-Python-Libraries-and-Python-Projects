# REFERENCE: https://medium.com/@madanflies/linear-regression-on-carprice-dataset-or-encoding-a-categorical-dataset-in-linear-regression-7378f207e5c1

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import scale
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import copy

X=pd.read_csv('categorial_lin_reg.csv')
Y=X.price #Target Variable 
X=X.drop(['price'],axis=1) 

print('Null values in X',X.isnull().sum())
print('Null values in Y',Y.isnull().sum())
print('Shape is',X.shape)
print('Head is',X.head())
print('Describing dataframe ',X.describe(include='all'))

plt.rcParams["figure.figsize"] = [16,9]
sns.set(style="darkgrid")
sns.pairplot(data=X)

scatter_matrix(X, alpha=0.5, figsize=(30,30), diagonal='kde',grid='true')
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(Y, bins=30)
plt.show()
Y.plot()

correlation_matrix = X.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)

cleanup_nums = {"doornumber":     {"four": 4, "two": 2},
                "cylindernumber": {"four": 4, "six": 6, "five": 5, "eight": 8,
                                  "two": 2, "twelve": 12, "three":3 }}
X.replace(cleanup_nums, inplace=True)

Cat=X.select_dtypes(include=['object']).copy(deep='False')

Cat=Cat.iloc[:, :].apply(pd.Series)
Name=Cat.CarName.copy()

Temp=[]
Temp=Name.str.split(pat=" ",expand=True)
Temp=Temp[0]
X.CarName=Temp
Cat.CarName=Temp

cleanup_nums = {"CarName":     { "maxda": "mazda" , "porcshce": "porsche" , "Nissan":"nissan" , "vokswagen":"volkswagen", "toyouta" : "toyota","vw" : "volkswagen"} }
X.replace(cleanup_nums, inplace=True)

L=X.copy(deep='False')
L=pd.get_dummies(L, columns=Cat.columns)

Xs = scale(L)

X_train, X_test, Y_train, Y_test = train_test_split(Xs, Y, test_size=0.3, random_state=42)

Coef=LinearRegression()

Coef.fit(X_train, Y_train)
Y_pred = Coef.predict(X_test)

print('Coefficients: \n', Coef.coef_)
print('Variance score: %.2f' % r2_score(Y_test, Y_pred))









