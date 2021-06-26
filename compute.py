from numpy import linspace
import matplotlib.pyplot as plt
import os, time, glob

def mde_calc(alpha, beta):
    return alpha*beta #2 * (sigma**2) * ((stats.norm.ppf(1-alpha/2) + stats.norm.ppf(1-beta))**2) / ((mu * MDE)**2)

def compute(alpha, beta ):
    return alpha*beta

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


#if __name__ == '__main__':
#    print compute(1, 2)