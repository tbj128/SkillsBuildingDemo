import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--learning_rate", type=float, default=0.01)

args = parser.parse_args()

print("learning rate is %f" % args.learning_rate)
# Hyperparameters
x = 0.1
noise = 0.1

# Simulated training loss
loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * noise)

print("loss: %f" % loss)

for i in range(10):
    print(f"{i}: accuracy loss: 95")
