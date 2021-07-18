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
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def mde(alpha, beta, sigma, n, Mean):
    return round((((norm.isf(alpha / 2) + norm.isf(1 - beta / 100)) * np.sqrt(2 * (sigma ** sigma) / n)) / Mean) * 100,
                 3)

def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 5) for x in xs]
    axis.plot(xs, ys)
    fig.savefig('/static/images/new_plot.png')
    return #fig

