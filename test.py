import pyACA
import librosa
import librosa.display
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
import numpy as np
import os
from scipy.signal import spectrogram

def load_files():
    """Finds and loads files from within folder structure."""
    files = [x for x in os.listdir(util.audio_in_path) if x != '.ipynb_checkpoints']
    print(files)
    return files

def main():
    
    #Load into array all audio to feature
    files = load_files()
    
    #HannWindow
    util.w = np.hanning(util.wlen)
    
    print("wlen:",util.wlen,
          "| wstep:",util.wstep)
    print(files)
    
    for fwav in files:
        print('-------------------------------------------------------------------------------------------')
        
        #Load audio and print basic info related to file processing 
        load_audio(fwav)
        print(fwav,
              "\n\tN = %d samples" %util.N , 
              " | Dur = %f seconds" %util.dur , 
              " | Fs = %d Hz" %util.Fs)
        
        #Spectral side of life
        [util.spec.f, util.spec.t, X] = spectrogram(util.audata,
                                                    fs=util.Fs,
                                                    window=util.w,
                                                    nperseg=util.wlen,
                                                    noverlap=util.wlen - util.wstep,
                                                    nfft=util.wlen,
                                                    detrend=False,
                                                    return_onesided=True,
                                                    scaling='spectrum')
        
        #We just want the magnitude spectrum...
        util.spec.X = np.sqrt(X / 2)
        
        
        #SPECTRAL CENTROID
        util.ft.cntr = pyACA.FeatureSpectralCentroid(X, util.Fs) #output the vector
        centroid_mean = np.around(np.mean(util.ft.cntr) , decimals=5)
        centroid_std = np.std(util.ft.cntr)
        centroid_plot()
    
    
        
        #SPECTRAL SPREAD
        #SPECTRAL FLUX
        #SPECTRAL FLATNESS
         
        plt.show()

if __name__ == '__main__':
    main()