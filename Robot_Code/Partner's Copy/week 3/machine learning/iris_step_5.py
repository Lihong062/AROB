# STUDENTS: copy-paste this whole file into the bottom of iris_machine_learning.


# Split out validation dataset
values = dataset.values
X = values[:, 0:4]
Y = values[:, 4]
validation_portion = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation =
        model_selection.train_test_split(
    X, Y, test_size=validation_portion, random_state=seed)

# Test options and evaluation metric
scoring = 'accuracy'

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, 
        Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# STUDENTS: write your code for step 6 below this line