###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
side_1 = a*b
side_2 = b*c
side_3 = a*c
cuboid_volume = a*b*c
cuboid_surface_area = 2*side_1 + 2*side_2 + 2*side_3
print(f'The volume of the cuboid is {cuboid_volume}')
print(f'The surface area of the cuboid is {cuboid_surface_area}')