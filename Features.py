class Features:
    def __init__(self,features):
        self.features = features


    def plotSpecgram(self):
        plt.imshow(self.features[0,:,0:32])
        plt.show()