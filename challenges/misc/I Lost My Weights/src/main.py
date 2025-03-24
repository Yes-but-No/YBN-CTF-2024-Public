from flask import Flask, Response
from sklearn import datasets

import numpy as np
import json

FLAG = "YBN24{un1v3r5al_4ppr0x1m4t10n_th30r3m}"
BINARY = "".join(f"{ord(i):08b}" for i in FLAG)

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

app = Flask(__name__)

@app.get('/')
def index():
    return "Obtain the dataset from the /dataset endpoint!"

@app.get('/dataset')
def gen_dataset():
    funcs = [datasets.make_circles, datasets.make_moons]

    f = np.random.choice(funcs)
    X, Y = f(n_samples=1000, noise=0.2)
    X_test = []

    X_tests, Y_tests = f(n_samples=2000)
    i = 101

    for d in BINARY:
        d = int(d)
        while i < 2000:
            x_test, y_test = X_tests[i], Y_tests[i]
            if y_test != d:
                i += 1
                continue
            X_test.append(x_test)
            break
        if i == 2000:
            return "You won the lottery! Here's the flag: " + FLAG

    data = {"train_x": X.tolist(), "train_y": Y.tolist(), "test_x": X_test}
    return Response(json.dumps(data, cls=NumpyEncoder), mimetype="application/json")

app.run(host='0.0.0.0', port=8683)