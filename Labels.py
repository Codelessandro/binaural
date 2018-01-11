import matplotlib.pyplot as plt
from Settings import *
import pdb

class Labels:
    def __init__(self,labels):
        self.labels = labels


    def plotLabels(self):

        #pdb.set_trace()

        plt.subplot(221)
        plt.yticks(range(len(labelcats)), labelcats)
        plt.imshow(self.labels[:,::10], origin='lower')
        plt.show()
        
        plt.subplot(221)
        plt.yticks(range(len(labelcats)), labelcats)
        plt.imshow(self.labels[:,::10], origin='lower')
        plt.show()
