"""
    This program allows the user to draw a flower pattern based on their input

    author : Siphosethu Shumani

    Date : 2021/12/28
"""

import turtle


""" input """

number_of_petals = int(input("Enter the number of petals (must be an even number): "))

stem_length = int(input("Enter the length of stem: "))

petal_type = input("Enter the petal type (triangle, square, or pentagon): ")

side_length = int(input("Enter the length of side: "))  

stem_colour = input("Enter the stem colour: ")

first_petal_colour = input("Enter the first petal colour: ")

second_petal_colour = input("Enter the second  petal colour: ")


""" Process and Output  """

turn_degree = 360/number_of_petals  

petal_drawer = turtle

petal_drawer.shape("turtle")

petal_drawer.left(90)

if petal_type.lower() == "triangle":

    petal_drawer.color(stem_colour)
    petal_drawer.forward(stem_length)
    
    for petal_number in range(number_of_petals):

        petal_drawer.left(30)
       
       # alternating triangle colours 
        if petal_number%2 != 0:
            petal_drawer.color(first_petal_colour)

            # drawing the triangle
            for line in range(3):
                petal_drawer.forward(side_length)
                petal_drawer.right(120)
            petal_drawer.right(30)

        else:
            petal_drawer.color(second_petal_colour)

            # drawing the triangle
            for line in range(3):
                petal_drawer.forward(side_length)
                petal_drawer.right(120)
            petal_drawer.right(30)
            
        petal_drawer.color(stem_colour)
        petal_drawer.backward(stem_length)
        petal_drawer.right(turn_degree)
        petal_drawer.forward(stem_length)

elif petal_type.lower() == "square":
        
    petal_drawer.color(stem_colour)
    petal_drawer.forward(stem_length)
    
    for petal_number in range(number_of_petals):

        petal_drawer.left(90)
       
       # alternating Square colours 
        if petal_number%2 != 0:
            petal_drawer.color(first_petal_colour)

            # drawing the Square
            petal_drawer.forward(side_length/2)
            for line in range(4):
                petal_drawer.right(90)
                petal_drawer.forward(side_length)

            petal_drawer.backward(side_length/2)
            petal_drawer.right(90)

        else:
            petal_drawer.color(second_petal_colour)

            # drawing the Square
            petal_drawer.forward(side_length/2)
            for line in range(4):
                petal_drawer.right(90)
                petal_drawer.forward(side_length)

            petal_drawer.backward(side_length/2)
            petal_drawer.right(90)
            
        petal_drawer.color(stem_colour)
        petal_drawer.backward(stem_length)
        petal_drawer.right(turn_degree)
        petal_drawer.forward(stem_length)

else:

    petal_drawer.color(stem_colour)
    petal_drawer.forward(stem_length)
    
    for petal_number in range(number_of_petals):

        petal_drawer.left(54)
       
       # alternating Pentagon colours 
        if petal_number%2 != 0:
            petal_drawer.color(first_petal_colour)

            # drawing the Pentagon
            for line in range(5):
                petal_drawer.forward(side_length)
                petal_drawer.right(72)

            petal_drawer.right(54)
            
        else:
            petal_drawer.color(second_petal_colour)

            # drawing the Pentagon
            for line in range(5):
                petal_drawer.forward(side_length)
                petal_drawer.right(72)

            petal_drawer.right(54)

        petal_drawer.color(stem_colour)
        petal_drawer.backward(stem_length)
        petal_drawer.right(turn_degree)
        petal_drawer.forward(stem_length)
    
petal_drawer.backward(stem_length)

petal_drawer.exitonclick()

