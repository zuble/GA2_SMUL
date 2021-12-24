class utilvar:
    max_vol = -0.3
    
    audio_in_path = './audio/input/'
    img_out_path = './img/'
    f = None #filename w/out extension
    
    audata = None         #AudioDataArray
    audata_overwin = None #AudioDataMatrix Overlapped and Windowed
    dur = None #AudioDuration
    t = None   #TimeArray acoording sample occurencies
    Fs = 44100  #FreqSampling
    N = None   #Nsamples
    nwin = None #Nwindows in overlap
    
    w = None
    wlen = 2048
    wstep = 512 #int(wlen-woverlap)
    
    class ft:
        rms = None
        zcr = None
        cntr = None #all vectors
        sprd = None
        flux = None
        flat = None
        
    class spec:
        t = None
        f = None
        X = None