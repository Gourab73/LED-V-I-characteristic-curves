import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


xr = np.array([1.6,1.7,1.72,1.74,1.75,1.80,1.81,1.83,1.84,1.85,1.87])
yr = np.array([0,0.1,0.2,0.4,0.5,1.1,1.8,2.3,2.7,3.6,4.4])
def fitR(x1,a1,b1):
    return a1*np.exp(x1*b1)
    
popt, pcov = curve_fit(fitR, xr,yr,p0=[1,1])
xFit_r = np.arange(1.7,1.92,0.02)

xy = np.array([1.76,1.8,1.85,1.86,1.87,1.88,1.9,1.91,1.94,1.96,1.97])
yy = np.array([0,0.1,0.4,0.5,0.7,0.8,1.2,1.6,2.6,3.9,4.8])
def fitY(x2,a2,b2):
    return a2*np.exp(x2*b2)
    
popt2, pcov2 = curve_fit(fitY, xy,yy,p0=[1,1],maxfev=1000)
xFit_y = np.arange(1.79,2,0.02)

xg = np.array([1.87,1.96,2.12,2.16,2.21,2.22,2.24,2.29,2.3,2.33,2.36,2.40,2.41,2.45])
yg = np.array([0,0,0.1,0.2,0.5,0.6,0.7,1.3,1.4,1.7,2.3,2.9,3,3.4])
def fitG(x3,a3,b3):
    return a3*np.exp(x3*b3)
    
popt3, pcov3 = curve_fit(fitG, xg,yg,p0=[1,1],maxfev=1000)
xFit_g = np.arange(1.87,2.51,0.02)

xb = np.array([2.28,2.37,2.49,2.50,2.53,2.57,2.59,2.60,2.63,2.66,2.67,2.68,2.72])
yb = np.array([0,0,0.2,0.3,0.6,1,1.4,1.6,2.1,2.8,3.1,3.4,4.1])
def fitB(x4,a4,b4):
    return a4*np.exp(x4*b4)
    
popt4, pcov4 = curve_fit(fitB, xb,yb,p0=[1,1],maxfev=1000)
xFit_b = np.arange(2.25,2.75,0.02)


xo = np.array([1.53,1.62,1.65,1.69,1.73,1.76,1.78,1.80,1.81,1.84])
yo = np.array([0,0.1,0.3,0.6,1.4,2.5,3.3,4.2,5.2,6.5])
def fitO(x5,a5,b5):
    return a5*np.exp(x5*b5)
    
popt5, pcov5 = curve_fit(fitO, xo,yo,p0=[1,1],maxfev=1000)
xFit_o = np.arange(1.48,1.89,0.02)



plt.scatter(xr, yr,s=10, c='blue')
plt.plot(xFit_r,fitR(xFit_r, *popt), 'red')

plt.scatter(xy, yy,s=10, c='blue')
plt.plot(xFit_y,fitY(xFit_y, *popt2), 'yellow')

plt.scatter(xg, yg,s=10, c='blue')
plt.plot(xFit_g,fitG(xFit_g, *popt3), 'green')

plt.scatter(xb, yb,s=10, c='blue')
plt.plot(xFit_b,fitB(xFit_b, *popt4), 'blue')

plt.scatter(xo, yo,s=10, c='blue')
plt.plot(xFit_o,fitO(xFit_o, *popt5), 'orange')

plt.title('V-I characteristic plots of LEDs', size=15)
plt.xlabel('Forward Voltage(volt)')
plt.ylabel('Forward Current(mA)')
plt.legend(["Red LED", "Yellow LED", "Green LED", "Blue LED", "Orange LED"], loc ="upper right")
plt.grid()
plt.show()

