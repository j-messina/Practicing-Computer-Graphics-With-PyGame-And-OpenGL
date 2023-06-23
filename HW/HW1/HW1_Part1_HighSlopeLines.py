import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
blue  = pygame.Color(0, 0, 255)

start_range = -500
end_range = 500
the_range = abs(end_range - start_range)

xoriginoffset = int(screen.get_width() / 2)
yoriginoffset = int(screen.get_height() / 2)
def draw_line_old(slope, y_intercept):
    for x in range(start_range, end_range):
        y = int(slope * x + y_intercept)
        screen.set_at((x + xoriginoffset, y + yoriginoffset), white)
def draw_line_low(slope, y_intercept):
    draw_line_old(slope, y_intercept)

def draw_line_high(slope, x_intercept):
    for y in range(start_range, end_range):
        x = int(slope * y + x_intercept)
        screen.set_at((x + xoriginoffset, y + yoriginoffset), white)

def draw_line(slope, y_intercept):
    if x <= 1:
        draw_line_low(slope, y_intercept)
    else:
        x_intercept = -1 * y_intercept / slope
        draw_line_high(1/slope, x_intercept)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # x axis
    for x in range(-500, 500):
        screen.set_at((x + xoriginoffset, yoriginoffset), green)
    # y axis
    for y in range(-400, 400):
        screen.set_at((xoriginoffset, y + yoriginoffset), green)

    # steep line with visible dotted gaps
    draw_line_old(15, 0)

    # draw with draw_line_low aka draw_line_old
    draw_line_low(1/4, 0)

    # draw with draw_line_high
    draw_line(6, 0)

    pygame.display.update()
pygame.quit()
