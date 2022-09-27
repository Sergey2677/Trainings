# Prompt user to set value of mass
mass = int(input('m: '))

# Constant value for lightspeed
SPEED = 300000000

# To calculate energy
E = mass * SPEED ** 2

# Print result
print('E:', E)