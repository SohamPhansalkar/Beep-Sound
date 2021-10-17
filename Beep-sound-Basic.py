import winsound # No need to do pip install as it is pre-installed 

# Frequency is set to 500Hz
frequency = 500 

# Duration is set to 1 second (1000 = 1 Second)           
duration = 1000
               
winsound.Beep(frequency, duration)
