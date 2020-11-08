# WHACK 2020
# Ballot Race: Nevada Edition
# Anna, Alyssa, Amanda

import sys, pygame, random, time

# sloth is 150px x 198px

##################### Intro & Info ######################

def intro():
    cover = pygame.image.load("cover.png")
    coverRect = cover.get_rect()
    screen.blit(cover, coverRect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

def infoPage():
    info = pygame.image.load("info.png")
    infoRect = info.get_rect()
    screen.blit(info, infoRect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

def instructions():
    howTo = pygame.image.load("how-to.png")
    howToRect = howTo.get_rect()
    screen.blit(howTo, howToRect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

##################### Game play #######################

def gamePlay(score):
    
    # SLOTH
    person = pygame.image.load("person.png")
    player = person.get_rect()
    player = player.move(400, 320)

    # BALLOT
    ballot = pygame.image.load("ballot.png")
    ballotRect = ballot.get_rect().move(0, -50)
    ballotRect2 = ballot.get_rect().move(850, -300)
    ballotRect3 = ballot.get_rect().move(300,-400)

    # MAGA HAT
    hat = pygame.image.load("magaHat.png")
    hatRect = hat.get_rect().move(500, -200)

    # PROTESTERS
    protest = pygame.image.load("protest.jpeg")
    protestRect = protest.get_rect().move(800, -320)

    # TRUMP
    trump = pygame.image.load("trump.png")
    trumpRect = trump.get_rect().move(670, -100)
    trumpRect2 = trump.get_rect().move(300, -500)

    while True:
        fallingItems = [ballotRect, ballotRect2, ballotRect3,
                    hatRect, protestRect, trumpRect, trumpRect2]

        # when item hits the bottom of the screen, go back to the top
        # and start from random horizontal position 
        for item in fallingItems:
            if item.top > 500:
                item.top = -100
                item.left = random.randint(0, 1000 - item.width)

        # animate the falling items
        ballotRect = ballotRect.move(0, 1)
        ballotRect2 = ballotRect2.move(0, 1)
        ballotRect3 = ballotRect3.move(0, 1)

        hatRect = hatRect.move(0, 1)

        protestRect = protestRect.move(0, 1)
        
        trumpRect = trumpRect.move(0, 1)
        trumpRect2 = trumpRect2.move(0,1)

        screen.fill(white)

        # display the items
        screen.blit(person, player)
        
        screen.blit(ballot, ballotRect)
        screen.blit(ballot, ballotRect2)
        screen.blit(ballot, ballotRect3)
        
        screen.blit(hat, hatRect)
        
        screen.blit(protest, protestRect)
        
        screen.blit(trump, trumpRect)
        screen.blit(trump, trumpRect2)

        
        for event in pygame.event.get():
            # if the user presses the right key, move the person right
            if pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < width:
                print("pressed right")
                player = player.move(100, 0)
                screen.blit(person, player)
            if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
                print("pressed left")
                player = player.move(-100, 0)
                screen.blit(person, player)

        obstacles = [hatRect, protestRect, trumpRect, trumpRect2]
        collisions = player.collidelist(obstacles)
        # returns index of the first collision found. If no collisions are found, -1 is returned.
        if collisions >= 0:
            print('collision')
            return score

        ballots = [ballotRect, ballotRect2, ballotRect3]
        newPoint = player.collidelist(fallingItems)
        if newPoint >=0: 
            score += 1
            newPoint = []
        
        # display the score
        gameFont = pygame.font.SysFont('arialroundedbold', 25)
        textSurface = gameFont.render(" Score: " + str(score) + " ballots", False, (0, 0, 255))
        textRect = textSurface.get_rect
        screen.blit(textSurface, (0, 0))

            
        pygame.display.flip()

##################### Game over ############################
        
def gameOver(finalScore):
    screen.fill(white)
    
    gameFont = pygame.font.SysFont('arialroundedbold', 25)
    overSurface = gameFont.render("GAME OVER! ", False, (0, 0, 255))
    screen.blit(overSurface, (screen.get_width() / 2 - 200, screen.get_height() / 2 - 100))

    scoreSurface = gameFont.render("You counted " + str(finalScore) + " ballots", False, (0, 0, 255))
    screen.blit(scoreSurface, (screen.get_width() / 2 - 200, screen.get_height() / 2 - 60))
            
    pygame.display.flip()


pygame.init()

size = width, height = 1000, 500
screen = pygame.display.set_mode(size)
white = (255, 255, 255)

screen.fill(white)
pygame.display.set_caption("Ballot Race")

intro()
infoPage()
instructions()
gameOver(gamePlay(0))

