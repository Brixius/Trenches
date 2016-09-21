from constants import *
import pygame, sys, string, csv, time
from pygame.locals import *
from random import randint
import random
from pygaze import libtime
from pygaze.libscreen import Display, Screen
from pygaze.libinput import Keyboard
from pygaze.eyetracker import EyeTracker

keyboard = Keyboard()
disp = Display()
eyetracker = EyeTracker(disp)

block_list = pygame.sprite.Group()
shield_list = pygame.sprite.Group()
trench_list = pygame.sprite.Group()
BHIT = pygame.sprite.Group()
SHIT = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, name):
#To make this work with Python 3.x, just change out the 3
#super_init calls with the commented out versions.
        super(Block, self).__init__()
#        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.name = name

class Shield(pygame.sprite.Sprite):
    def __init__(self, color, width, height, name):
        super(Shield, self).__init__()
#        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.name = name

class Trench(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Trench, self).__init__()
#        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

#color, width, height, reference name
player = Block(playercolour, 15, 15, 'p')
block1 = Block(OTHCOL, random.randrange(30,80), 15, '1')
shield1 = Shield(RED, 5,20,'1')
block2 = Block(OTHCOL, random.randrange(30,80), 15, '2')
shield2 = Shield(RED, 5,20,'2')
block3 = Block(OTHCOL, random.randrange(30,80), 15, '3')
shield3 = Shield(RED, 5,20,'3')
block4 = Block(OTHCOL, random.randrange(30,80), 15, '4')
shield4 = Shield(RED, 5,20,'4')
block5 = Block(OTHCOL, random.randrange(30,80), 15, '5')
shield5 = Shield(RED, 5,20,'5')
block6 = Block(OTHCOL, random.randrange(30,80), 15, '6')
shield6 = Shield(RED, 5,20,'6')
block7 = Block(OTHCOL, random.randrange(30,80), 15, '7')
shield7 = Shield(RED, 5,20,'7')
trench1 = Trench(OTHCOL, screen_width, 2)
trench2 = Trench(OTHCOL, screen_width, 2)

screen = pygame.display.set_mode((screen_width,screen_height)) #SUBJ NUM ENTRY CALL
pygame.display.set_caption('Trenches')

#Setting up lists for log file
L1 = ["Subject#"]
L2 = ["Block"]
L3 = ["Trial#"]
L4 = ["Score"]
L5 = ["Direction"]
B1 = ["Target1"]
B2 = ["Target2"]
B3 = ["Target3"]
B4 = ["Target4"]
B5 = ["Target5"]
B6 = ["Target6"]
B7 = ["Target7"]
S1 = ["Shield1"]
S2 = ["Shield2"]
S3 = ["Shield3"]
S4 = ["Shield4"]
S5 = ["Shield5"]
S6 = ["Shield6"]
S7 = ["Shield7"]
R1 = ["Subject#"]
R2 = ["Block"]
R3 = ["Trial#"]
R4 = ["Passage"]
R5 = ["ReadingTime"]
A1 = ["Block"]
A2 = ["Answer"]

#Draws the arena the game will be played in. 
def drawArena():
    DISPLAYSURF.fill(BLACK)
    pygame.draw.rect(DISPLAYSURF, OTHCOL, ((0,0),(screen_width,screen_height)), LINETHICKNESS*2-1)
			
def updateBlockWidths():
    block1 = Block(OTHCOL, random.randrange(30,70), 15, '1')
    block2 = Block(OTHCOL, random.randrange(30,70), 15, '2')
    block3 = Block(OTHCOL, random.randrange(30,70), 15, '3')
    block4 = Block(OTHCOL, random.randrange(30,70), 15, '4')
    block5 = Block(OTHCOL, random.randrange(30,70), 15, '5')
    block6 = Block(OTHCOL, random.randrange(30,70), 15, '6')
    block7 = Block(OTHCOL, random.randrange(30,70), 15, '7')

    block_list.add(block1, block2, block3, block4, block5, block6, block7)
    shield_list.add(shield1, shield2, shield3, shield4, shield5, shield6, shield7)
    trench_list.add(trench1, trench2)

    block1.rect.x = random.randrange(50,80)
    shield1.rect.x = (block1.rect.x)+(block1.rect.width * .35)
    block2.rect.x = random.randrange(155,185)
    shield2.rect.x = (block2.rect.x)+(block2.rect.width * .35)
    block3.rect.x = random.randrange(260,290)
    shield3.rect.x = (block3.rect.x)+(block3.rect.width * .35)
    block4.rect.x = random.randrange(365,395)
    shield4.rect.x = (block4.rect.x)+(block4.rect.width * .35)
    block5.rect.x = random.randrange(470,500)
    shield5.rect.x = (block5.rect.x)+(block5.rect.width * .35)
    block6.rect.x = random.randrange(575,605)
    shield6.rect.x = (block6.rect.x)+(block6.rect.width * .35)
    block7.rect.x = random.randrange(680,710)
    shield7.rect.x = (block7.rect.x)+(block7.rect.width * .35)

    trench1.rect.x = 0
    trench2.rect.x = 0

    block1.rect.y = random.randrange(50,screen_height - 50)
    block2.rect.y = block1.rect.y
    block3.rect.y = block1.rect.y
    block4.rect.y = block1.rect.y
    block5.rect.y = block1.rect.y
    block6.rect.y = block1.rect.y
    block7.rect.y = block1.rect.y

    shield1.rect.y = block1.rect.y - 3
    shield2.rect.y = block1.rect.y - 3
    shield3.rect.y = block1.rect.y - 3
    shield4.rect.y = block1.rect.y - 3
    shield5.rect.y = block1.rect.y - 3
    shield6.rect.y = block1.rect.y - 3
    shield7.rect.y = block1.rect.y - 3

    trench1.rect.y = block1.rect.y + 40
    trench2.rect.y = block1.rect.y - 30

    block_list.update(block1, block2, block3, block4, block5, block6, block7)
    shield_list.update(shield1, shield2, shield3, shield4, shield5, shield6, shield7)
    trench_list.update(trench1, trench2)

