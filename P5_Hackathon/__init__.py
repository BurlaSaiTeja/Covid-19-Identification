import os

import numpy as np
from keras.models import load_model

from P5_Hackathon.settings import BASE_DIR

model_file = load_model(os.path.join(BASE_DIR, "P5_Hackathon/Main_one.h5"))
outputs = [model_file.layers[i].output for i in np.arange(len(model_file.layers))]
