import numpy as np
import requests

URL = "http://localhost:8683"

inputs = 2
hiddens = 50
outputs = 1

def get_dataset(base_url):
    r = requests.get(base_url + "/dataset")
    dataset = r.json()

    X = np.array(dataset["train_x"])
    Y = np.array(dataset["train_y"])
    X_test = np.array(dataset["test_x"])

    return X, Y, X_test

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_prime(x):
    s = sigmoid(x)
    return s * (1 - s)


def mse(y, y_pred):
    return np.mean((y - y_pred) ** 2)


def mse_prime(y, y_pred):
    return (2 * (y_pred - y)) / y.size


w1 = np.random.uniform(-1, 1, size=(inputs, hiddens))
b1 = np.random.uniform(-1, 1, size=(1, hiddens))
w2 = np.random.uniform(-1, 1, size=(hiddens, outputs))
b2 = np.random.uniform(-1, 1, size=(1, outputs))


def feed_forward(w1, b1, w2, b2, x):
    z1 = np.dot(x, w1) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(a1, w2) + b2
    a2 = sigmoid(z2)

    return z1, a1, z2, a2


def backprop(w1, b1, w2, b2, z1, a1, z2, a2, x, y):
    d_err = mse_prime(y, a2)
    d_activ = sigmoid_prime(z2)
    delta_output = d_err * d_activ

    dw2 = np.dot(a1.T, delta_output)
    db2 = np.sum(delta_output, axis=0, keepdims=True)

    d_err_hidden = np.dot(delta_output, w2.T)
    d_activ_hidden = sigmoid_prime(z1)
    delta_hidden = d_err_hidden * d_activ_hidden

    dw1 = np.dot(x.T, delta_hidden)
    db1 = np.sum(delta_hidden, axis=0, keepdims=True)

    return dw1, db1, dw2, db2


def train(w1, b1, w2, b2, X, Y, epochs=1000, lr=0.01):
    for i in range(epochs):
        z1, a1, z2, a2 = feed_forward(w1, b1, w2, b2, X)
        dw1, db1, dw2, db2 = backprop(w1, b1, w2, b2, z1, a1, z2, a2, X, Y)

        w1 -= dw1 * lr
        w2 -= dw2 * lr

        b1 -= db1 * lr
        b2 -= db2 * lr

        if i % 100 == 0:
            print(f"Loss at iteration {i}: {mse(Y, a2)}")

    return w1, b1, w2, b2


def predict(w1, b1, w2, b2, X):
    _, _, _, out = feed_forward(w1, b1, w2, b2, X)
    return out


X, Y, X_test = get_dataset(URL)
Y = Y.reshape(-1, 1)

w1, b1, w2, b2 = train(w1, b1, w2, b2, X, Y, epochs=10000, lr=1)

out = ""
for x in X_test:
    predicted = round(predict(w1, b1, w2, b2, np.array([x]))[0][0])
    out += str(predicted)

print("Flag: " + "".join(chr(int(out[i * 8 : i * 8 + 8], 2)) for i in range(len(out) // 8)))
