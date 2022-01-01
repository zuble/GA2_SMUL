# GA2_SMUL
Low-Level features and timbre characterization on classical instruments 

Avaiable features:
 - **Temporal**  
  ZCR  
  RMS   
  Log Attack Time  
  Temporal Centroid  
  Effective Duration  
 -  **Spectral**  
    Centroid  
    Spread/Bandwidth  
    FLux  
    Flat   
   

### Environment Install

    $ conda env create --file environment.yml --name ga2
    $ conda activate ga2
    $ jupyter lab


###  Audio Data Management
Put the data you want to process inside /audio/input  
Then change in utilvar.py under *class:vs* accordingly, with the name partition being underscore  

    /GA2_SMUL/audio/input$ ls 
    flt_G1.wav  saxof_G3.wav
      
    class vs:
        instr = ["flt","saxof"]
        cor   = [ "y" , "m" ]
        mrk   = [ "v" , "1" ]

### PLots Examples
Envelope + LAT + EffectiveDuration  
![alt text](https://github.com/zuble/GA2_SMUL/blob/main/img/acc_qu_G2_12_env%2Blat%2Btcntroid.png)

Feature Versus  
![alt text](https://github.com/zuble/GA2_SMUL/blob/main/img/FEATURE_VERSUS.png)
