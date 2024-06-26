# -*- coding: utf-8 -*-
"""hand wrt reg.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B1uSqoX0ukd2yIL3Zaak8X7qAQ7dWYXy
"""

#libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


mnist = fetch_openml('mnist_784')

mnist.data.shape

#def function
def showimage(dframe, index):
  some_digit = dframe.to_numpy()[index]
  some_digit_image = some_digit.reshape(28,28)

  plt.imshow(some_digit_image, cmap= "binary")
  plt.axis("off")
  plt.show()

#sample use:
showimage(mnist.data, 0)

#train and test data
train_img, test_img, train_lbl, test_lbl = train_test_split( mnist.data, mnist.target, test_size = 1/7.0, random_state= 0 )

type(train_img)

test_img_copy = test_img.copy()

showimage(test_img_copy, 2)

scaler = StandardScaler()

scaler.fit(train_img)

train_img = scaler.transform(train_img)
test_img = scaler.transform(test_img)

pca_model = PCA(.95)

pca_model.fit(train_img)

print(pca_model.n_components_)

train_img = pca_model.transform(train_img)
test_img = pca_model.transform(test_img)

lr = LogisticRegression(solver= 'lbfgs' , max_iter = 10000)

lr.fit(train_img, train_lbl)

lr.predict(test_img[0].reshape(1,-1))

showimage(test_img_copy, 0)

lr.predict(test_img[1].reshape(1,-1))

showimage(test_img_copy, 1)

showimage(test_img_copy, 42)

lr.predict(test_img[42].reshape(1,-1))

showimage(test_img_copy, 57)

lr.predict(test_img[57].reshape(1,-1))

lr.score(test_img, test_lbl)