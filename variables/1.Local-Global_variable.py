# Local versus Global

# we define a function, called local
def local():
    m = 7
    print(m)

m = 5
print(m) this will print the value of m

# we call, or `execute` the function local
local() #this will print the value of variable m which is defined in the function
