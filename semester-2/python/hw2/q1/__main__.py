from .standard_weight import StandardWeight

height, gender = input().split()
height = int(height)
gender = int(gender)
sw = StandardWeight(height, gender)
print("{:.1f}".format(sw.calculate()))
