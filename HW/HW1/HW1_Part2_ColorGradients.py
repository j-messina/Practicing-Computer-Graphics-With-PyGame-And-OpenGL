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

def interpolate(start_color, end_color, progress_value):
    interp_color = []
    for x in range(0,3):
        interp_color.append(min(255, int(progress_value * max(0, end_color[x]-start_color[x])) + start_color[x]))
        # print("end_color[{}] = {}".format(x, end_color[x]))
        # print("start_color[{}] = {}".format(x, start_color[x]))
        # print("end_color[{}] - start_color[{}] = {} - {} = {}".format(x, x, end_color[x], start_color[x], end_color[x]-start_color[x]))
        # print("max(0, {}) = {}".format(end_color[x]-start_color[x], max(0,end_color[x]-start_color[x])))
        # print("progress_value =", progress_value)
        # print("progress_value * max(0, end_color[{0}] - start_color[{0}] = {1} * max(0, {2}) = {3}".format(x, progress_value, end_color[x]-start_color[x], progress_value * max(0,end_color[x]-start_color[x])))
        # print("interp_color =", interp_color)
        # print()
    return tuple(interp_color)
def draw_line_low(slope, y_intercept, start_color, end_color):
    for x in range(start_range, end_range):
        progress_value = (x - start_range) / (end_range-start_range)
        interp_color = interpolate(start_color, end_color, progress_value)
        y = int(slope * x + y_intercept)
        screen.set_at((x + xoriginoffset, y + yoriginoffset), interp_color)

def draw_line_high(slope, x_intercept, start_color, end_color):
    for y in range(start_range, end_range):
        x = int(slope * y + x_intercept)
        screen.set_at((x + xoriginoffset, y + yoriginoffset), white)

def draw_line(slope, y_intercept, start_color, end_color):
    if x <= 1:
        draw_line_low(slope, y_intercept, start_color, end_color)
    else:
        x_intercept = -1 * y_intercept / slope
        draw_line_high(1/slope, x_intercept, start_color, end_color)

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

    # draw draw_line_low with interpolated color gradient from green to blue
    draw_line_low(1/4, 0, green, blue)

    pygame.display.update()
pygame.quit()
