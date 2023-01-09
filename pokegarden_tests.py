#-----------------
#|	James Hom   |
#|	jhh318      |
#|	11287431    |
#|	Mark Keil   |
#-----------------

import numpy as np
from a10q1 import initial_garden, around_fruits, fruit_type, fruit_logic, spring, fall, grow_garden

#####  TEST DRIVER: initial_garden  #####
# if the size of the number of cells do not equal to a 5x5
if initial_garden("pokefruit_celadonfarm.txt").size != 25:
    print("Error: size of pokefarm is not 25, (5x5 array)")
# if the size of the number of cells do not equal to a 4x4
if initial_garden("pokefruit_palletfarm.txt").size != 16:
    print("Error: size of pokefarm is not 16, (4x4 array)")
# if the size of the number of cells do not equal to a 5x5
if initial_garden("pokefruit_pewterfarm.txt").size != 25:
    print("Error: size of pokefarm is not 25, (5x5 array)")
# if the size of the number of cells do not equal to a 100x100
if initial_garden("pokefruit_saffronfarm.txt").size != 10000:
    print("Error: size of pokefarm is not 10000, (100x100 array)")
# if the size of the number of cells do not equal to a 7x7
if initial_garden("pokefruit_viridianfarm.txt").size != 49:
    print("Error: size of pokefarm is not 49, (7x7 array)")

#####  TEST DRIVER: around_fruits  #####
for i in range(len(initial_garden("pokefruit_celadonfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_celadonfarm.txt"))):
        # if (i, j) or the coordinates for adjacent cells are negative in pokefruit_celadonfarm
        if around_fruits(i, j, initial_garden("pokefruit_celadonfarm.txt")) == (i < 0, j < 0):
            print("Error: detecting fruits out of bounds from initial_garden (5x5 array)")
            break
for i in range(len(initial_garden("pokefruit_palletfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_palletfarm.txt"))):
        # if (i, j) or the coordinates for adjacent cells are negative in pokefruit_palletfarm
        if around_fruits(i, j, initial_garden("pokefruit_palletfarm.txt")) == (i < 0, j < 0):
            print("Error: detecting fruits out of bounds from initial_garden (4x4 array)")
            break
for i in range(len(initial_garden("pokefruit_pewterfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_pewterfarm.txt"))):
        # if (i, j) or the coordinates for adjacent cells are negative in pokefruit_pewterfarm
        if around_fruits(i, j, initial_garden("pokefruit_pewterfarm.txt")) == (i < 0, j < 0):
            print("Error: detecting fruits out of bounds from initial_garden (5x5 array)")
            break
for i in range(len(initial_garden("pokefruit_saffronfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_saffronfarm.txt"))):
        # if (i, j) or the coordinates for adjacent cells are negative in pokefruit_saffronfarm
        if around_fruits(i, j, initial_garden("pokefruit_saffronfarm.txt")) == (i < 0, j < 0):
            print("Error: detecting fruits out of bounds from initial_garden (100x100 array)")
            break
for i in range(len(initial_garden("pokefruit_viridianfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_viridianfarm.txt"))):
        # if (i, j) or the coordinates for adjacent cells are negative in pokefruit_viridianfarm
        if around_fruits(i, j, initial_garden("pokefruit_viridianfarm.txt")) == (i < 0, j < 0):
            print("Error: detecting fruits out of bounds from initial_garden (7x7 array)")
            break

#####  TEST DRIVER: fruit_type  #####
for i in range(len(initial_garden("pokefruit_celadonfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_celadonfarm.txt"))):
        # if the list of abbreviated fruits have a different data type than expected in pokefruit_celadonfarm
        if fruit_type(around_fruits(i, j, initial_garden("pokefruit_celadonfarm.txt")), initial_garden("pokefruit_celadonfarm.txt")) == [""]:
            print("Error: detecting unexpected output from fruit_type that is neither 'F', 'W', 'G', 'J', 'M' or '_' in Celadon Farm")
            break
for i in range(len(initial_garden("pokefruit_palletfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_palletfarm.txt"))):
        # if the list of abbreviated fruits have a different data type than expected in pokefruit_palletfarm
        if fruit_type(around_fruits(i, j, initial_garden("pokefruit_palletfarm.txt")), initial_garden("pokefruit_palletfarm.txt")) == [""]:
            print("Error: detecting unexpected output from fruit_type that is neither 'F', 'W', 'G', 'J', 'M' or '_' in Celadon Farm")
            break
