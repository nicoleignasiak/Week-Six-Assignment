# Nicole Ignasiak
# Dr. Nuemann
# CIS 125 82B
# October 14, 2015

# Pre Conditions for Populate
    # That world is a list
    
# Post Conditions for Populate
    # World will contain random cells

def populate(petri_dish, h, w):
    import random
    for x in range(h):
        row = []
        for y in range(w):
            row.append(random.randint(0,1))
        petri_dish.append(row)
            
            
# Pre Condition for Display
    # World is populated
# Post Conditions for Display
    
def display(petri_dish, h, w):
    worldString = ""
    for x in range(h):
        for y in range(w):
            if petri_dish[x][y] == 1:
                worldString += "*"
            else:
                worldString += " "
        worldString += "\n"
    print(worldString)


def generation(petri_dish, h, w):
    new_world = []
    # fill this in
    
    # check each cell

    for x in range(h):
        row = []
        for y in range(w):
            row.append(0)
        new_world.append(row)
        
        
        # count the neighbors
    n = 0    
    for x in range(1,h-1): # the outside border cells wont be counted
        for y in range(1,w-1):
            n = petri_dish[x-1][y-1] + \
            petri_dish[x-1][y] + \
            petri_dish[x-1][y+1] + \
            petri_dish[x][y-1] + \
            petri_dish[x][y+1] + \
            petri_dish[x+1][y-1] + \
            petri_dish[x+1][y] + \
            petri_dish[x+1][y+1]
            
            if petri_dish[x][y] == 0:
                
        # if cell is dead: 
                if n == 3:
                    new_world[x][y] = 1
            # else:
                # new_world[x][y] = 0
            else: #(cell is alive)
                if n < 2 or n > 3:
                    new_world[x][y] = 0
            # else:
                # new_world[x][y] = 1
                
    return new_world


def main():
    import random
    # defines world, h, and w varaibles
    world = []
    heigth = 22
    width = 80
    
    # runs the populate and display functions
    populate(world, heigth, width)
    display(world, heigth, width)
    
    # prompts the user to enter any key
    key = input("Enter any key: ")
   
   # Loops while the entered key !='q'
    while key != "q":
        generation(world, heigth, width)
        display(world, heigth, width)
        key = input("Press q to quit, and any other key to continue: ")
        
    print ("goodbye")
    
        # run the generation function, replacing the current world with the newly generated world
        # returns a value, namely a new list that contains your updated world
#        newgeneration = generation(world, h, w)
        
        # display the new world
    
# Says that if this loads and the function main() is in it, run it
if __name__ == '__main__':
    main()