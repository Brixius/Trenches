from constants import *
import pygame, sys, string, csv, time
from pygame.locals import *
from random import randint
import random
#from random import uniform
from pygaze import libtime
from pygaze.libscreen import Display, Screen
from pygaze.libinput import Keyboard
from pygaze.eyetracker import EyeTracker

# create keyboard object
keyboard = Keyboard()
# display object
disp = Display()
# create eyelink objecy
eyetracker = EyeTracker(disp)
# eyelink calibration
#eyetracker.calibrate()

# Number of frames per second
# Change this value to speed up or slow down your game
# See if can modify the update (when ball location actually changes) with
# another variable to get finer degrees of speed variation.  E.G. on tick,
# if tickcount >= speedmod, do_update.
FPS = 60

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

#Global Variables to be used through our program

screen_width = 800
screen_height = 600
LINETHICKNESS = 10
HOLESIZE = 50 #size of shield
GAMESESSDUR = 10 #duration of game block in seconds
BLOCKSTILQUIT = 4 #Number of blocks to run (reading task and game task)

block_list = pygame.sprite.Group()
shield_list = pygame.sprite.Group()
trench_list = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
#To make this work with Python 3.x, just change out the 3
#super_init calls with the commented out versions.
        super(Block, self).__init__()
#        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Shield(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Shield, self).__init__()
#        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Trench(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Trench, self).__init__()
#        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

#color, width, height
player = Block(RED, 15, 15)
block1 = Block(BLACK, random.randrange(30,80), 15)
shield1 = Shield(RED, 5,20)
block2 = Block(BLACK, random.randrange(30,80), 15)
shield2 = Shield(RED, 5,20)
block3 = Block(BLACK, random.randrange(30,80), 15)
shield3 = Shield(RED, 5,20)
block4 = Block(BLACK, random.randrange(30,80), 15)
shield4 = Shield(RED, 5,20)
block5 = Block(BLACK, random.randrange(30,80), 15)
shield5 = Shield(RED, 5,20)
block6 = Block(BLACK, random.randrange(30,80), 15)
shield6 = Shield(RED, 5,20)
block7 = Block(BLACK, random.randrange(30,80), 15)
shield7 = Shield(RED, 5,20)
#block8 = Block(BLACK, 30, 15)
#shield8 = Shield(RED, 5,20)
#block9 = Block(BLACK, 30, 15)
#shield9 = Shield(RED, 5,20)
#block10 = Block(BLACK, 30, 15)
#shield10 = Shield(RED, 5,20)
trench1 = Trench(BLACK, screen_width, 2)
trench2 = Trench(BLACK, screen_width, 2)

screen = pygame.display.set_mode((screen_width,screen_height)) #SUBJ NUM ENTRY CALL
pygame.display.set_caption('Trenches')

# Set up the colours
BLACK     = (0  ,0  ,0  )
WHITE     = (255,255,255)
OTHCOL = (100,100,100)

#Setting up lists for log file
L1 = ["Subject#"]
L2 = ["Block"]
L3 = ["Trial#"]
L4 = ["Score"]
L5 = ["Speed"]
L6 = ["Hit"]
R1 = ["Subject#"]
R2 = ["Block"]
R3 = ["Trial#"]
R4 = ["Passage"]
R5 = ["ReadingTime"]
A1 = ["Block"]
A2 = ["Answer"]

#Draws the arena the game will be played in. 
def drawArena():
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, BLACK, ((0,0),(screen_width,screen_height)), LINETHICKNESS*2-1)
    