def drawSprites(trialnum, L1, L2, L3, L4, L5, B1, B2, S1, S2, BHIT, SHIT):
    block_list.draw(DISPLAYSURF)
    shield_list.draw(DISPLAYSURF)

def drawPlayer(player, trialnum, L1, L2, L3, L4, L5, B1, B2, S1, S2, BHIT, SHIT):
    player.rect.y = trench1.rect.y -40
    pygame.draw.rect(DISPLAYSURF, playercolour, player)
    drawSprites(trialnum, L1, L2, L3, L4, L5, B1, B2, S1, S2, BHIT, SHIT)

def movePlayer(player, direction):
    if direction == 1:
        player.rect.x += 2# (1 + randspeed)
    elif direction == 2:
        player.rect.x -= 2# (1 + randspeed)
    return player

def checkReachedEnd(player, trialnum, blockend, gametimer, blocknum, score, direction, L1, L2, L3, L4, L5, B1, B2, B3, B4, B5, B6, B7, S1, S2, S3, S4, S5, S6, S7, BHIT, SHIT):
    if (direction == 1 and player.rect.right >= (screen_width - LINETHICKNESS)) or (direction == 2 and player.rect.left <= LINETHICKNESS):
        eyetracker.stop_recording()
        if direction == 1:
            player.rect.x = LINETHICKNESS
        if direction == 2:
            player.rect.x = (screen_width - LINETHICKNESS)
#        targets_missed = [''.join(str(i.name) for i in block_list)]
        targets_hit = (''.join(str(i.name) for i in BHIT))
#        avoids_missed = [''.join(str(i.name) for i in shield_list)]
        avoids_hit = (''.join(str(i.name) for i in SHIT))
        #Logs "False" or "True" for whether each target/avoid was hit.
        B1 += ["1" in targets_hit]
        B2 += ["2" in targets_hit]
        B3 += ["3" in targets_hit]
        B4 += ["4" in targets_hit]
        B5 += ["5" in targets_hit]
        B6 += ["6" in targets_hit]
        B7 += ["7" in targets_hit]
        S1 += ["1" in avoids_hit]
        S2 += ["2" in avoids_hit]
        S3 += ["3" in avoids_hit]
        S4 += ["4" in avoids_hit]
        S5 += ["5" in avoids_hit]
        S6 += ["6" in avoids_hit]
        S7 += ["7" in avoids_hit]
        for i in block_list:
            i.kill()
        for i in shield_list:
            i.kill()
        for i in BHIT:
            i.kill()
        for i in SHIT:
            i.kill()
        L1 += [subnum]
        L2 += [blocknum]
        L3 += [trialnum]
        L4 += [score]
        if direction == 1:
          L5 += ["RIGHT"]
        if direction == 2:
          L5 += ["LEFT"]
        if time.clock()-gametimer >= GAMESESSDUR:
            blockend=1
            return player, trialnum, blockend, gametimer
        updateBlockWidths()
        trialnum += 1
        return player, trialnum, blockend, gametimer
    else: return player, trialnum, blockend, gametimer

def checkPointScored(player, score, trialnum, L1, L2, L3, L4, L5, B1, B2, S1, S2, BHIT, SHIT):
  if playercolour==OTHCOL:
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    shields_hit_list = pygame.sprite.spritecollide(player, shield_list, True)
#    for sprite in pygame.sprite.spritecollide(player, block_list, True):
    for sprite in blocks_hit_list:
      score += 1
      BHIT.add(sprite)
      print "Block sprite hit:", sprite.name, "--", len(BHIT), "Total"
    for sprite in shields_hit_list:
      score -= 2
      SHIT.add(sprite)
      print "Shield sprite hit:", sprite.name, "--", len(SHIT), "Total"

    return score
  else: return score

