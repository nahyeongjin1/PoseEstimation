import cv2, numpy as np
import pickle, gzip, os
from urllib.request import urlretrieve
import matplotlib.pyplot as plt

def load_mnist(filename):
    if not os.path.exists(filename):
        print("Downloading")
        link = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
        urlretrieve(link, filename)
    with gzip.open(filename, 'rb') as f:
        return pickle.load(f, encoding='unicode-escape')

def graph_image(data, lable, title, nsample):
    plt.figure(num=title, figsize=(10,10))
    rand_idx = np.random.choice(range(data.shape[0]), nsample)
    for i, id in enumerate(rand_idx):
        img = data[id].reshape(28, 28)
        plt.subplot(6, 4, i+1), plt.axis('off'), plt.imshow(img, cmap='gray')
        plt.title("%s: %d" % (title, lable[id]))
        plt.tight_layout()

train_set, valid_set, test_set = load_mnist("mnist.pkl.gz")

## MNIST 로드 데이터 크기 확인
print("train_set=", train_set[0].shape)
print("valid_set=", valid_set[0].shape)
print("test_set=", test_set[0].shape)

print("training...")
print(train_set)
knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE, train_label)

nsample = 100
print("%d 개 predicting..." % nsample)
a, resp, b, c = knn.findNearest(test_data[:nsample], k=5)
accur = sum(resp.flatten() == test_label[:nsample])

print('정확도=', accur / nsample * 100, '%')
graph_image(train_data, train_label, 'label', 24)
graph_image(test_data[:nsample], resp, 'predict', 24)
plt.show()