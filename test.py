import matplotlib.pyplot as plt
from pylab import *
figure(figsize=(8, 6), dpi=80)
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plot(X, C, color="blue", linewidth=1.0, linestyle="-")
