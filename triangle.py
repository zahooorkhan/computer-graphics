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
    glBegin(GL_TRIANGLES)
    glVertex2f(9.0,0.0)
    glVertex2f(-1.0,0.0)  
    glVertex2f(5.0,5.0)  
    glEnd()
    glFlush()#it try to display the screen
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(600,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("OpenGl Program")
    glutDisplayFunc(display)
    init()
    glutMainLoop()
main()