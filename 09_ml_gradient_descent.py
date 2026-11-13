"""
09 - Gradient Descent

Aim: Implement Gradient Descent Algorithm to find the local minima of a function.
     Example: find the local minima of y = (x+3)^2 starting from the point x = 2.

Update rule:  x_new = x_old - learning_rate * dy/dx      (here dy/dx = 2(x + 3))
Answer     :  minima at x = -3, y = 0

Complexity:
  Time  : O(k) -> k = number of iterations, each step is constant work
  Space : O(1) -> only x is needed (xs list is just for the plot)

Key terms:
  Gradient         : slope (derivative) of the function at a point.
  Gradient descent : move step by step opposite to the slope (downhill) to reach the minimum.
  Learning rate    : step size. Too big -> overshoots/never converges; too small -> very slow.
  Convergence      : stopping when the slope is almost 0.
  Local minima     : lowest point in a nearby region (like a small valley).
  Global minima    : lowest point of the whole function.
                     Gradient descent can get stuck in a local minima; y = (x+3)^2 has
                     only one minimum, so here local = global.
  First steps (lr = 0.1): x = 2 -> grad 10 -> x = 1 -> grad 8 -> x = 0.2 -> ... -> -3
  Use in ML        : minimizing the loss function to find model weights.
  Types            : Batch, Stochastic (SGD), Mini-batch.
"""

import matplotlib.pyplot as plt

def f(x):
    return (x + 3) ** 2

def gradient(x):              # dy/dx = 2(x + 3)
    return 2 * (x + 3)

x = 2                         # starting point
lr = 0.1                      # learning rate
xs = [x]

for i in range(100):
    x = x - lr * gradient(x)  # update rule
    xs.append(x)
    if abs(gradient(x)) < 0.0001:   # stop when slope is almost 0
        break

print("Local minima at x =", round(x, 4))
print("Minimum value y   =", round(f(x), 4))
print("Iterations        :", i + 1)

# Plot the curve and the steps taken
X = [v / 10 for v in range(-80, 40)]
plt.plot(X, [f(v) for v in X], label="y = (x+3)^2")
plt.scatter(xs, [f(v) for v in xs], color="red", label="steps")
plt.legend()
plt.show()
