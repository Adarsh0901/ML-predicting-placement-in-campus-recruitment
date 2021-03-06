# -*- coding: utf-8 -*-
"""Adarsh_Shukla_project_final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18UyCb5RoeObSrq9c1b17TP8VGsGCJq7s

# **1] Importing necessary Libraries**
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

"""# **2] Reading CSV file and printing 5 elements**"""

df=pd.read_csv("/content/11-4-Dataset-Predicting Placement in Campus Recruitment.csv")
df.head()

#print statistical information

df.describe()

df.shape

"""# **2] Preprocessing the data**"""

df.isnull().sum()     #checking for null values

#Filling null values with median

df["salary"] = df["salary"].fillna(df["salary"].median())

df.isnull().sum()

#Removing unneccesary column

df=df.drop(["sl_no"],axis=1)         
df.columns

#converting into numericals

df.loc[df["status"] == "Not Placed", "status"] = 0      
df.loc[df["status"] == "Placed", "status"] = 1

#converting into numerical

df.loc[df["gender"] == "M", "gender"] = 0           
df.loc[df["gender"] == "F", "gender"] = 1

# separate input(X) and output(y) columns

X=df.drop("status", axis=1)       
y=df["status"]

#convert categorial data into numerical

from sklearn.preprocessing import LabelEncoder
Encoder_X = LabelEncoder()           
for col in X.columns:
    X[col] = Encoder_X.fit_transform(X[col])
Encoder_y=LabelEncoder()
y = Encoder_y.fit_transform(y)

X

#storing new data into new CSV file

X.to_csv("newsample.csv")
y

"""# **3] Performing EDA on Dataset**"""

#Using countplot to plot no of student placed and not placed
#0-Not placed and 1-Placed

sns.countplot(x='status',data=df)

#using boxplot on no of student placed and not placed based on MBA percentage
#0-Not placed and 1-Placed

sns.boxplot(x='status', y='mba_p', data=df)

#using boxplot on no of student placed and not placed based on Degree percentage
#0-Not placed and 1-Placed

sns.boxplot(x='status', y='degree_p',data=df)

#using boxplot on no of student placed and not placed based on Entrance test percentage
#0-Not placed and 1-Placed

sns.boxplot(x='status', y='etest_p',data=df)

sns.violinplot(x="status", y="mba_p", data=df, size=8)

"""# **4] Split Data into Training and Testing part**"""

#spliting Data into training and testing part
#80%-training and 20%-testing 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=144)

"""# **5] Apply standard scaling to standardize the data**"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""#**6] Applying all algorithms**"""

# 1. applying linear Regression algorithm to our model

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
my_model=LinearRegression()
result=my_model.fit(X_train, y_train)

predictions=my_model.predict(X_test)
predictions

r2_score(y_test,predictions)

new_pred=list(result6.predict([[0,46,1,93,1,1,14,2,0,9,1,64,19]]))
new_pred

# 2. applying logistic Regression algorithm to our model

from sklearn.linear_model import LogisticRegression
my_model2=LogisticRegression()
result2=my_model2.fit(X_train, y_train)

predictions2 = result2.predict(X_test)
predictions2

from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions2)

new_pred2=list(result6.predict([[0,46,1,93,1,1,14,2,0,9,1,64,19]]))
new_pred2

from sklearn.metrics import confusion_matrix
confusion_mat = confusion_matrix(y_test, predictions2)
confusion_df = pd.DataFrame(confusion_mat, index=['Actual neg','Actual pos'], columns=['Predicted neg','Predicted pos'])
confusion_df

Color_conf_matrix = sns.heatmap(confusion_df, cmap='coolwarm',annot = True)

from sklearn import metrics
print('\n**Classification Report:\n',metrics.classification_report(y_test,predictions2))

# 3. applying Decision Tree algorithm to our model
# Training Model

from sklearn.tree import DecisionTreeClassifier
my_model3 = DecisionTreeClassifier(random_state=0)
result3 = my_model3.fit(X_train,y_train)

# Testing Model

predictions3 = result3.predict(X_test)
predictions3

accuracy_score(y_test,predictions3)

new_pred3=list(result6.predict([[0,46,1,93,1,1,14,2,0,9,1,64,19]]))
new_pred3

confusion_mat = confusion_matrix(y_test, predictions3)
confusion_df = pd.DataFrame(confusion_mat, index=['Actual neg','Actual pos'], columns=['Predicted neg','Predicted pos'])
confusion_df

Color_conf_matrix = sns.heatmap(confusion_df, cmap='coolwarm',annot = True)

from sklearn import metrics
print('\n**Classification Report:\n',metrics.classification_report(y_test,predictions3))

# 4. applying Random Forest algorithm to our model
# Training model

from sklearn.ensemble import RandomForestClassifier
my_model4 = RandomForestClassifier(n_estimators = 50, criterion = 'entropy', random_state = 42)
result4=my_model4.fit(X_train, y_train)

