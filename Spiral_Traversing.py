# Spiral_Traversing
import random
import turtle
turtle.bgcolor("black")
pen = turtle.Turtle()
width = 5
height = 7
pen.penup()
dot_distance = 25
pen.setpos(-250,250)
pen.color("white")
color_list = ["blue","red","green","yellow","orange","violet"]


def spiral(m,n):              # m is no.of rows, n is no.of cols; a is matrix.
  x = 0
  y = 0                       # x is starting index of row, y is starting index of col
  f = 0

  while x<m and y<n :
    if(f==1):
      pen.right(90)
                              # printing first row from remaining rows
    pen.color(color_list[random.randint(0,5)])
    for i in range(y,n):
      pen.dot()
      pen.forward(dot_distance)
      #print(a[x][i], end=" ")
                              # printing last col from remaining cols leaving first one in col
    f = 1
    x = x + 1
    pen.right(90)
    pen.color(color_list[random.randint(0,5)])
    for j in range(x,m):
      pen.dot()
      pen.forward(dot_distance)
      #print(a[j][n-1], end=" ")

                              # printing last row from remaining rows leaving last one in row
    n = n - 1
    pen.right(90)
    pen.color(color_list[random.randint(0,5)])
    if x < m :
      for i in range(n-1,y-1,-1):
        pen.dot()
        pen.forward(dot_distance)
        #print(a[m-1][i], end=" ")
                              # printing first col from remaining cols leaving last one in col
    m = m - 1
    pen.right(90)
    pen.color(color_list[random.randint(0,5)])
    if y < n :
      for j in range(m-1,x-1,-1):
        pen.dot()
        pen.forward(dot_distance)
        #print(a[j][y], end=" ")
      y = y + 1

spiral(20,20)
turtle.done()