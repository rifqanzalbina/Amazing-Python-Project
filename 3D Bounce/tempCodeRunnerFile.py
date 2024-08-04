import pygame
from pygame.math import Vector3
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

# Set up the 3D perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Ball properties
ball_pos = Vector3(0, 0, 0)
ball_velocity = Vector3(0.05, 0.05, 0.05)
ball_radius = 0.5
ball_color = (1, 0, 1)  # Initial color: red

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update ball position
    ball_pos += ball_velocity

    # Check for collisions with walls
    if abs(ball_pos.x) > 2 - ball_radius:
        ball_velocity.x *= -1
        ball_color = (0, 2, 0)  # Change color to green on collision
    if abs(ball_pos.y) > 2 - ball_radius:
        ball_velocity.y *= -1
        ball_color = (0, 0, 1)  # Change color to blue on collision
    if abs(ball_pos.z) > 2 - ball_radius:
        ball_velocity.z *= -1
        ball_color = (1, 1, 0)  # Change color to yellow on collision

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the ball
    glPushMatrix()
    glTranslatef(ball_pos.x, ball_pos.y, ball_pos.z)
    glColor3f(*ball_color)  # Set the ball color
    quad = gluNewQuadric()
    gluSphere(quad, ball_radius, 32, 32)
    glPopMatrix()

    # Update the display
    pygame.display.flip()
    clock.tick(60)
