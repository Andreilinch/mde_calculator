import base64
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import random
import numpy as np
import os
import time
import io
from scipy.stats import norm
import random
from matplotlib.figure import Figure
import pandas as pd
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import exp, cos, linspace

def mde(alpha, beta, sigma, n, Mean):
    return round((((norm.isf(alpha / 2) + norm.isf(1 - beta / 100)) * np.sqrt(2 * (sigma ** sigma) / n)) / Mean) * 100,
                 3)

# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')
#
#
# def create_figure():
#     plt.plot([1,2,3])
#
#     return() #plt.savefig('/static/images/new_plot.png')

# def compute(A=1, b=3, w=2, T=4, resolution=500):
#     """Return filename of plot of the damped_vibration function."""
#     t = linspace(0, T, resolution+1)
#     u = np.sin(b)
#     plt.figure()  # needed to avoid adding curves in plot
#     plt.plot(t, u)
#     plt.title('A=%g, b=%g, w=%g' % (A, b, w))
#
#     if not os.path.isdir('static'):
#         os.mkdir('static')
#     else:
#         # Remove old plot files
#         for filename in glob.glob(os.path.join('static', '*.png')):
#             os.remove(filename)
#         # Use time since Jan 1, 1970 in filename in order make
#         # a unique filename that the browser has not chached
#     plotfile = os.path.join('static', str(time.time()) + '.png')
#     plt.savefig(plotfile)
#     return()# plotfile

# if __name__ == '__main__':
#     print(compute(1, 0.1, 1, 20))