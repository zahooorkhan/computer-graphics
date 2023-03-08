from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
def init():
    glClearColor(0 ,1, 0, 1.0)
    gluOrtho2D(-10.0,10.0,-10.0,10.0)
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(16)
    glLineWidth(4)
    glBegin(GL_POINT)
    x1 = 10 ,
    y1 = 10 ,
    x2 = 40 ,
    y2 = 30 
    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    b = y1 - mx1
    if m < 1:
        step = dx
        for x in range(x+1 , step):
            y = m * x + b
            glVertex2f(x,y)
    else:
        step = dy
        for y in range(y+1 , step):
            x = (y-b)/m
            glVertex2f(x,y)     
    glEnd()
    glFlush()#it try to display the screen
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(700,700)
    glutInitWindowPosition(100,100)
    glutCreateWindow("OpenGl Program")
    glutDisplayFunc(display)
    init()
    glutMainLoop()
main()