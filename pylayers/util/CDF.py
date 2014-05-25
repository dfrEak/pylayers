# -*- coding:Utf-8 -*-

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pdb
#import mplrc.ieee.transaction
#
# mplrc is a python module which provides an easy way to change
# matplotlib's plotting configuration for specific publications.
# git clone https://github.com/arsenovic/mplrc.git
#
#
from matplotlib import rcParams


rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True


class CDF(object):
    def __init__(self, ld, filename):
        """
        cdf = CDF(ld)

        ld is a list of dictionnary

        d0 = ld[0]

        d0['bound']       : abscisse bounds of the cdf
        d0['values']      : valeurs
        d0['xlabel']      :
        d0['ylabel']      :
        d0['legend']      : legend
        d0['title]        : title
        d0['filename]     : filename
        d0['linewidth']   : linewidth

        """
        self.ld = ld
        self.parmsh = {}
        self.parmsh['file'] = True
        self.filename = filename
        """
        plt.rcParams['xtick.labelsize'] ='x-large'
        plt.rcParams['ytick.labelsize'] ='x-large'
        plt.rcParams['axes.labelsize']  ='large'
        plt.rcParams['font.weight']     ='normal'
        plt.rcParams['xtick.minor.size']=2
        plt.rcParams['legend.fontsize'] = 'xx-large'
        plt.rcParams['font.size']       =20
        plt.rcParams['grid.linewidth']  =3.5
        plt.rcParams['xtick.major.pad'] =20
        """
        self.cdf = []
        for d in self.ld:
            bound = d['bound']
            values = d['values']
            Nv = len(values)
            cdf = np.array([])
            for k in bound:
                u = np.nonzero(values <= k)
                lu = len(u[0]) / (Nv * 1.0)
                cdf = np.hstack((cdf, lu))

            self.cdf.append(cdf)

    def show(self,**kwargs):
        """ show cdf
        """
        if 'fig' not in kwargs:
            f = plt.figure(**kwargs)
        else:
            f = kwargs['fig']

        if 'ax' not in kwargs:
            ax = f.add_subplot(111)
        else:
            ax == kwargs['ax']

        leg = []
        c = []

        for k in range(len(self.ld)):

            d = self.ld[k]
            bound = d['bound']
            marker = d['marker']
            markersize = d['markersize']
            markercolor = d['markercolor']
            markerfrequency = d['markerfrequency']
            linewidth = d['linewidth']
            linestyle = d['linestyle']
            color = d['color']
            legend = d['legend']
#                       leg.append(legend)
            cdf = self.cdf[k]
            c.append(ax.plot(bound, cdf, marker=marker,
              markevery=markerfrequency, ms=markersize, mfc=markercolor,
                             ls=linestyle, c=color, linewidth=linewidth,
                             label=legend))
            plt.xlabel(self.ld[0]['xlabel'])

        plt.ylabel(self.ld[0]['ylabel'])
        ax.legend(loc='best', scatterpoints=1, numpoints=1.)
        plt.grid()
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.savefig(self.filename + '.pdf', format='pdf',
                    bbox_inches='tight', pad_inches=0)
        plt.savefig(self.filename + '.eps', format='eps',
                    bbox_inches='tight', pad_inches=0)


if __name__ == "__main__":
    d0 = {}
    d0['values'] = sp.randn(1000)
    d0['bound'] = np.arange(-10, 10, 0.1)
    d0['xlabel'] = 'xlabel'
    d0['ylabel'] = 'ylabel'
    d0['legend'] = 'legend '
    d0['markersize'] = 3
    d0['markercolor'] = 'red'
    d0['markerfrequency'] = 2
    d0['title'] = 'title'
    d0['color'] = 'black'
    d0['marker'] = 'o'
    d0['linestyle'] = '-'
    d0['linewidth'] = 3
    d0['filename'] = 'essai.png'
    d1 = {}
    d1['values'] = 4 * sp.randn(1000)
    d1['bound'] = np.arange(-10, 10, 0.1)
    d1['xlabel'] = 'xlabel'
    d1['ylabel'] = 'ylabel'
    d1['legend'] = 'legend '
    d1['markersize'] = 3
    d1['markercolor'] = 'blue'
    d1['linestyle'] = '-'
    d1['color'] = 'black'
    d1['markerfrequency'] = 2
    d1['title'] = 'title'
    d1['marker'] = 'o'
    d1['linewidth'] = 3
    lv = [d0, d1]
    c = CDF(lv, 'fig')
    c.show()
