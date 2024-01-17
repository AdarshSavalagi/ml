import shutil
import gradio as gr
from tensorflow.keras.models import load_model
import tensorflow as tf
import cv2
import numpy as np
import os

def calculator(imgpath):
        model=load_model('model.keras')
        img = cv2.imread(imgpath)
        resize = tf.image.resize(img,(256,256))
        yhat = model.predict(np.expand_dims(resize/255,0))
        return not round(yhat[0][0]) > 0.5 


def classify_image(img):
 
    path = "ctscan/" + os.path.basename(img) 
    shutil.copyfile(img.name, path)
    ans = calculator(path)
    print(ans)
    return 'Covid' if ans else 'Non-covid'
    # class_name, probability = predictor('ctscan', 'class.csv', 'model.keras')


    # if class_name is not None and probability is not None:
    #     return class_name
    # else:
    #     return "Not classified"

# Create Gradio interface
    

# pip install httpx==0.25.0
image = gr.Image()
label = gr.Label()

iface = gr.Interface(
    fn=classify_image,
    inputs='file',
    outputs="text",
    title='COVID-19 Detection'
)

iface.launch(share=True)


