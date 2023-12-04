# lib/deli_counter.py

def line(deli_line):
    if not deli_line:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently: " + ", ".join(f"{index + 1}. {name}" for index, name in enumerate(deli_line))
        print(line_str)

def take_a_number(deli_line, name):
    deli_line.append(name)
    position = len(deli_line)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving = deli_line.pop(0)
        print(f"Currently serving {serving}.")

katz_deli = []

take_a_number(katz_deli, "Ada")  
take_a_number(katz_deli, "Grace")  
take_a_number(katz_deli, "Kent")  

line(katz_deli)  

now_serving(katz_deli)  

line(katz_deli)  

take_a_number(katz_deli, "Matz")  

line(katz_deli)  

now_serving(katz_deli)  

line(katz_deli)  