for i in range(len(initial_garden("pokefruit_pewterfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_pewterfarm.txt"))):
        # if the list of abbreviated fruits have a different data type than expected in pokefruit_pewterfarm
        if fruit_type(around_fruits(i, j, initial_garden("pokefruit_pewterfarm.txt")), initial_garden("pokefruit_pewterfarm.txt")) == [""]:
            print("Error: detecting unexpected output from fruit_type that is neither 'F', 'W', 'G', 'J', 'M' or '_' in Celadon Farm")
            break
for i in range(len(initial_garden("pokefruit_saffronfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_saffronfarm.txt"))):
        # if the list of abbreviated fruits have a different data type than expected in pokefruit_saffronfarm
        if fruit_type(around_fruits(i, j, initial_garden("pokefruit_saffronfarm.txt")), initial_garden("pokefruit_saffronfarm.txt")) == [""]:
            print("Error: detecting unexpected output from fruit_type that is neither 'F', 'W', 'G', 'J', 'M' or '_' in Celadon Farm")
            break
for i in range(len(initial_garden("pokefruit_viridianfarm.txt"))):
    for j in range(len(initial_garden("pokefruit_viridianfarm.txt"))):
        # if the list of abbreviated fruits have a different data type than expected in pokefruit_viridianfarm
        if fruit_type(around_fruits(i, j, initial_garden("pokefruit_viridianfarm.txt")), initial_garden("pokefruit_viridianfarm.txt")) == [""]:
            print("Error: detecting unexpected output from fruit_type that is neither 'F', 'W', 'G', 'J', 'M' or '_' in Celadon Farm")
            break

#####  TEST DRIVER: determine_type_fruit  #####
# if two firefruits do not equal to firefruit in a cell
if fruit_logic(["F", "F"]) != "F":
    print("Error: fruit_logic's logic is incorrect where 'F' and 'F' in one cell is not 'F'")
# if two waterfruits do not equal to waterfruit in a cell
if fruit_logic(["W", "W"]) != "W":
    print("Error: fruit_logic's logic is incorrect where 'W' and 'W' in one cell is not 'W'")
# if two grassfruits do not equal to grassfruit in a cell
if fruit_logic(["G", "G"]) != "G":
    print("Error: fruit_logic's logic is incorrect where 'G' and 'G' in one cell is not 'G'")
# if two joltfruits do not equal to joltfruit in a cell
if fruit_logic(["J", "J"]) != "J":
    print("Error: fruit_logic's logic is incorrect where 'J' and 'J' in one cell is not 'J'")
# if two megafruits do not equal to megafruit in a cell
if fruit_logic(["M", "M"]) != "M":
    print("Error: fruit_logic's logic is incorrect where 'M' and 'M' in one cell is not 'M'")
# if a firefruit and waterfruit are competing for a cell
if fruit_logic(["F", "W"]) == "F":
    print("Error: fruit_logic's logic is incorrect where 'F' > 'W'")
# if a waterfruit and grassfruit are competing for a cell
if fruit_logic(["W", "G"]) == "W":
    print("Error: fruit_logic's logic is incorrect where 'W' > 'G'")
# if a grassfruit and firefruit are competing for a cell
if fruit_logic(["G", "F"]) == "G":
    print("Error: fruit_logic's logic is incorrect where 'G' > 'F'")
# if a firefruit and joltfruit are competing for a cell
if fruit_logic(["F", "J"]) == "F":
    print("Error: fruit_logic's logic is incorrect where 'F' > 'J'")
# if a waterfruit and joltfruit are competing for a cell
if fruit_logic(["W", "J"]) == "W":
    print("Error: fruit_logic's logic is incorrect where 'W' > 'J'")
# if a grassfruit and joltfruit are competing for a cell
if fruit_logic(["G", "J"]) == "G":
    print("Error: fruit_logic's logic is incorrect where 'G' > 'J'")
# if a firefruit and megafruit are competing for a cell
if fruit_logic(["F", "M"]) == "F":
    print("Error: fruit_logic's logic is incorrect where 'F' > 'M'")
