import turtle

def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
        
def draw_sectioned_face(t, sides, length):
    # draw the outer polygon
    draw_polygon(t, sides, length)
    
    # move to the center of the polygon
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    # draw the hatch lines
    angle = 360 / sides
    num_hatch_lines = 10  # adjust the number of hatch lines as needed
    hatch_line_spacing = length / num_hatch_lines
    for i in range(sides):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(i * angle)
        for j in range(num_hatch_lines):
            t.forward(hatch_line_spacing)
            t.penup()
            t.forward(hatch_line_spacing)
            t.pendown()

# create the turtle and set its speed
t = turtle.Turtle()
t.speed('fastest')
# set the pen thickness
t.width(20)

# draw the letter M
t.penup()
t.goto(-200, 0)
t.pendown()
t.setheading(90)
t.forward(100)
t.right(135)
t.forward(70.71)
t.left(90)
t.forward(70.71)
t.right(135)
t.forward(100)

# add the empty spaces
t.penup()
t.goto(-135, 35)
t.pendown()
t.setheading(0)
t.forward(40)

t.penup()
t.goto(-85, 35)
t.pendown()
t.setheading(0)
t.forward(40)

"""
# draw the sectioned faces
# draw_sectioned_face(t, 4, 100)
# draw_sectioned_face(t, 5, 80)
# draw_sectioned_face(t, 6, 60)
t.penup()
t.goto(-200, 0)
t.pendown()
t.setheading(90)
t.forward(100)
t.right(135)
t.forward(70.71)
t.left(90)
t.forward(70.71)
t.right(135)
t.forward(100)
"""
# hide the turtle when finished
t.hideturtle()

# keep the turtle window open until closed manually
turtle.mainloop()