def updateBlockWidths():
    block1 = Block(BLACK, random.randrange(30,80), 15)
    shield1 = Shield(RED, 5,20)
    block2 = Block(BLACK, random.randrange(30,80), 15)
    shield2 = Shield(RED, 5,20)
    block3 = Block(BLACK, random.randrange(30,80), 15)
    shield3 = Shield(RED, 5,20)
    block4 = Block(BLACK, random.randrange(30,80), 15)
    shield4 = Shield(RED, 5,20)
    block5 = Block(BLACK, random.randrange(30,80), 15)
    shield5 = Shield(RED, 5,20)
    block6 = Block(BLACK, random.randrange(30,80), 15)
    shield6 = Shield(RED, 5,20)
    block7 = Block(BLACK, random.randrange(30,80), 15)

    block_list.add(block1, block2, block3, block4, block5, block6, block7)
    shield_list.add(shield1, shield2, shield3, shield4, shield5, shield6, shield7)
    trench_list.add(trench1, trench2)
  
    block1.rect.x = random.randrange(50,100)
    shield1.rect.x = block1.rect.x - 5
    block2.rect.x = random.randrange(150,200)
    shield2.rect.x = block2.rect.x - 5
    block3.rect.x = random.randrange(250,300)
    shield3.rect.x = block3.rect.x - 5
    block4.rect.x = random.randrange(350,400)
    shield4.rect.x = block4.rect.x - 5
    block5.rect.x = random.randrange(450,500)
    shield5.rect.x = block5.rect.x - 5
    block6.rect.x = random.randrange(550,600)
    shield6.rect.x = block6.rect.x - 5
    block7.rect.x = random.randrange(650,700)
    shield7.rect.x = block7.rect.x - 5
 #   block8.rect.x = random.randrange(screen_width)
#    shield8.rect.x = block8.rect.x - 5
#    block9.rect.x = random.randrange(screen_width)
#    shield9.rect.x = block9.rect.x - 5
#    block10.rect.x = random.randrange(screen_width)
#    shield10.rect.x = block10.rect.x - 5
    trench1.rect.x = 0
    trench2.rect.x = 0
    block1.rect.y = random.randrange(50,screen_height - 50)
    block2.rect.y = block1.rect.y
    block3.rect.y = block1.rect.y
    block4.rect.y = block1.rect.y
    block5.rect.y = block1.rect.y
    block6.rect.y = block1.rect.y
    block7.rect.y = block1.rect.y
#    block8.rect.y = block1.rect.y
#    block9.rect.y = block1.rect.y
#    block10.rect.y = block1.rect.y
    shield1.rect.y = block1.rect.y - 3
    shield2.rect.y = block1.rect.y - 3
    shield3.rect.y = block1.rect.y - 3
    shield4.rect.y = block1.rect.y - 3
    shield5.rect.y = block1.rect.y - 3
    shield6.rect.y = block1.rect.y - 3
    shield7.rect.y = block1.rect.y - 3

    trench1.rect.y = block1.rect.y + 40
#upper trench location
    trench2.rect.y = block1.rect.y - 30
    player.rect.x = 0

    block_list.update(block1, block2, block3, block4, block5, block6, block7)
    shield_list.update(shield1, shield2, shield3, shield4, shield5, shield6, shield7)
    trench_list.update(trench1, trench2)

"""
# Testing whether lists were updating properly, with removal (kill())
# of old uncollided blocks and reinstatement of a full new set.

#    for item in block_list:
#        print(item.rect.width)
"""

def drawSprites():
#    all_sprites_list.draw(DISPLAYSURF)
    block_list.draw(DISPLAYSURF)
    shield_list.draw(DISPLAYSURF)
    trench_list.draw(DISPLAYSURF)

def drawPlayer(player):
    if player.rect.bottom >=(trench1.rect.y):
        player.rect.bottom = trench1.rect.y
    elif player.rect.top <=(trench2.rect.y + 2):
        player.rect.top = trench2.rect.y + 2
    pygame.draw.rect(DISPLAYSURF, RED, player)
    drawSprites()

def movePlayer(player):
    player.rect.x += 2
    return player

def checkReachedEnd(player, trialnum, blockend, gametimer):
    if player.rect.right >=(screen_width - LINETHICKNESS):
        eyetracker.stop_recording()
        player.rect.x = LINETHICKNESS
