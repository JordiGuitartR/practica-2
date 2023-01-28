# Import a library of functions called 'pygame'
import pygame
import os
import sys

def drawSquare(screen,color):
    # Draw a 6x5 table on the screen
    i=80
    j=440
    j2=382
    wide=5
    inc=60
    for k in range(0,7):
        pygame.draw.line(screen, color, [i, i+inc*k], [j2,i+inc*k], wide)
        
    for k in range(0,6):
        pygame.draw.line(screen, color, [i+inc*k,i], [i+inc*k,j], wide)
        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.

def drawValues(t,screen):
    GREEN = (  0, 255,   0)
    GREY = (100,100,100)
    ORANGE = (255,165,0)
     
#    fontV = pygame.font.Font(pygame.font.match_font('arial'),20)
    fontV = pygame.font.Font('freesansbold.ttf', 24) 
    i=100
    inc=60
    for r in range(0,6):
        j=102
        for c in range(0,5):
            if t[r][c][1]==0:
                color=GREY
            elif t[r][c][1]==1:
                color=ORANGE
            elif t[r][c][1]==2:
                color=GREEN
            else:
                print("Error en la taula")
                pygame.quit()
                sys.exit(0)
            text=fontV.render(t[r][c][0],True,color)
            screen.blit(text, (j,i))
            j=j+inc
        i=i+inc
        
def draw(tauler):
    # set the pygame window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (900,120)
    # Initialize the game engine
    pygame.init()
     
    # Define the colors we will use in RGB format
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    RED =   (255,   0,   0)
   
    # Set the height and width of the screen
    size = [460, 520]
    screen = pygame.display.set_mode(size,pygame.NOFRAME)
    
    pygame.display.set_caption("Wordle Català")
    
    # Clear the screen and set the screen background
    screen.fill(WHITE)


    # create a font object. 
    # 1st parameter is the font file which is present in pygame. 
    # 2nd parameter is size of the font 
    font = pygame.font.Font('freesansbold.ttf', 18) 
      
    # create a text and draw. 
    #text = font.render('   1          2          3 ', True, BLACK, WHITE)   
    #screen.blit(text, (88,50))
    '''
    text = font.render(' A     B     C      D     E      F      G     H      I ', False, BLACK, WHITE) 
    text = pygame.transform.rotate(text,270)
    screen.blit(text, (50,90))
    '''
    #lind=list('ABC')
    #inc=60
    #for i in range(0,len(lind)):
    #    text = font.render(lind[i],True,BLACK,WHITE)
    #    screen.blit(text,(55,100+i*inc))
    
    drawSquare(screen,BLACK)

    screen.unlock()
    drawValues(tauler,screen)
            
    pygame.display.flip()
    #pygame.quit()
    
'''
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    
 
# Be IDLE friendly
pygame.quit()

'''
if __name__=="__main__":
    t=[[('X',0)]*5 for i in range(0,6)]
    draw(t)