# if a waterfruit and megafruit are competing for a cell
if fruit_logic(["W", "M"]) == "W":
    print("Error: fruit_logic's logic is incorrect where 'W' > 'M'")
# if a grassfruit and megafruit are competing for a cell
if fruit_logic(["G", "M"]) == "G":
    print("Error: fruit_logic's logic is incorrect where 'G' > 'M'")
# if joltfruit and megafruit are competing for a cell
if fruit_logic(["J", "M"]) == "J":
    print("Error: fruit_logic's logic is incorrect where 'J' > 'M'")
# if firefruit is in an empty cell
if fruit_logic(["F", "_"]) == "_":
    print("Error: fruit_logic's logic is incorrect where 'F' > '_'")
# if waterfruit is in an empty cell
if fruit_logic(["W", "_"]) == "_":
    print("Error: fruit_logic's logic is incorrect where 'W' > '_'")
# if grassfruit is in an empty cell
if fruit_logic(["G", "_"]) == "_":
    print("Error: fruit_logic's logic is incorrect where 'G' > '_'")
# if joltfruit is in an empty cell
if fruit_logic(["J", "_"]) == "_":
    print("Error: fruit_logic's logic is incorrect where 'J' > '_'")
# if megafruit is in an empty cell
if fruit_logic(["M", "_"]) == "_":
    print("Error: fruit_logic's logic is incorrect where 'M' > '_'")
# if firefruit, waterfruit, and grassfruit compete for a cell
if fruit_logic(["F", "W", "G"]) != "_":
    print("Error: fruit_logic's logic is incorrect where 'F', 'W', and 'G' do not make '_'")
# if a firefruit, waterfruit, and joltfruit are competing for a cell
if fruit_logic(["F", "W", "J"]) != "J":
    print("Error: fruit_logic's logic is incorrect where 'F' and 'W' > 'J'")
# if a waterfruit, grassfruit, and joltfruit are competing for a cell
if fruit_logic(["W", "G", "J"]) != "J":
    print("Error: fruit_logic's logic is incorrect where 'W' and 'G' > 'J'")
# if a grassfruit, firefruit, and joltfruit are competing for a cell
if fruit_logic(["G", "F", "J"]) != "J":
    print("Error: fruit_logic's logic is incorrect where 'G' and 'F' > 'J'")
# if a firefruit, waterfruit, grassfruit, joltfruit, and megafruit are competing for a cell
if fruit_logic(["F", "W", "G", "J", "M"]) != "M":
    print("Error: fruit_logic's logic is incorrect where 'F', 'W', 'G', or 'J' > 'M'")