#        setSprites()
        for i in block_list:
            i.kill()
        for i in shield_list:
            i.kill()
        if time.clock()-gametimer >= GAMESESSDUR:
            blockend=1
            return player.rect.x, trialnum, blockend, gametimer
        updateBlockWidths()
        trialnum += 1
#        drawSprites()
        return player.rect.x, trialnum, blockend, gametimer
    else: return player.rect.x, trialnum, blockend, gametimer



def checkPointScored(player, score):
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    shields_hit_list = pygame.sprite.spritecollide(player, shield_list, True)
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print "Block hit.  New score:",score
#        print "Subject number:", subnum #FROM TESTING
    for shield in shields_hit_list:
        score -= 2
        print "Shield hit.  New score:",score
    return score

def displayScore(score):
    resultSurf = BASICFONT.render('Score = %s' %(score), True, RED)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (screen_width - 150, 25)
    DISPLAYSURF.blit(resultSurf, resultRect)

def displayTrialNum(trialnum):
    trialSurf = BASICFONT.render('Trial = %s' %(trialnum), True, RED)
    trialRect = trialSurf.get_rect()
    trialRect.topleft = (50, 25)
    DISPLAYSURF.blit(trialSurf, trialRect)

def displayBlockNum(blocknum):
    blockSurf = BASICFONT.render('Block = %s' %(blocknum), True, RED)
    blockRect = blockSurf.get_rect()
    blockRect.topleft = (250, 25)
    DISPLAYSURF.blit(blockSurf, blockRect)

def quitwrite():
	eyetracker.close()
	csv_out = open("./Logs/" + str(subnum) + "TrenchesReadLogLR.csv",'wb')
	mywriter = csv.writer(csv_out)
	for row in zip(R1, R2, R3, R4, R5):
		mywriter.writerow(row)
	csv_out.close()
	csv_out2 = open("./Logs/" + str(subnum) + "TrenchesAnsLogLR.csv",'wb')
	mywriter2 = csv.writer(csv_out2)
	for row in zip(A1, A2):
		mywriter2.writerow(row)
	csv_out2.close()
	csv_out3 = open("./Logs/" + str(subnum) + "TrenchesGameLogLR.csv",'wb')
	mywriter3 = csv.writer(csv_out3)
	for row in zip(L1, L2, L3, L4, L5, L6):
		mywriter3.writerow(row)
	csv_out3.close()
	pygame.quit()
	sys.exit()

#updates logfile array for reading trials, called in next section (readbits)
def readlog(filename,t0,blocknum,R1,R2,R3,R4,R5):
	print time.clock() - t0, "seconds via time.clock (p1)"
	readtime=time.clock()-t0	
	R5 += [readtime]
	R1 += [subnum]
	R2 += [blocknum]
	R3 += [subnum]
	R4 += [filename]

def readbits(filename,t0,blocknum,R1,R2,R3,R4,R5,A1,A2):
#    pygame.key.set_repeat()
#    if event.type == pygame.KEYDOWN:
  if filename == 'Instruc.png':
    blocknum+=1
    eyetracker.calibrate()
  img=pygame.image.load(filename)
  screen.blit(img,(0,0))
  pygame.display.flip()
  while filename != 70:
    for event in pygame.event.get():
      if event.type == QUIT:
        quitwrite()
      elif event.type == pygame.KEYDOWN:
