from scipy import stats
import numpy as np
import pandas as pd

class slope_estimator():
    def __init__(self, tailleWin=20):
        self.tailleWin = tailleWin
        
    def fit(self, X, y = None):
        
        values = np.array([X]).T
        X_window = []
        for ind in range (0, 800 - self.tailleWin):
            X_window.append(values[ind : ind + self.tailleWin])

        X_window = np.array(X_window)
        dfX = pd.DataFrame(data = X_window.reshape(-1,self.tailleWin))        
        
        
        
        dataPente = []
        for ind in range(len(dfX.index)):
            pts = dfX.iloc[ind]

            slope,_,_,_,_ = stats.linregress(range(self.tailleWin), pts)
            dataPente.append(slope)
        dataPente = np.array(dataPente)      
        return dataPente