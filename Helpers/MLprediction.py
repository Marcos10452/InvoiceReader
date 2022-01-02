


import numpy as np
import pandas as pd
import keras

  ###________________ Getting invoice prediction_____________________
def prediction_func(tempdf):
    #Create array with 'x0','top','Providercode','page_number'&'text' columns 
    testarray=np.array(tempdf[['x0','top','x1','bottom','Providercode','page_number','text']].values)

    #again, orderdering
    sorter = lambda x: (x[5], x[1], x[0])
    testarray= sorted(testarray, key=sorter)
    
  
    #I had to update keras because colab has a newest version.
    #from tensorflow.keras.models import load_model

    new_model = keras.models.load_model('./Model/path_to_my_model.hdf5')
    keras.__version__

    #_________Standarize input_____________________
    standar=[573.504, 816.416, 584.276, 823.566, 11,10]#check everytime is trained again.


    Typeclass=[]
    #PREDICTING class type using data from invoice and trained parameters
    
    for count,forarray in enumerate(testarray):
      testinvoice=new_model.predict(np.array(list(forarray[:6]/standar)).reshape(1,6)).argmax(axis=1)[0]  
      Typeclass.append(testinvoice)
    return Typeclass