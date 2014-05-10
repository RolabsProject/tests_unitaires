#!/usr/bin/python

import cwiid
import sys
import os

import cwiid, time
from numpy import * #Import matrix libraries
from pylab import *

print "Press 1 & 2 on the Wiimote simultaneously to find it"
 
global wiimote
while True:
	try:
		wiimote = cwiid.Wiimote('00:1F:C5:47:E4:F1')#add address of Wiimote here for speedup)
		break
	except:
		continue
global led
led = True
wiimote.led = cwiid.LED1_ON
wiimote.rpt_mode = cwiid.RPT_BTN
wiimote.enable(cwiid.FLAG_MESG_IFC)

cwiid.LED1_ON
 
print "Wiimote activiated..."
print "Press + to start recording and - to stop recording"
 
# Set Wii Parameters to get
wiimote.enable(cwiid.FLAG_MESG_IFC)
wiimote.rpt_mode = cwiid.RPT_IR | cwiid.RPT_BTN
 
# Setup Initial Constants
t=[]
ir_x=[]
ir_y=[]
ir_s=[]
rec_flg =0
flg=True
t_i = time.time()   # Initial Time
 
# -----------------------------------------------------------------------------
# Check for Wii Commands until stop (- button) is pressed
while flg==True:
    time.sleep(0.01)    # Wait 1 hundredth of a second between Wiimote messages
    messages = wiimote.get_mesg()   # Get Wiimote messages
 
    for mesg in messages:   # Loop through Wiimote Messages
        if mesg[0] == cwiid.MESG_IR: # If message is IR data
            if rec_flg == 1:    # If recording
                for s in mesg[1]:   # Loop through IR LED sources
                    if s:   # If a source exists
                        print s['pos'][0], s['pos'][1], s['size']
 
                        t.append(time.time()-t_i)                       
                         
        elif mesg[0] == cwiid.MESG_BTN:  # If Message is Button data
            if mesg[1] & cwiid.BTN_PLUS:    # Start Recording
                rec_flg = 1
                print "Recording..."
            elif mesg[1] & cwiid.BTN_MINUS: # Stop Recording
                flg=False
                break
 
 
show()
