#Basic Bell Curve Fitter: Histogram to Gaussian from CSV
#with multigraph generator

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" 
Code fitter class & graph is appropriated from https://balamuralimblog.wordpress.com/2018/08/12/normaldistribution/

"""

class norm1:
    def __init__(self, a1, b1, c1):
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        
    def dist_curve(self):
        plt.plot(self.c1, 1/(self.b1 * np.sqrt(2 * np.pi)) *
            np.exp( - (self.c1 - self.a1)**2 / (2 * self.b1**2) ), linewidth=2, color='y')
        plt.show()


def col_grabr(stats, i):
    samp_1 = stats.iloc[ 0:, i ]##########
    val = samp_1.values
    mean = np.mean(val)
    sd1 = np.std(val)
    return val, mean, sd1

def multi_grapher(val, mean, sd1, i, title):
    t_full = 'Bell Curve of Generation 1 Pokemon Stats: ' + title
    plt.title( t_full , loc = 'center')
    plt.xlabel(title)
    plt.ylabel('Frequency')
    w1, x1, z1 = plt.hist(val, 20, density=True) #hist
    hist1 = norm1(mean, sd1, x1)
    plot1 = hist1.dist_curve()

        
def main():
    df = pd.read_csv("Pokemon.csv", encoding='cp1252')# https://stackoverflow.com/questions/45529507/unicodedecodeerror-utf-8-codec-cant-decode-byte-0x96-in-position-35-invalid
    stats = df[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']]
    
    for i in range( 0, 6, 1):
        cols = ['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']
        title = cols[i]
        val, mean, sd1 = col_grabr(stats, i)
        multi_grapher(val, mean, sd1, i, title)
        
main() 
