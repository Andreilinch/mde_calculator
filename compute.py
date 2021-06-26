import numpy as np
# import matplotlib.pyplot as plt
from scipy.stats import norm
#import os, time, glob


# def damped_vibrations(alpha, beta):
#    return alpha*beta

def compute(alpha, beta, sigma, n):
    return (norm.isf(alpha / 2) + norm.isf(beta/100)) * np.sqrt(2*(sigma**sigma)/ n)

# **resolution=500):
# """Return filename of plot of the damped_vibration function."""
# t = linspace(0, T, resolution+1)
# u = damped_vibrations(alpha, beta)
# plt.figure()  # needed to avoid adding curves in plot
# plt.plot(t, u)
# plt.title('A=%g, b=%g, w=%g' % (A, b, w))
# if not os.path.isdir('static'):
#     os.mkdir('static')
# else:
#     # Remove old plot files
#     for filename in glob.glob(os.path.join('static', '*.png')):
#         os.remove(filename)
# Use time since Jan 1, 1970 in filename in order make
# a unique filename that the browser has not chached
# plotfile = os.path.join('static', str(time.time()) + '.png')
# plt.savefig(plotfile)


# if __name__ == '__main__':
#    print compute(1, 2)
