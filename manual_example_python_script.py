#======================================
# XRF python example, (c) MOGLabs 2016
#======================================
from mogdevice_dummy import MOGDevice # dummy MOGDevice for code test
# from mogdevice import MOGDevice

# connect to the device
dev = MOGDevice('10.1.1.23')
# print some information
print('Device info:', dev.ask('info'))
# example command: set frequency
dev.cmd('FREQ,1,100MHz')
# example query: check frequency
print('CH1 Freq:', dev.ask('FREQ,1'))
# some queries can return dictionaries
print('Temperatures:', dev.ask_dict('TEMP'))
# other queries respond with binary data
tbl = dev.ask_bin('TABLE,DUMP,1')
print('Binary table:', len(tbl))
# close the connection
dev.close()

#======================================
# XRF Gaussian pulse example, (c) MOGLabs 2016
#======================================
from mogdevice import MOGDevice
import numpy as np
# connect to the device
dev = MOGDevice('10.1.1.45')
print('Device info:', dev.ask('info'))
# construct the pulse
N = 200
X = np.linspace(-2,2,N)
Y = 30*(np.exp(-X**2)-1) # =30 to 0dBm
dev.cmd('MODE,1,TSB') # set CH1 into table mode
dev.cmd('TABLE,ENTRIES,1,0') # clear existing table
for y in Y: # upload the entries
    dev.cmd('TABLE,APPEND,1,100,%.2f,0,5'%y)
print(dev.cmd('TABLE,ARM,1')) # ready for execution
