#======================================
# XRF Python Example: Send Advanced Table Script for Sinusoidal Frequency Ramp
# (c) MOGLabs Example (adapted)
#======================================

from mogdevice_custom.mogdevice_dummy import MOGDevice # dummy MOGDevice for code test
# from mogdevice import MOGDevice

# Connect to the device
# For Ethernet connection, use the device IP (e.g., '10.1.1.23')
# For USB connection, note: the device appears as a Virtual COM port (e.g., 'COM4')
device_address = '10.1.1.23'  # Change to 'COM4' or the appropriate COM port for USB
dev = MOGDevice(device_address)

# Print device info for confirmation
print('Device info:', dev.ask('info'))

# Define the advanced table script as a multi-line string
table_script = """
; Set Channel 1 to advanced table mode (TPA)
MODE,1,TPA

; Set the initial fixed parameters for Channel 1
FREQ,1,100MHz
POW,1,26dBm
PHAS,1,0deg

; Clear any existing table on Channel 1
TABLE,CLEAR,1

; Entry 1: Hold the initial state for 500 µs to ensure output stabilization
TABLE,ENTRY,1,500,100MHz,26dBm,0deg

; Arm the table to wait for an external trigger on a rising edge
TABLE,ARM,1,EXT,RISE

; Define the sweep entries approximating the sin² profile
TABLE,ENTRY,2,1000,100.0MHz,26dBm,0deg,100.49MHz,26dBm,0deg
TABLE,ENTRY,3,1000,100.49MHz,26dBm,0deg,101.91MHz,26dBm,0deg
TABLE,ENTRY,4,1000,101.91MHz,26dBm,0deg,104.12MHz,26dBm,0deg
TABLE,ENTRY,5,1000,104.12MHz,26dBm,0deg,106.91MHz,26dBm,0deg
TABLE,ENTRY,6,1000,106.91MHz,26dBm,0deg,110.00MHz,26dBm,0deg
TABLE,ENTRY,7,1000,110.00MHz,26dBm,0deg,113.09MHz,26dBm,0deg
TABLE,ENTRY,8,1000,113.09MHz,26dBm,0deg,115.88MHz,26dBm,0deg
TABLE,ENTRY,9,1000,115.88MHz,26dBm,0deg,118.09MHz,26dBm,0deg
TABLE,ENTRY,10,1000,118.09MHz,26dBm,0deg,119.51MHz,26dBm,0deg
TABLE,ENTRY,11,1000,119.51MHz,26dBm,0deg,120.00MHz,26dBm,0deg

; Enable auto‑restart so that once the sequence finishes, the table automatically re‑arms for the next trigger
TABLE,RESTART,1,ON
"""

# Send each command from the table script to the device.
# Comment lines (starting with ';') and empty lines are skipped.
for line in table_script.strip().splitlines():
    command = line.strip()
    if not command or command.startswith(';'):
        continue
    # Send the command and print the response (for debugging)
    response = dev.cmd(command)
    print("Sent:", command, "Response:", response)

# Optionally, dump the table as binary data to verify it was uploaded correctly
binary_table = dev.ask_bin('TABLE,DUMP,1')
print("Binary table length:", len(binary_table))

# Close the connection to the device
dev.close()
