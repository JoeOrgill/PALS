# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 11:55:01 2022

@author: php20jo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import splev, splrep

def conv(x,height,position,std,A,l1,B,C,l3):
    l2=(1/0.125)
    g=height*np.exp(-(x-position)**2/(2*std**2))
    e=(A * (np.exp(-(l1 * x))) + B * (np.exp(-(l2 * x))) + C * (np.exp(-(l3 * x))))# + D)
    return (np.convolve(g,e,mode='full') / sum(e) )[:667]

#new convolution funnction with 4 exponrtials
## 2 for different pore sizes
def conv2(x,height,position,std,A,l1,B,C,l3,E,l4):
    l2=(1/0.125)
    g=height*np.exp(-(x-position)**2/(2*std**2))
    e=(A * (np.exp(-(l1 * x))) + B * (np.exp(-(l2 * x))) + C * (np.exp(-(l3 * x))) + E * (np.exp(-(l4 * x))
    return (np.convolve(g,e,mode='full') / sum(e) )[:667]


def flat(x,D):
    y=D
    return y