#        for final version, consider having an "if filename isnumber<lastnumber), filename = filename+1"
#            else if filename = "lastnumber", filename = "lastscreen", etc.  Will likely save space for
#            the final product (reading passage screens, question screens).
#        filename, t0, t1 = readbits(filename, t0, t1)
        if filename == 'Instruc.png':
            global passage
            passage=1
            filename = "B" + str(blocknum) + "P" + str(passage) + ".png"
            img=pygame.image.load(filename)
            screen.blit(img,(0,0))
            t0=time.clock()
            print('key pressed, filename = %s' %(filename))
            # start eye tracking
            eyetracker.start_recording()
            eyetracker.status_msg("trial %s" % filename)
            eyetracker.log("start_image %s" % filename)
            pygame.display.flip()
            return filename,t0,blocknum
        elif filename[:1] == 'B':
            # stop eye tracking from previous reading trial
            eyetracker.stop_recording()
            readlog(filename,t0,blocknum,R1,R2,R3,R4,R5)
            passage += 1
            if passage == 4:
                filename = "Q" + str(blocknum) + ".png"
                print('key pressed, starting question(s)')
            else:
                filename = "B" + str(blocknum) + "P" + str(passage) + ".png"
                print('key pressed, filename = %s' %(filename))
            img=pygame.image.load(filename)
            screen.blit(img,(0,0))
            t0=time.clock()
            # start eye tracking
            eyetracker.start_recording()
            eyetracker.status_msg("trial %s" % filename)
            eyetracker.log("start_image %s" % filename)
            pygame.display.flip()
            return filename,t0,blocknum
        elif filename[:1] == "Q" and event.key == ord('1') or event.key == ord('2') or event.key == ord('3') or event.key == ord('4'):
            qans = event.key - 48 #1 = 49, 4 = 52
            A1 += [blocknum]
            A2 += [qans]
            filename='70'
#            img=pygame.image.load(filename)
#            screen.blit(img,(0,0))
#            t0=time.clock()
#            pygame.display.flip()
            print('%s key pressed, end reading portion' %(qans))
            return filename,t0,blocknum
        else: return filename,t0,blocknum
    if filename=='70':
      return filename,t0,blocknum

#######ATTEMPT TO HAVE A COUNTDOWN BEFORE START OF FIRST TRIAL#######
def gameStartCountdown(starttimer, tcountdown, blockend, blocknum, filename):
	if tcountdown == 70:
#		print 'Setting tcountdown to current time plus 6 seconds.'
		tcountdown = time.clock()+6
	elif starttimer > 0:
#		print 'starttimer is %s' %(starttimer)
		starttimer = int(tcountdown-time.clock())
#		print 'tcountdown is %s' %(tcountdown)
#		print 'new starttimer is %s' %(starttimer)
		startSurf = BASICFONT.render('%s' %(starttimer), True, BLACK)
		startRect = startSurf.get_rect()
		startRect.center = (screen_width/2,screen_height/2)
		DISPLAYSURF.blit(startSurf, startRect)
		pygame.display.update()
		return starttimer,tcountdown,blockend,blocknum,filename
	elif starttimer <= 0:
#		print 'starttime less than or equal to zero'
		starttimer = 5
		tcountdown = 70
		blockend = 0
		gametimer = time.clock()
#		blocknum += 1
		filename="Instruc.png"
		gamebits(gametimer,blockend,blocknum,filename)
		return starttimer,tcountdown,blockend,blocknum,filename
	else:
		blockend=0
		tcountdown=70
		starttimer = 5		
		return starttimer,tcountdown,blockend,blocknum,filename
	return starttimer,tcountdown,blockend,blocknum,filename
#THIS WAS A COMPLETE BASTARD TO GET TO WORK PROPERLY, BECAUSE I DID NOT
#QUITE COMPREHEND THE NECESSITY OF FULL RETURN STATEMENTS AND ELIF DUE
#TO THE FUNCTION NOT ACTUALLY CLOSING WHEN IT JUST CALLS ANOTHER FUNCTION.
#NOTE TO SELF: ALWAYS TEST WHAT HAPPENS WHEN YOU ACTUALLY EXIT OUT OF A
#FUNCTION.  SERIOUSLY.  FUCK.

#######SUBJECT NUMBER ENTRY CODE#######
def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
#  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def getsubnum(screen, question):
#  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")
  

#######END SUBJECT NUMBER ENTRY CODE#######
    

