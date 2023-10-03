import preprocessing
from tensorflow.keras.models import load_model
import numpy as np
def prediction(essay):


    features = preprocessing.extract_features(essay)

    model = load_model('C:/Users/LENOVO/Desktop/aeg/proj/grader/my_model.h5')
    #print(features.loc[0,'char_count_before'] )

    X_test = np.array(features)

    testDataVecs = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

    testDataVecs = testDataVecs.astype(np.float)

    y_pred = model.predict(testDataVecs)

    y_pred = np.around(y_pred)

    y_pred = np.array(y_pred, dtype='int')

    y_pred = y_pred[:, :, 0]
    
    return y_pred[0][0]
