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

def run_render():
    axiom = entry_axiom.get()
    rule_str = entry_rule.get() # Format: F:F+F-F
    try:
        angle = float(entry_angle.get())
        iters = int(entry_iter.get())
    except ValueError:
        print("Please enter valid numbers for Angle and Iterations")
        return

    rules = {}
    if ":" in rule_str:
        key, value = rule_str.split(":")
        rules[key.strip()] = value.strip()

    final_string = expand_string(axiom, rules, iters)
    print(f"Generated String Length: {len(final_string)}")

    screen = t_screen 
    screen.tracer(0, 0) 
    my_turtle.reset()
    my_turtle.hideturtle()
    my_turtle.speed(0)
    my_turtle.pensize(1)

    my_turtle.penup()
    my_turtle.goto(0, -200)
    my_turtle.setheading(90) # Face Up
    my_turtle.pendown()

    step_size = 200 / (iters * 2) if iters > 0 else 50
    draw_l_system(my_turtle, final_string, angle, step_size)

    screen.update() 

root = tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("900x700")

frame_inputs = tk.Frame(root, bg="#f0f0f0", pady=10)
frame_inputs.pack(side=tk.TOP, fill=tk.X)

def create_input(parent, label_text, default_val, col):
    tk.Label(parent, text=label_text, bg="#f0f0f0").grid(row=0, column=col, padx=5)
    entry = tk.Entry(parent, width=15)
    entry.insert(0, default_val)
    entry.grid(row=1, column=col, padx=5)
    return entry

entry_axiom = create_input(frame_inputs, "Axiom (Start)", "F", 0)
entry_rule = create_input(frame_inputs, "Rule (Symbol:New)", "F:F[+F]F[-F]F", 1)
entry_angle = create_input(frame_inputs, "Angle", "25.7", 2)
entry_iter = create_input(frame_inputs, "Iterations", "4", 3)
