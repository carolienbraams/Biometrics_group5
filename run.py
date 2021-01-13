import cv2
import numpy as np
from keras.models import Model, load_model
from keras.layers import Input, Conv2D, Dense, Dropout, GlobalAveragePooling2D, MaxPooling2D, Lambda
import keras.backend as K

import sys
print(sys.version)

# paths to images
pathA = 'C:/Users/stijn/Documents/Studie/delft/20-21--2/IntroBio/Final/Biometrics_group5/frgc32x32/02463d170.png'
pathB = 'C:/Users/stijn/Documents/Studie/delft/20-21--2/IntroBio/Final/Biometrics_group5/frgc32x32/02463d184.png'

pathWeights = 'C:/Users/stijn/Documents/Studie/delft/20-21--2/IntroBio/Final/Biometrics_group5/output/siamese_model/saved_weights.h5'
pathModel = 'C:/Users/stijn/Documents/Studie/delft/20-21--2/IntroBio/Final/Biometrics_group5/output/siamese_model/saved_model'

IMG_SHAPE = (32, 32, 1)
#
#
# def build_siamese_model(inputShape, embeddingDim=48):
#     inputs = Input(inputShape)
#     x = Conv2D(64, (2, 2), padding="same", activation="relu")(inputs)
#     x = MaxPooling2D(pool_size=(2, 2))(x)
#     x = Dropout(0.3)(x)
#
#     x = Conv2D(64, (2, 2), padding="same", activation="relu")(x)
#     x = MaxPooling2D(pool_size=2)(x)
#     x = Dropout(0.3)(x)
#
#     pooledOutput = GlobalAveragePooling2D()(x)
#     outputs = Dense(embeddingDim)(pooledOutput)
#
#     model = Model(inputs, outputs)
#
#     return model
#
#
# def euclidean_distance(vectors):
#     # unpack the vectors into separate lists
#     (featsA, featsB) = vectors
#     # compute the sum of squared distances between the vectors
#     sumSquared = K.sum(K.square(featsA - featsB), axis=1,
#                        keepdims=True)
#     # return the euclidean distance between the vectors
#     return K.sqrt(K.maximum(sumSquared, K.epsilon()))
#
#
imageA = cv2.imread(pathA, 0)
imageB = cv2.imread(pathB, 0)

imageA = np.expand_dims(imageA, axis=-1)
imageB = np.expand_dims(imageB, axis=-1)

imageA = np.expand_dims(imageA, axis=0)
imageB = np.expand_dims(imageB, axis=0)

imageA = imageA / 255.0
imageB = imageB / 255.0

imgA = Input(shape=IMG_SHAPE)
imgB = Input(shape=IMG_SHAPE)
# featureExtractor = build_siamese_model(IMG_SHAPE)
# featsA = featureExtractor(imgA)
# featsB = featureExtractor(imgB)
#
# distance = Lambda(euclidean_distance)([featsA, featsB])
# outputs = Dense(1, activation="sigmoid")(distance)
# model = Model(inputs=[imgA, imgB], outputs=outputs)
#
# model.load_weights(pathWeights)
model = load_model(pathModel)
preds = model.predict([imageA, imageB])

print(preds)
