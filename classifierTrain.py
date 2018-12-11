#Training module
import pickle
import random

import numpy as np
from sklearn.externals import joblib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

from vectorize import getSentencesIbc, vectorizeSentences

V = vectorizeSentences() #An array of vectorized sentences from the IBC
y = np.asarray(getSentencesIbc()[1]) #Labels of the corresponding sentences

X_train, X_test, y_train, y_test = train_test_split(V, y, test_size = 0.25) #25% of data set aside for testing

mlp = MLPClassifier(hidden_layer_sizes=(500, 20, 20, 20), max_iter=1000, batch_size=32, \
                    warm_start=True, early_stopping= True)  #Classifier object

mlp.fit(X_train, y_train)  

predictions = mlp.predict(X_test)


if __name__ == '__main__':
    #Results of classifier predictions
    print(confusion_matrix(y_test,predictions))  
    print(classification_report(y_test,predictions))  
    # Store the classifier for further use by uncommenting the line below
    # joblib.dump(mlp, 'classifier.joblib') 
