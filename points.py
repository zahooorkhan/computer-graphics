from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawPoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Points")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glutDisplayFunc(drawPoints)
    glutMainLoop()

if __name__ == '__main__':
    main()
