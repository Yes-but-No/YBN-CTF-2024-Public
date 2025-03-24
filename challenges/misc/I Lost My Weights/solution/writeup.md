# I Lost My Weights

This is an AI challenge where participants are required to train their
own binary classifier to fit to a given train set. After their network
generalises the underlying function, they can run it on a test
set.

The generalised function can be defined as follows. Given a 2D coordinate
`x` and `y` , the function, `f`, should give an output `z` where
$f(x, y) \rightarrow z \space \forall z \in {0, 1}$

As shown in the equation above, the function / classifier returns a
`1` or `0`. If the classifier generalised correctly, the output
of the test set would print the flag in binary.

The full solve script can be found in `solve.py`.
