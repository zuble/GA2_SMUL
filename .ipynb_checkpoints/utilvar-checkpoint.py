class utilvar:
    max_vol = -0.3
    
    f = None     #filename w/out extension
    files = None #Arraysof all filenames
    
    audio_in_path = './audio/input/'
    img_out_path = './img/'
    
    audata = None         #AudioDataArray
    audata_overwin = None #AudioDataMatrix Overlapped and Windowed
    dur = None            #AudioDuration
    t = None              #TimeArray acoording sample occurencies
    Fs = 44100            #FreqSampling
    N = None              #Nsamples
    nwin = None           #Nwindows in overlap
    
    w = None
    wlen = 1024 
    wstep = 64 #int(wlen-woverlap)
    
    
    rms = None
    zcr = None
    lat = None    #RealS*
    latStart = None
    latStop = None
    tcntr = None
    ted = None
    nlat = None   #Normalized
    ntcntr = None
    nted = None
    
    cntr = None #DirectOutputVectors
    sprd = None
    flux = None
    flat = None
    
    
    ft_table = None  #TableW/ft
    ft_vector = None #Vector with all ft_info of atual AudioData
    ft_matrix = [] #Matrix with all ft_info of all audio within audio_in_path
    ft_info = ["T-rms.mean","T-rms.std",
               "T-zcr.mean","T-zcr.std",
               "T-LAT","T-centroid","T-effective-dur",
               "S-centroid.mean","S-cntr.std",
               "S-spread","S-sprd.std",
               "S-flux","S-flux.std",
               "S-flatness","S-flat.std"]
    
    #Spectrogram    
    class spec:
        t = None
        f = None
        X = None
    