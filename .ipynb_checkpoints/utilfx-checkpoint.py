import numpy as np
import sklearn
from sklearn import preprocessing
from essentia import *
from essentia.standard import *

from utilvar import utilvar as utilv
 
def overlap_n_window():
    """
    Computes a matrix version of utilv.audata that is windowed 
    by a hann window with size = utilv.wlen and overlapped by utilv.step
    """
    window_len, window_step = map(int, (utilv.wlen, utilv.wstep))
    if window_len % 2 != 0:
        raise ValueError("Window size must be even!")
    
    X = utilv.audata
    # Make sure there are an even number of windows before stridetricks
    append = np.zeros((window_len - len(X) % window_len)) #478
    X = np.hstack((X, append)) #22050 + 478 = 22528 ; len(X) multiplo de utilv.w.len
    
    ws = window_len
    ss = window_step
    a = X

    valid = len(a) - ws #retira a primeira janela
    nw = (valid) // ss #n janelas que vai iterar
    X_win = np.ndarray((ws,nw),dtype = a.dtype)
    
    #print("\taudata_overwind =" , np.shape(X_win) , "(wlen , nwin)")
    
    for i in range(nw):
        start = i * ss
        stop = start + ws
        #get X windowed / 1 janela por coluna
        X_win[:,i] = a[start : stop] * utilv.w
    
    utilv.audata_overwin = X_win
    utilv.nwin = nw
    
def normalize(x, axis=0):
    """
    Normalizes the values within tthe array to values between 0 and 1
      Args:
        x: input array 

      Returns:
        normalized version of x
    """
    return sklearn.preprocessing.minmax_scale(x, axis=axis)


def zcr_generate():
    """
    Computes a ZCR per frame of utilv.audata_overwin , thus generating a array 
    """
    zcr = np.zeros( utilv.nwin );
    zcr2 = np.zeros( utilv.nwin );

    #zero_crossings = numpy.where(numpy.diff(numpy.sign(a)))[0] outputs array with indices where it crossed
    x = utilv.audata_overwin

    for i in range(utilv.nwin):

        zcr_cont = 0
        for j in range(np.shape(x)[0] - 1): #np.shape(x)[0] = window_len
            if x[j,i] * x[j+1,i] < 0 :
                zcr_cont = zcr_cont + 1
                
        zcr[i] = zcr_cont / utilv.wlen
        zcr2[i] = np.sum(np.diff(np.sign(x[:,i])) != 0, axis=0) / utilv.wlen

    utilv.zcr = zcr

    
def rms_generate():
    """
    Computes a RMS per frame of utilv.audata_overwin , thus generating a array 
    """
    x = utilv.audata_overwin
    rms = np.zeros( utilv.nwin);
    
    for i in range(utilv.nwin):
        rms[i] = np.sqrt(np.mean(x[:,i]**2))
       
    utilv.rms = rms

def rms_lib_replica_generate():
    """
    Alternative rms_generate
    """
    rmse = []
    # calculate rmse for each frame
    for i in range(0, len(utilv.audata), utilv.wstep): 
        rmse_current_frame = np.sqrt(sum(utilv.audata[i:i+utilv.wlen]**2) / utilv.wlen)
        rmse.append(rmse_current_frame)
    return np.array(rmse) 


def env_generate():
    """
    https://essentia.upf.edu/reference/std_Envelope.html
    Computes a envelope of utilv.audata
    """
    envelope = Envelope( attackTime = 5,releaseTime = 25)
    utilv.Env = envelope(utilv.audata) #envelope according utilv.t
        
    
#https://essentia.upf.edu/reference/streaming_LogAttackTime.html
def lat_generate():
    """
    https://essentia.upf.edu/reference/streaming_LogAttackTime.html
    Computes a Log Attack Time (base10) value of utilv.audata envelope
    """
    logAttackTime = LogAttackTime()
    utilv.lat , utilv.latStart, utilv.latStop = logAttackTime(utilv.Env)
    utilv.nlat = (10**(utilv.lat)) / utilv.dur
    
    
#https://essentia.upf.edu/reference/streaming_Centroid.html  
def tcntr_generate():  
    """
    https://essentia.upf.edu/reference/streaming_Centroid.html
    Computes a Temporal Centroid value of utilv.audata envelope
    """
    centroid = Centroid(range = ((utilv.N-1) / utilv.Fs) )
    utilv.tcntr = centroid(utilv.Env)
    utilv.ntcntr = utilv.tcntr / utilv.dur
    
    
def ted_generate():
    """
    Computes the Temporal Effective Duration of utilv.audata
    """
    threshold = 0.4*np.max(utilv.audata)
    indices = np.where(np.abs(utilv.audata) > threshold)[0]
    p1 = indices[0]
    p2 = indices[len(indices)-1]
    utilv.ted = (p2 - p1) / utilv.Fs
    utilv.nted = utilv.ted / utilv.dur   
    
    
def moving_average(a, n=30):
    """
    Creates a moving average to apply smoothing to the spectral centroid plot
    """
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n