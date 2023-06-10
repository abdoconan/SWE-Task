import pandas as pd 
from matplotlib import pyplot as plt
from sklearn  import model_selection as ms
from sklearn import metrics as mtc
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
dataset = pd.read_csv("data.csv", names= ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'])
print("dataset shape: ", dataset.shape, "\n", "Peek of the data: ", dataset.head(), "\n"
    ,"description of the dataset: ", dataset.describe(), "\n", "classes size: ", dataset.groupby("class").size())
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
dataset.hist()
pd.plotting.scatter_matrix(dataset)
plt.show()
X, y = dataset.values[:,0:4], dataset.values[:,4]
X_train, X_validation, Y_train, Y_validation = ms.train_test_split(X, y, 
test_size=0.20, random_state=1)
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
print(mtc.accuracy_score(Y_validation, predictions), "\n", mtc.confusion_matrix(Y_validation, predictions),
    "\n", mtc.classification_report(Y_validation, predictions))
models, results, names = [], [], []
models.extend([('LR', LogisticRegression(solver='liblinear', multi_class='ovr')), ('LDA', LinearDiscriminantAnalysis()),
    ('KNN', KNeighborsClassifier()), ('CART', DecisionTreeClassifier()), ('NB', GaussianNB()), ('SVM', SVC(gamma='auto'))])
for name, model in models:
    kfold = ms.StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = ms.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
plt.boxplot(results, labels=names)
plt.title('Algorithm Comparison')
plt.show()