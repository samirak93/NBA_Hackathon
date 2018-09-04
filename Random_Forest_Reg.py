#Used Random Forest Regressor
#Accuracy 67%
#MAPE= ~4400 viewers

## Samira Kumar NBA Hackathon 2018 - Business Analytics
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler



#Train and test model with output.csv file
df=pd.read_csv('output.csv')

data=pd.DataFrame(df)
data_set=data.fillna(0)

features=data_set.iloc[:,3:-1]

dataset_X=np.array(features)

onehotencoder = OneHotEncoder(categorical_features = [0,1,10,12,13,18])
X = onehotencoder.fit_transform(features).toarray()
X = X[:, 1:]

views_target=data_set['Rounded Viewers'].values
feature_list = list(features.columns)


bball=RandomForestRegressor(random_state=42,n_estimators=1500,max_features=None,max_depth=None)

X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, views_target, test_size=0, random_state=42)

sc = StandardScaler()
X_trainset = sc.fit_transform(X_trainset)


#Test with test_data.csv
tdf=pd.read_csv('test_data.csv')

test_data=pd.DataFrame(tdf)
test_dataset=test_data.fillna(0)


feature_difference = set(data) - set(test_dataset)

feature_difference_df = pd.DataFrame(data=np.zeros((test_dataset.shape[0], len(feature_difference))),
                                     columns=list(feature_difference))

test_dummy = test_dataset.join(feature_difference_df)

test_features=np.array(test_dummy.iloc[:,3:-1])


test_onehotencoder = OneHotEncoder(categorical_features = [0,1,10,12,13,18])
X_test = onehotencoder.fit_transform(test_features).toarray()
X_test = X_test[:, 1:]

X_testset = sc.transform(X_test)

views_target=data_set['Rounded Viewers'].values
feature_list = list(features.columns)

bball.fit(X_trainset,y_trainset)

output=[]
predForest=bball.predict(X_testset)

output=predForest

test_set_new=pd.DataFrame(pd.read_csv('test_set.csv'))

test_set_new['Total_Viewers']=np.round(output,0)

print test_set_new['Total_Viewers']

test_set_new.to_csv('test_set.csv')


