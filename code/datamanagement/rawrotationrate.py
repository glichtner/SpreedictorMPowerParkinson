import os
import joblib
import itertools
import synapseclient
import pandas as pd
import numpy as np
from .numpydataset import NumpyDataset

datadir = os.getenv('PARKINSON_DREAM_DATA')

class RawRotationRate(NumpyDataset):
    def __init__(self, variant, reload_ = False, training = True, rmnan = True):
        self.npcachefile = os.path.join(datadir,
                "rawrotationrate_{}.pkl".format(variant))

        self.columns = list(itertools.product(["rotationRate"], \
                    ["x","y","z"]))
        NumpyDataset.__init__(self, "deviceMotion", variant, reload_, training, rmnan)

    def getValues(self, df):
        M = df[[ "_".join(el) for \
            el in self.columns]].values.astype("float32")
        shift = M.mean(axis=0)
        M -= shift
        return M

class RawRotationRateOutbound(RawRotationRate):
    '''
    Raw rotationRate for outbound walk
    '''
    def __init__(self, reload_ = False, training = True, rmnan = True):
        RawRotationRate.__init__(self, "outbound", reload_, training, rmnan)

class RawRotationRateRest(RawRotationRate):
    '''
    Raw rotationRate for rest phase
    '''
    def __init__(self, reload_ = False, training = True, rmnan = True):
        RawRotationRate.__init__(self, "rest", reload_, training, rmnan)

class RawRotationRateReturn(RawRotationRate):
    '''
    Raw rotationRate for return walk
    '''
    def __init__(self, reload_ = False, training = True, rmnan = True):
        RawRotationRate.__init__(self, "return", reload_, training, rmnan)
