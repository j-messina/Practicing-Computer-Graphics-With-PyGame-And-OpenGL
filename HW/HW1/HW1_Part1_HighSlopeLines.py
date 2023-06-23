import pygame

# Create Pygame display window
pygame.init()
# screen_width = 1000
# screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

# Intialize some RGB color variables
white = pygame.Color(255, 255, 255)
red   = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue  = pygame.Color(0, 0, 255)

# Define range for drawing lines (will be centered to whatever relative origin we are using)
range_start = -500
range_end = 500
the_range = abs(range_end - range_start)

# Move our relative origin to approximately the middle of the display window
xoriginoffset = int(screen.get_width() / 2)
yoriginoffset = int(screen.get_height() / 2)
def draw_line_low(slope, y_intercept, color):
    for x in range(range_start, range_end):
        y = int(slope * x + y_intercept)
        screen.set_at((x + xoriginoffset, y + yoriginoffset), color)

def draw_line_high(slope, y_intercept, color):
    x_intercept = -1 * y_intercept / slope
    for y in range(range_start, range_end):
        x = int((1/slope) * y + x_intercept)
        screen.set_at((x + xoriginoffset, y + yoriginoffset), color)

def draw_line(slope, y_intercept, color):
    if abs(slope) <= 1:
        draw_line_low(slope, y_intercept, color)
    else:
        draw_line_high(slope, y_intercept, color)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # x axis
    for x in range(-500, 500):
        screen.set_at((x + xoriginoffset, yoriginoffset), white)
    # y axis
    for y in range(-400, 400):
        screen.set_at((xoriginoffset, y + yoriginoffset), white)

    gray = lambda x : (255-x, 255-x, 255-x)
    # (proof of concept) steep line with visible dotted gaps
    draw_line_low(5, -200, white)
    # draw with draw_line_low
    draw_line(1/4, -50, green)
    # draw with draw_line_high
    draw_line(5, 100, green)
    # draw midway slope
    # draw_line(1, 0, gray(125))

    pygame.display.update()
pygame.quit()
