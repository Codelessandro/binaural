#all SceneInstance have same parametrization
class Scene:

    def __init__(self,type,sceneid):

        self.type = type
        self.sceneid = sceneid
        
        scenedir = datadir + 'features/cache.binAudLSTM_' + self.type + '_scene' + str(self.sceneid) + '/'

        sceneInstances = []
        for subdir, dirs, files in os.walk(scenedir):
            for file in files:
                if file != "cfg.mat" and file !="fdesc.mat":
                    sI = SceneInstance(self.type,self.sceneid,file)
                    sceneInstances.append(sI)