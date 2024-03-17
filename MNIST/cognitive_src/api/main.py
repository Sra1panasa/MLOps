from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing import image
import numpy as np
import uvicorn
import io
#from cognitive_src.utils import logger ---- getting import issue need to check

app = FastAPI()

# Load base model
base_model = MobileNetV2(weights='imagenet', include_top=False)

# Add a global spatial average pooling layer
x = base_model.output
x = GlobalAveragePooling2D()(x)
# Add a fully-connected layer
x = Dense(1024, activation='relu')(x)
# And a logistic layer -- we have 10 classes
predictions = Dense(10, activation='softmax')(x)

# This is the model we will use
model = Model(inputs=base_model.input, outputs=predictions)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = image.load_img(io.BytesIO(contents), target_size=(224, 224))  # Adjust target size to 224x224 for MobileNetV2
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_array_expanded_dims)
    
    prediction = model.predict(img_preprocessed)
    predicted_class = np.argmax(prediction, axis=1)[0]
    predicted_label = class_names[predicted_class]
    return {"filename": file.filename, "predicted_class": predicted_label}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
