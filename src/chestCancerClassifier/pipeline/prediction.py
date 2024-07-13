import os

import numpy as np
from tensorflow.keras.models import load_model  # type: ignore
from tensorflow.keras.preprocessing import image  # type: ignore


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
<<<<<<< HEAD
        # model = load_model(os.path.join("artifacts", "training", "model.h5"))
        model = load_model(os.path.join("model", "model.h5"))
=======
        model = load_model(os.path.join("artifacts", "training", "model.h5"))
        # model = load_model(os.path.join("model", "model.h5"))
>>>>>>> d2259b80d8a83ef6c1727b9ecb2ec0ce065b5d2a

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Normal'
            return [{"image": prediction}]
        else:
            prediction = 'Adenocarcinoma Cancer'
            return [{"image": prediction}]
