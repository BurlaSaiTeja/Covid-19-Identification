from django.shortcuts import render
import requests
import os
import numpy as np
from keras.preprocessing import image


def home(request):
    data = requests.get("https://api.rootnet.in/covid19-in/stats").json().get("data").get("summary")
    positive = data.get("confirmedCasesIndian")
    deaths = data.get("deaths")
    discharged = data.get("discharged")
    return render(request, "index.html", {
        "deaths": deaths,
        "positive": positive,
        "discharged": discharged
    })


def make_prediction(request):
    positive = 0
    negative = 0
    saved_model = load_model("Covid19Net.h5")
    for dirname, _, filenames in os.walk('/content/drive/My Drive/data-p5/Source_1/Test/'):
        for filename in filenames:
            img = image.load_img(os.path.join(dirname, filename), target_size=(384, 384))
            img = np.asarray(img)
            img = np.expand_dims(img, axis=0)
            output = saved_model.predict(img)
            if output[0][0] > output[0][1]:
                print("Positive")
                positive += 1
            else:
                print('Negative')
                negative += 1
    print("Total Positive Predicted ->", positive)
    print("Total Negative Predicted ->", negative)
