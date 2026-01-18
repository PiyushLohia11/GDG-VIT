import tkinter as tk
import turtle
def expand_string(axiom, rules, iterations):
    current_string = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current_string:
            if char in rules:
                next_string += rules[char]
            else:
                next_string += char
        current_string = next_string
    return current_string

def draw_l_system(t, instructions, angle, distance):
    stack = [] # Storage for saving turtle position/heading
    colors = ["#FF5733", "#C70039", "#900C3F", "#581845", "#1C2833"]
    color_index = 0

    for char in instructions:
        if char == 'F':
            t.forward(distance)
        elif char == '+':
            t.right(angle)
        elif char == '-':
            t.left(angle)
        
        elif char == '[':
            state = (t.position(), t.heading())
            stack.append(state)
        elif char == ']':
            if stack:
                position, heading = stack.pop()
                t.penup()
                t.goto(position)
                t.setheading(heading)
                t.pendown()
                t.pencolor(colors[color_index % len(colors)])
                color_index += 1
