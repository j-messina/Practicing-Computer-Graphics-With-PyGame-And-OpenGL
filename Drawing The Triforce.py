import pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
done = False
white = pygame.Color(255,255,255)
yellow = pygame.Color(255,215,0)
offset = 86.6
list_of_points = [(100,100), (200,100), (200,200)]
list_of_points_triforce = [(150,300+offset), (200,300), (250, 300-offset), (300,300), (350,300+offset), (250,300+offset), (300,300), (200,300), (250,300+offset)]
def build_triforce_contiguous():
    # testing lines function
    # this builds the triforce symbol using contiguous points
    pygame.draw.lines(screen, white, True, list_of_points_triforce)

def build_triforce_linebyline():
    # middle triangle
    pygame.draw.line(screen, white, (400, 400), (500, 400))
    pygame.draw.line(screen, white, (400, 400), (450, 486.6))
    pygame.draw.line(screen, white, (450, 486.6), (500, 400))

    # upper triangle
    pygame.draw.line(screen, yellow, (400, 400), (450, 400 - offset))
    pygame.draw.line(screen, yellow, (450, 400 - offset), (500, 400))
    pygame.draw.line(screen, yellow, (400, 399), (500, 399))  # borders middle triangle edge

    # left triangle
    pygame.draw.line(screen, yellow, (400, 400), (350, 400 + offset))
    pygame.draw.line(screen, yellow, (350, 400 + offset), (450, 400 + offset))
    pygame.draw.line(screen, yellow, (400, 401), (450, 400 + offset - 1))  # borders middle triangle edge

    # right triangle
    pygame.draw.line(screen, yellow, (500, 400), (550, 400 + offset))
    pygame.draw.line(screen, yellow, (450, 400 + offset), (550, 400 + offset))
    pygame.draw.line(screen, yellow, (500, 401), (450, 400 + offset + 1))  # borders middle triangle edge

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  build_triforce_contiguous()
  build_triforce_linebyline()


  pygame.display.update()
pygame.quit()