#Display block, trial, and score information.  Do not use during experiment.
'''
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
'''

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
	for row in zip(L1, L2, L3, L4, L5, B1, B2, B3, B4, B5, B6, B7, S1, S2, S3, S4, S5, S6, S7):
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
            eyetracker.stop_recording()
            qans = event.key - 48 #1 = 49, 4 = 52
            A1 += [blocknum]
            A2 += [qans]
            filename='70'
            print('%s key pressed, end reading portion' %(qans))
            if blocknum == RECALBLOCK and filename == '70':
               eyetracker.calibrate()
            return filename,t0,blocknum
        else: return filename,t0,blocknum
    if filename=='70':
      return filename,t0,blocknum

#ADD A COUNTDOWN BEFORE START OF FIRST TRIAL IN ANY BLOCK
def gameStartCountdown(starttimer, tcountdown, blockend, blocknum, filename):
	if tcountdown == 70:
#		print 'Setting tcountdown to current time plus 6 seconds.'
		tcountdown = time.clock()+6
	elif starttimer > 0:
#		print 'starttimer is %s' %(starttimer)
		starttimer = int(tcountdown-time.clock())
#		print 'tcountdown is %s' %(tcountdown)
#		print 'new starttimer is %s' %(starttimer)
		startSurf = BASICFONT.render('%s' %(starttimer), True, WHITE)
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
		filename="Instruc.png"
		gamebits(gametimer,blockend,blocknum,filename)
		return starttimer,tcountdown,blockend,blocknum,filename
	else:
		blockend=0
		tcountdown=70
		starttimer = 5		
		return starttimer,tcountdown,blockend,blocknum,filename
	return starttimer,tcountdown,blockend,blocknum,filename

#Main function
def gamebits(gametimer,blockend,blocknum,filename):
    global playercolour
    playercolour = OTHCOL
    clock = pygame.time.Clock()

    direction = DIREC
    if blocknum > BLOCKSTILSWITCH:
        if DIREC == 1:
            direction = 2
        if DIREC == 2:
            direction = 1

    score = 0
    trialnum = 1
    player = Block(playercolour, 15, 15, 'p')
#    moveDown = False
#    moveUp = False

    if direction == 1:
        player.rect.x = LINETHICKNESS + 5
    if direction == 2:
        player.rect.x = (screen_width - LINETHICKNESS - 5)

    drawArena()
    updateBlockWidths()
    drawSprites(trialnum, L1, L2, L3, L4, L5, B1, B2, S1, S2, BHIT, SHIT)
    drawPlayer(player, trialnum, L1, L2, L3, L4, L5, B1, B2, S1, S2, BHIT, SHIT)

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
#                if event.key == K_UP or event.key == ord('w'):
#                    moveDown = False
#                    moveUp = True
#                if event.key == K_DOWN or event.key == ord('s'):
#                    moveUp = False
#                    moveDown = True
                if event.key == K_SPACE:
                    playercolour=RED
            if event.type == KEYUP:
                if event.key == K_BACKQUOTE: #quit if tilde key pressed
                    quitwrite()
                    pygame.quit()
                    sys.exit()
#                if event.key == K_UP or event.key == ord('w'):
#                    moveUp = False
#                if event.key == K_DOWN or event.key == ord('s'):
#                    moveDown = False
                if event.key == K_SPACE:
                    playercolour=OTHCOL
        if blockend == 1:
#            blocknum += 1
            filename="Instruc.png"
            return gametimer,blockend,blocknum,filename

        drawArena()
        drawPlayer(player, trialnum, L1, L2, L3, L4, L5, B1, B2, S1, S2, BHIT, SHIT)

        player = movePlayer(player, direction)
        score = checkPointScored(player, score, trialnum, L1, L2, L3, L4, L5, B1, B2, S1, S2, BHIT, SHIT)
        player, trialnum, blockend, gametimer = checkReachedEnd(player, trialnum, blockend, gametimer, blocknum, score, direction, L1, L2, L3, L4, L5, B1, B2, B3, B4, B5, B6, B7, S1, S2, S3, S4, S5, S6, S7, BHIT, SHIT)


#        displayScore(score)
#        displayTrialNum(trialnum)
#        displayBlockNum(blocknum)

#        if moveDown:
#            player.rect.y += 2
#        if moveUp:
#            player.rect.y -= 2

        pygame.display.update()
        clock.tick(FPS)
##############

def main():
    pygame.init()
    pygame.mouse.set_visible(0) # make cursor invisible
#    screen = pygame.display.set_mode((screen_width,screen_height)) #SUBJ NUM ENTRY CALL
    pygame.display.set_caption('Trenches')
    blocknum=0

    t0=0
    filename = 'Instruc.png'

    global direction
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
    global BHIT
    BHIT = pygame.sprite.Group()
    global SHIT
    SHIT = pygame.sprite.Group()
    blockend = 0
    drawArena()

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                quitwrite()
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
