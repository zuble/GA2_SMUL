from scipy.signal import butter, lfilter
import soundfile as sf
import numpy as np
#%run branq-noise-gen.py

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

#white noise gen
fs = 44100
mu, sigma = 0, 1 # mean and standard deviation
s = np.random.normal(mu, sigma, size=2*fs) # 1000 samples with normal distribution

#full spec
sf.write('branquelas-noise.wav', s, 44100, subtype='PCM_24') # Write out audio as 24bit PCM WAV

#bp filtered
branquelas = butter_bandpass_filter(s,900,1100,fs)
sf.write('branquelas-noise-1000.wav', branquelas, 44100, subtype='PCM_24')