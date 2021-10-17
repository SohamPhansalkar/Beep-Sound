# Winsound Advaned
import winsound

# frequency is set to 500Hz
freq = 2500 
  
# duration is set to 1000 milliseconds = 1 second        
dur = 1000

freq = input("Put the frequency You want in the Beep sound : ")
if freq == "" or freq == "0":
    freq = 2500
    
dur = input("Put the duration of the sound (1000 = 1s) : ")
if dur == "" or dur == "0":
    dur = 2000
               
winsound.Beep(freq, dur)
