# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:01:22 2016

@author: William
"""


# MAIN
DUMMYMODE = True # False for gaze contingent display, True for dummy mode (using mouse or joystick)
LOGFILENAME = raw_input("Enter subject number: ") # logfilename, without path
LOGFILE = LOGFILENAME[:] # .txt; adding path before logfilename is optional; logs responses (NOT eye movements, these are stored in an EDF file!)
subnum = LOGFILENAME #LFN is name for pygaze and tracker logs, subnum is for the custom exp code already written before adding ET stuff.
DIREC = int(raw_input("Enter 1 to start with left to right, 2 for right to left: "))
#TRIALS = 1

# Number of frames per second
# Change this value to speed up or slow down your game
FPS = 60

#Global Variables to be used through our program

screen_width = 800
screen_height = 600
LINETHICKNESS = 10
HOLESIZE = 50 #size of shield
GAMESESSDUR = 30 #duration of game block in seconds
BLOCKSTILQUIT = 8 #Number of blocks to run (reading task and game task)
BLOCKSTILSWITCH = 4 #Number of blocks to run before switching game task direction.
    #Set to half of BLOCKSTILQUIT to switch in the middle.
    #Set equal to BLOCKSTILQUIT to keep the same direction for the entire run.
RECALBLOCK = 5 #Block to have a calibration screen come up between reading and
	#game trials.  To recal between them just before game direction switches,
	#set to BLOCKSTILSWITCH + 1.

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,  50,   50)
OTHCOL = (230,230,230)

playercolour = OTHCOL

# DISPLAY
SCREENNR = 0 # number of the screen used for displaying experiment
DISPTYPE = 'pygame' # either 'psychopy' or 'pygame'
DISPSIZE = (800,600) # canvas size
SCREENSIZE = (36.0,26.6) #physical screen size in centimeters.
SCREENDIST = 80.0 #distance from participant to screen in centimeters
MOUSEVISIBLE = False # mouse visibility
#BGC = (125,125,125) # backgroundcolour
#FGC = (0,0,0) # foregroundcolour
BGC = (0,0,0) # backgroundcolour for calibration
FGC = (255,255,255) # foregroundcolour (text) for calibration
FONTSIZE = 32 # font size

# INPUT
KEYLIST = None # None for all keys; list of keynames for keys of choice (e.g. ['space','9',':'] for space, 9 and ; keys)
KEYTIMEOUT = 1 # None for no timeout, or a value in milliseconds

# EYETRACKER
# general
TRACKERTYPE = 'eyelink' # either 'smi', 'eyelink' or 'dummy' (NB: if DUMMYMODE is True, trackertype will be set to dummy automatically)
#SACCVELTHRESH = 35 # degrees per second, saccade velocity threshold
#SACCACCTHRESH = 9500 # degrees per second, saccade acceleration threshold

# STIMULUS
#STIMSIZE = 100 # stimulus size (pixels)
#STIMCOL = (255,255,0) # stimulus colour
#STIMPOS = (DISPSIZE[0]/2,DISPSIZE[1]/2) # start position
#STIMREFRESH = 2500 # ms; time before stimulus is set to new position

# GAME