#Main function
def gamebits(gametimer,blockend,blocknum,filename):
#    screen = pygame.display.set_mode((screen_width,screen_height)) #SUBJ NUM ENTRY CALL
#    pygame.display.set_caption('Trenches')
#    global subnum #needed to keep subnum in memory
#    subnum=getsubnum(screen, "Subject #") #SETS SUBJECT NUMBER TO INPUT
#    pygame.init()
#    global DISPLAYSURF
#    ##Font information
#    global BASICFONT, BASICFONTSIZE
#    BASICFONTSIZE = 20
#    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    clock = pygame.time.Clock()
#    DISPLAYSURF = pygame.display.set_mode((screen_width,screen_height))

    score = 0
    trialnum = 1
    player = Block(RED, 15, 15)
    moveDown = False
    moveUp = False

    drawArena()
#    setSprites()
    updateBlockWidths()
    drawSprites()
    drawPlayer(player)

    pygame.mouse.set_visible(0)
    
    while blockend == 0: #main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or gametimer == 0:
                quitwrite()
#Removed mouse control code:
#            elif event.type == MOUSEMOTION:
#                pos = pygame.mouse.get_pos()
#                player.rect.y = pos[1]
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False
        if blockend == 1:
#            blocknum += 1
            filename="Instruc.png"
            return gametimer,blockend,blocknum,filename



        drawArena()
        drawPlayer(player)

        player = movePlayer(player)
        score = checkPointScored(player, score)
#        trialnum = checkReachedEnd(player, trialnum)
        player.rect.x, trialnum, blockend, gametimer = checkReachedEnd(player, trialnum, blockend, gametimer)



        displayScore(score)
        displayTrialNum(trialnum)
        displayBlockNum(blocknum)
 
        if moveDown:
            player.rect.y += 2
        if moveUp:
            player.rect.y -= 2

        pygame.display.update()
        clock.tick(FPS)
##############

def main():
    pygame.init()
    pygame.mouse.set_visible(0) # make cursor invisible
    screen = pygame.display.set_mode((screen_width,screen_height)) #SUBJ NUM ENTRY CALL
    pygame.display.set_caption('Trenches')
#    global subnum
#    subnum=getsubnum(screen, "Subject #") #SETS SUBJECT NUMBER TO INPUT
    blocknum=0

    t0=0
    filename = 'Instruc.png'
#    img=pygame.image.load(filename)
#    screen.blit(img,(0,0))
#    pygame.display.flip()
    
    global DISPLAYSURF
    ##Font information
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    global FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((screen_width,screen_height), pygame.FULLSCREEN)
    starttimer = 5
    global tcountdown
    tcountdown = 70
#    global blockend
    blockend = 0
#    global gametimer
#    gametimer = 2
    drawArena()

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                quitwrite()
#            elif event.type == pygame.KEYDOWN:
#                filename, t0, t1 = readbits(filename, t0, t1)
#        drawArena()
#        filename, t0, t1 = readbits(filename,t0,t1)
##        starttimer, tcountdown, blockend, blocknum = gameStartCountdown(starttimer, tcountdown, blockend, blocknum)
#        gamebits()
#        gamebits(gametimer,blockend)
        #Quit if number of blocks is at the global blocktilquit value
        #Addition of the filename == 70 allows for the final reading trial
        #to complete (readtrial is where block is incremented, would quit
        #after instruction screen without filename tag) -- all together this
        #means we will have BLOCKSTILQUIT number of game blocks, and
        #BLOCKSTILQUIT + 1 number of reading trials.  Which we want.
        if blocknum > BLOCKSTILQUIT and filename == '70':
            quitwrite()
        if filename != '70':
            filename,t0,blocknum = readbits(filename, t0, blocknum, R1, R2, R3, R4, R5, A1, A2)
        elif filename == '70':
            drawArena()
            starttimer, tcountdown, blockend, blocknum, filename= gameStartCountdown(starttimer, tcountdown, blockend, blocknum, filename)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()
