# # def draw_circle(radius):
# #     for y in range(-radius, radius + 1):
# #         for x in range(-radius, radius + 1):
# #             if x**2 + y**2 <= radius**2:
# #                 print("*", end=" ")
# #             else:
# #                 print(" ", end=" ")
# #         print()

# # radius = 10
# # draw_circle(radius)
# def draw_rectangle(width, height):
#     for y in range(height):
#         for x in range(width):
#             if y == 0 or y == height - 1 or x == 0 or x == width - 1:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()

# width = 10
# height = 5
# draw_rectangle(width, height)

# import turtle

# def draw_circle(radius):
#     turtle.speed(1)
#     turtle.circle(radius)
#     turtle.done()

# radius = 50
# draw_circle(radius)
# import turtle

# def draw_rectangle(width, height):
#     turtle.speed(1)
#     turtle.penup()
#     turtle.goto(-width/2, -height/2)  # Move to the bottom-left corner of the rectangle
#     turtle.pendown()
    
#     for _ in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)

#     turtle.done()

# width = 200
# height = 100
# draw_rectangle(width, height)

# import turtle

# def draw_rectangle(width, height):
#     turtle.speed(1)
#     turtle.penup()
#     turtle.goto(-width/2, -height/2)  # Move to the bottom-left corner of the rectangle
#     turtle.pendown()
    
#     for _ in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)

#     turtle.done()

# width = 200
# height = 100
# draw_rectangle(width, height)

import turtle

# def draw_triangle(side_length):
#     turtle.speed(1)
#     turtle.penup()
#     turtle.goto(-side_length/2, side_length)  # Move to the bottom-left corner of the rectangle
#     turtle.pendown()
    
#     for _ in range(3):
#         turtle.forward(side_length)
#         turtle.left(120)

#     turtle.done()

# side_length = 200
# draw_triangle(side_length)
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the radius of the circle
radius = 100

# Draw the circle
t.circle(radius)

# Keep the window open until it's manually closed
turtle.done()




