from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawLine():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_LINE_STRIP)
    # here we can use the for loop to draw the line on the basis of points
    for i in range(20):
        glVertex2f(0.1 + i/50.0, 0.1)
    # glBegin(GL_LINES)
    # glVertex2f(-0.5, 0.0)
    # glVertex2f(0.5, 0.0)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(950, 950)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Line")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glutDisplayFunc(drawLine)
    glutMainLoop()

if __name__ == '__main__':
    main()
