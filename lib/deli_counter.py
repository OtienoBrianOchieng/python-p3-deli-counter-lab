

def line(katz_deli):
    if len(katz_deli) > 0:
        queue = []
        for index, name in enumerate(katz_deli, start= 1):
            updated_name = f"{name} you are position {index}"
            queue.append(updated_name)
        print (queue)
    else:
         print ("The line is currently empty.")
    pass

def take_a_number(katz_deli, name):
    
        katz_deli.append(name)
        position = len(katz_deli)
        print(f"Welcome, {name}. You are number {position} in line.")

    

def now_serving(katz_deli):
    if not katz_deli:
         print ("There is nobody waiting to be served!")
    else:
         serving_person = katz_deli.pop(0)
         print (f"Currently serving {serving_person}.")