#####  TEST DRIVER: spring  #####
# if firefruit is not in new_garden in pokefruit_celadon_farm
if "F" not in spring(initial_garden("pokefruit_celadonfarm.txt")):
    print("Error: spring has no firefruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_celadon_farm
if "W" not in spring(initial_garden("pokefruit_celadonfarm.txt")):
    print("Error: spring has no waterfruit in new_garden after year 1 of growth")
# if firefruit is not in new_garden in pokefruit_celadon_farm
if "G" not in spring(initial_garden("pokefruit_celadonfarm.txt")):
    print("Error: spring has no grassfruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_celadon_farm
if "J" not in spring(initial_garden("pokefruit_celadonfarm.txt")):
    print("Error: spring has no joltfruit in new_garden after year 1 of growth")
# if firefruit is not in new_garden in pokefruit_palletfarm
if "F" not in spring(initial_garden("pokefruit_palletfarm.txt")):
    print("Error: spring has no firefruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_palletfarm
if "W" not in spring(initial_garden("pokefruit_palletfarm.txt")):
    print("Error: spring has no waterfruit in new_garden after year 1 of growth")
# if firefruit is not in new_garden in pokefruit_palletfarm
if "G" not in spring(initial_garden("pokefruit_palletfarm.txt")):
    print("Error: spring has no grassfruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_palletfarm
if "J" not in spring(initial_garden("pokefruit_palletfarm.txt")):
    print("Error: spring has no joltfruit in new_garden after year 1 of growth")
# if firefruit is not in new_garden in pokefruit_pewterfarm
if "F" not in spring(initial_garden("pokefruit_pewterfarm.txt")):
    print("Error: spring has no firefruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_pewterfarm
if "W" not in spring(initial_garden("pokefruit_pewterfarm.txt")):
    print("Error: spring has no waterfruit in new_garden after year 1 of growth")
# if firefruit is not in new_garden in pokefruit_pewterfarm
if "G" not in spring(initial_garden("pokefruit_pewterfarm.txt")):
    print("Error: spring has no grassfruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_pewterfarm
if "J" not in spring(initial_garden("pokefruit_pewterfarm.txt")):
    print("Error: spring has no joltfruit in new_garden after year 1 of growth")
# if firefruit is not in new_garden in pokefruit_saffronfarm
if "F" not in spring(initial_garden("pokefruit_saffronfarm.txt")):
    print("Error: spring has no firefruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_saffronfarm
if "W" not in spring(initial_garden("pokefruit_saffronfarm.txt")):
    print("Error: spring has no waterfruit in new_garden after year 1 of growth")
# if firefruit is not in new_garden in pokefruit_saffronfarm
if "G" not in spring(initial_garden("pokefruit_saffronfarm.txt")):
    print("Error: spring has no grassfruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_saffronfarm
if "J" not in spring(initial_garden("pokefruit_saffronfarm.txt")):
    print("Error: spring has no joltfruit in new_garden after year 1 of growth")
# if firefruit is not in new_garden in pokefruit_viridianfarm
if "F" not in spring(initial_garden("pokefruit_viridianfarm.txt")):
    print("Error: spring has no firefruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_viridianfarm
if "W" not in spring(initial_garden("pokefruit_viridianfarm.txt")):
    print("Error: spring has no waterfruit in new_garden after year 1 of growth")
# if firefruit is not in new_garden in pokefruit_viridianfarm
if "G" not in spring(initial_garden("pokefruit_viridianfarm.txt")):
    print("Error: spring has no grassfruit in new_garden after year 1 of growth")
# if waterfruit is not in new_garden in pokefruit_viridianfarm
if "J" not in spring(initial_garden("pokefruit_viridianfarm.txt")):
    print("Error: spring has no joltfruit in new_garden after year 1 of growth")

#####  TEST DRIVER: fall  #####
# if the harvest has negative values or is not summing up the fruits during each harvest in pokefruit_celadonfarm
if fall(initial_garden("pokefruit_celadonfarm.txt"), [0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_celadonfarm")
# if the harvest has negative values or is not summing up the fruits during each harvest in pokefruit_palletfarm
if fall(initial_garden("pokefruit_celadonfarm.txt"), [0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_palletfarm")
# if the harvest has negative values or is not summing up the fruits during each harvest in pokefruit_pewterfarm
if fall(initial_garden("pokefruit_celadonfarm.txt"), [0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_pewterfarm")
# if the harvest has negative values or is not summing up the fruits during each harvest in pokefruit_saffronfarm
if fall(initial_garden("pokefruit_celadonfarm.txt"), [0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_saffronfarm")
# if the harvest has negative values or is not summing up the fruits during each harvest in pokefruit_viridianfarm
if fall(initial_garden("pokefruit_celadonfarm.txt"), [0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_viridianfarm")

#####  TEST DRIVER: grow_garden  #####
# if the grow_garden has negative values or is not summing up the fruits during each harvest in pokefruit_celadonfarm
if grow_garden(initial_garden("pokefruit_celadonfarm.txt")) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_celadonfarm")
# if the grow_garden has negative values or is not summing up the fruits during each harvest in pokefruit_palletfarm
if grow_garden(initial_garden("pokefruit_celadonfarm.txt")) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_palletfarm")
# if the grow_garden has negative values or is not summing up the fruits during each harvest in pokefruit_pewterfarm
if grow_garden(initial_garden("pokefruit_celadonfarm.txt")) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_pewterfarm")
# if the grow_garden has negative values or is not summing up the fruits during each harvest in pokefruit_saffronfarm
if grow_garden(initial_garden("pokefruit_celadonfarm.txt")) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_saffronfarm")
# if the grow_garden has negative values or is not summing up the fruits during each harvest in pokefruit_viridianfarm
if grow_garden(initial_garden("pokefruit_celadonfarm.txt")) == [-1, -1, -1, -1, -1]:
    print("Error: the harvest logic is incorrect and should not have negative values at all in pokefruit_viridianfarm")