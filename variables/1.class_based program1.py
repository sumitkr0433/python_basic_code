#Source:Learn Python programming Fabrizio Romanao

# let's define the class Bike
class Bike:

	#construction creation
	#taking three arguments one is iteself object and other two are the value which we passing at the time of initialising variable
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material
    
    #creating the another function which will print the message
    def brake(self):
        print("Braking!")

# let's create a couple of instances and sending value to the constructor 
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# let's inspect the objects we have, instances of the Bike class.
##now calling the initialsing variable in constructor on the basis of object
print(red_bike.colour)  # prints: Red
print(red_bike.frame_material)  # prints: Carbon fiber


###on the basis of the blue object acccesing the constructor variable
print(blue_bike.colour)  # prints: Blue
print(blue_bike.frame_material)  # prints: Steel

#calling the another function
# let's brake!
red_bike.brake()  # prints: Braking!


##########################################################################################################################################################
#Interview Question:---
#Create an class and initialize the value during the object creation and calling that function and create an another function based on the object and called it?
