""" practice with strings
1. concatenation and split
2. partition
3. format
4. f-string format
"""

import math
import json


colors_string = ";".join(["red", "blue", "green", "yellow"])
colors_list = colors_string.split(";")
bedrijf = "".join(["jouw", "ICT", "vacature"])

words = "unforgetable".partition("forget")
departure, separator, arrival = "London:Edinburgh".partition(":")
origin, _, destination = "Amsterdam-Paris".partition("-")   # _ is  for unused or dummy values; we don't want to capture the separator

stringformatting_1 = "My {0}'s birthday is {1}. {0} was born in {2}".format("mom", "21st of May", 1945)
stringformatting_2 = "My height and weight are {} m and {} kg".format(1.81, 64)
position = "Current position is {latitude} {longitude}".format(latitude="60N", longitude="5E")
galactic_position = "Galactic position is x={pos[0]},  y={pos[1]}, z={pos[2]}".format(pos=[65.2, 25.1, 82.2])
math_constants = "Math constants are pi={m.pi} and e={m.e}".format(m=math)
math_constants_3f = "Math constants are pi={m.pi:.3f} and {m.e:.3f}".format(m=math)

value = 4 * 20
forfstring = f'The results is {value}'   # value is evaluated and inserted at runtime


if __name__ == '__main__':
    print(colors_string)
    print(colors_list)
    print(bedrijf)
    print(words)
    print(departure, arrival)
    print(origin, destination)
    print(stringformatting_1)
    print(stringformatting_2)
    print(position)
    print(galactic_position)
    print(math_constants)
    print(math_constants_3f)
    print(forfstring)