# Testing model

predictions4 = result4.predict(X_test)
predictions4

from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, predictions4))

new_pred4=list(result6.predict([[0,46,1,93,1,1,14,2,0,9,1,64,19]]))
new_pred4

confusion_mat = confusion_matrix(y_test, predictions4)
confusion_df = pd.DataFrame(confusion_mat, index=['Actual neg','Actual pos'], columns=['Predicted neg','Predicted pos'])
confusion_df

Color_conf_matrix = sns.heatmap(confusion_df, cmap='coolwarm',annot = True)

from sklearn import metrics
print('\n**Classification Report:\n',metrics.classification_report(y_test,predictions4))

# 5. applying SVM algorithm to our model
# Training model

from sklearn.svm import SVC
my_model5 = SVC(kernel = 'rbf', random_state = 0)
result5 = my_model5.fit(X_train, y_train)

# Testing model

predictions5= my_model5.predict(X_test)
predictions5

print("Accuracy:",metrics.accuracy_score(y_test, predictions5))

new_pred5=list(result6.predict([[0,46,1,93,1,1,14,2,0,9,1,64,19]]))
new_pred5

confusion_mat = confusion_matrix(y_test, predictions5)
confusion_df = pd.DataFrame(confusion_mat, index=['Actual neg','Actual pos'], columns=['Predicted neg','Predicted pos'])
confusion_df

Color_conf_matrix = sns.heatmap(confusion_df, cmap='coolwarm',annot = True)

from sklearn import metrics
print('\n**Classification Report:\n',metrics.classification_report(y_test,predictions5))

# 6. applying KNN algorithm to our model
# Training Model

from sklearn.neighbors import KNeighborsClassifier
my_model6 = KNeighborsClassifier(n_neighbors = 3)
result6 = my_model6.fit(X_train,y_train)

# Testing model

predictions6= my_model6.predict(X_test)
predictions6

new_pred6=list(result6.predict([[0,46,1,93,1,1,14,2,0,9,1,64,19]]))
new_pred6

confusion_mat = confusion_matrix(y_test, predictions6)
confusion_df = pd.DataFrame(confusion_mat, index=['Actual neg','Actual pos'], columns=['Predicted neg','Predicted pos'])
confusion_df

Color_conf_matrix = sns.heatmap(confusion_df, cmap='coolwarm',annot = True)

from sklearn import metrics
print('\n**Classification Report:\n',metrics.classification_report(y_test,predictions6))

print('With KNN (K=3) accuracy is: ', result.score(X_test,y_test))

# df_scaled is our new data frame which will contain Normally
# distributed data.

df_scaled = sc.fit_transform(X_train,y_train)

# 7. applying K-Means algorithm to our model

from sklearn.cluster import KMeans
ssq =[]
for K in range(1,11):
  my_model7 = KMeans(n_clusters=K, random_state=123)
  result7 = my_model7.fit(df_scaled)
  ssq.append(my_model7.inertia_)

# Now generate plot of ssq with the help of matplotlib.

plt.plot(range(1,11), ssq, marker='o')
plt.xlabel("Number of clusters")
plt.ylabel("Within-cluster SSQ")
plt.title("SSQ Plot")
plt.show()

# Training Model

my_model7 = KMeans(n_clusters=3, random_state=123)
result7= my_model7.fit(df_scaled)

# Testing model

predictions7 = result7.predict(df_scaled)
predictions7

plt.scatter(df_scaled[predictions7==0,0], df_scaled[predictions7==0,1], s=50, c='lightgreen',marker='s', edgecolors='black', label='cluster 1')
plt.scatter(df_scaled[predictions7==1,0], df_scaled[predictions7==1,1], s=50, c='orange',marker='o', edgecolors='black', label='cluster 2')
plt.scatter(df_scaled[predictions7==2,0], df_scaled[predictions7==2,1], s=50, c='lightblue',marker='v', edgecolors='black', label='cluster 3')
plt.scatter(df_scaled[predictions7==3,0],df_scaled[predictions7==3,1], s=50, c='yellow',marker='s',edgecolors='black',label='cluster 4')
plt.scatter(result7.cluster_centers_[:,0],
result.cluster_centers_[:,1], s=250, c='red',marker='*', edgecolors='black', label='centroids')

plt.legend(scatterpoints=1)
plt.xlabel("Placed")
plt.ylabel("Not Placed")
plt.title("Clustering Output")
plt.show()

"""## **CONCLUSION**
  By applying all Algorithms to our model , accuracy of each model are as follows:
  1. By Linear regression:0.5211346131181207
  2. By Logistic regression:0.8837209302325582
  3. By Decision Tree:0.9069767441860465
  4. **By Random forest:0.9302325581395349**
  5. By SVM algorithm:0.8837209302325582
  6.By KNN algorithm:0.5211346131181207

      so, we can conclude that **Random forest algorithm** are best Model
"""