#Make sure to "pip install scikit-learn" and "pip install pandas"

import pandas 
import warning
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier

warnings.filterwarnings('ignore')

#download the diabetes.csv file and give its path to the url variable
url = ("/diabetes.csv") 
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names,header=0)
array = dataframe.values 
X = array[:,0:8] 
Y = array[:,8] 
seed = 7 
num_trees = 30 
#kfold makes trees with split number.
#kfold = model_selection.KFold(n_splits=10, algorithm='SAMME', random_state=seed)
#n_estimators : This is the number of trees you want to build before predictions.
#Higher number of trees give you better voting optionsand perfomance performance 
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)
#cross_val_score method is used to calculate the accuracy of model sliced into x, y
#cross validator cv is optional cv=kfold
results = model_selection.cross_val_score(model, X, Y, cv=5)
print(results.mean()) 
