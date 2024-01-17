from tensorflow.keras.models import load_model
import cv2
import tensorflow as tf
import numpy as np


from tensorflow.keras.models import load_model
model=load_model('model (1).keras')


# def calculate(imgpath):
#   img = cv2.imread(imgpath)
#   resize = tf.image.resize(img,(256,256))
#   yhat = model.predict(np.expand_dims(resize/255,0))
#   return not round(yhat[0][0]) > 0.5 


# img = cv2.imread('Covid (1).png')
# resize = tf.image.resize(img,(256,256))
# yhat = model.predict(np.expand_dims(resize/255,0))
# print(f"Predicted class is {'things' if round(yhat[0][0]) > 0.5 else 'human'}")
# print(yhat[0][0])



