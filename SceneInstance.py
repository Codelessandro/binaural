import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from datetime import datetime, date, time
import pandas as pd
import pdb
import os
import matplotlib.pyplot as plt

from Labels import Labels
from Features import Features

from Settings import *



#scp -r alessandroschneider@cursa.ni.tu-berlin.de:"'/mnt/raid/data/ni/twoears/reposX/idPipeCache/MultiEventTypeTimeSeriesLabeler(footsteps)'"  "MultiEventTypeTimeSeriesLabeler(footsteps)"
#pdb.set_trace()




class SceneInstance:

    def __init__(self, type, sceneid, name):

        self.type = type
        self.sceneid = sceneid
        self.name = name
        self.loadData()


    def loadMetaData(self):
        self.nSrcs = 2
        pass


    def loadFeatures(self):
        np.set_printoptions(threshold=np.nan)

        features = loadmat(datadir + 'features/cache.binAudLSTM_' + self.type + '_scene' + str(self.sceneid) + '/' + self.name)
        features = np.array(features["x"])
        
        self.fClass = Features(features)


    def loadSound(self):
        
        soundfile = datadir + 'sounds/cache.mc3_' + self.type + '_scene' + str(self.sceneid) + '/' + self.name.replace(".mat", "")
        print ("in command line:  open " + soundfile)

        


    def demo(self):
        #self.fClass.plotSpecgram()


        self.loadSound()
        self.lClass.plotLabels()

        
    def loadLabels(self):
        allLabelData = []

        for e,label in enumerate(labelcats):
            fileData = loadmat(datadir + 'label/MultiEventTypeTimeSeriesLabeler(' + label + ')/cache.binAudLSTM_' + self.type + '_scene' + str(self.sceneid) + '/' + self.name)
            
            singleLabelData = np.squeeze(fileData["y"], axis=0)
            allLabelData.append(singleLabelData)
            print label
            print e 
            print "--"
            #pdb.set_trace()

        allLabelData = np.array(allLabelData)
        self.lClass = Labels(allLabelData)
        

            
    def loadData(self):
        self.loadFeatures()
        self.loadLabels()







