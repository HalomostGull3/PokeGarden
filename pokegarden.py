#-----------------
#|	James Hom   |
#|	jhh318      |
#|	11287431    |
#|	Mark Keil   |
#-----------------

import numpy as np
import time

# start time for the time module
start_time = time.time()
# list of fruits abbreviated
fruits_list = ["F", "W", "G", "J", "M"]
# list of fruit's full names and their indexes in fruits_list to match order in output
fruit_value = [("Waterfruits", 1), ("Grassfruits", 2), ("Megafriuts", 4), ("Firefruits", 0), ("Joltfruits", 3)]

def initial_garden(filename):
    """
    This function takes in the text file and reads all the lines and determines the size of the garden and where each
        fruit is initially placed before starting the first year of spring.

    filename: string; used to access the text file
    return: the initial start for the garden array
    """
    f = open(filename, "r")
    get_line = f.readlines()        # read all the lines in the text file
    initial_tree_coords = {}        # dictionary to keep the coordinates for each fruit
    # create an empty array base off the first line of the text file
    garden_array = np.empty([int(get_line[0]), int(get_line[0])], dtype=str)
    garden_array.fill("_")      # fill the array with "_" to indicate an empty space

    for i in get_line:      # for-loop to iterate through all the lines in the text file
        if i == get_line[1]:        # if i equals the second line in the text file...\
            # create a key-value pair where, {"fruit abbreviation" : [list of tuples as coordinates]}
            initial_tree_coords["F"] = (get_line[1].strip().split(" "))
            # for-loop that iterates through how ever many coordinates there are to change the tuple values from string
            #   to integers
            for k in range(len(initial_tree_coords["F"])):
                initial_tree_coords["F"][k] = tuple(int(j) for j in initial_tree_coords["F"][k].split(","))
                garden_array[initial_tree_coords["F"][k]] = "F"     # implements the coordinates into the garden_array
        if i == get_line[2]:
            initial_tree_coords["W"] = (get_line[2].strip().split(" "))
            for k in range(len(initial_tree_coords["W"])):
                initial_tree_coords["W"][k] = tuple(int(j) for j in initial_tree_coords["W"][k].split(","))
                garden_array[initial_tree_coords["W"][k]] = "W"
        if i == get_line[3]:
            initial_tree_coords["G"] = (get_line[3].strip().split(" "))
            for k in range(len(initial_tree_coords["G"])):
                initial_tree_coords["G"][k] = tuple(int(j) for j in initial_tree_coords["G"][k].split(","))
                garden_array[initial_tree_coords["G"][k]] = "G"
        if i == get_line[4]:
            initial_tree_coords["J"] = (get_line[4].strip().split(" "))
            for k in range(len(initial_tree_coords["J"])):
                initial_tree_coords["J"][k] = tuple(int(j) for j in initial_tree_coords["J"][k].split(","))
                garden_array[initial_tree_coords["J"][k]] = "J"
    f.close()
    return garden_array

def around_fruits(i, j, garden_array):
    """
    This function looks through the garden array and finds the adjacent spaces for each single space in the array to
        place fruit abbreviations in and makes sure to not include spaces that are out of bounds.

    i: int; index of the row of the garden array
    j: int; index of the column of the garden array
    garden_array: array; the initial array of the garden
    return: list of tuples of integers that are possible coordinates within the range of the garden_array
    """
    adjacent_list = []
    for row in range(i - 1, i + 2):       # ranges from within 3 spaces row-wise
        # if the row coordinate is in range of the length of the garden_array...
        if row in range(0, len(garden_array)):
            for col in range(j - 1, j + 2):     # ranges within 3 spaces column-wise
                # if the col coordinate is in range of the length of garden_array...
                if col in range(0, len(garden_array)):
                    if row == i and col == j:
                        continue
                    # add valid adjacent coordinates to adjacent_list
                    adjacent_list.append((row, col))
    return adjacent_list


def fruit_type(adjacent_list, garden_array):
    """
    This function determines and return types of trees in the cells with coordinates from adjacent_list

    adjacent_list: list; list of tuples of integers
    garden_array: array; matrix to work with (list of lists of strings)
    return: list of fruit types coinciding with adjacent_list
    """
    tree_list = []
    for (i, j) in adjacent_list:            # does not include abbreviation for megafruit
        if garden_array[i][j] != "_":       # if the cell is not empty...
            tree_list.append(garden_array[i][j])        # append the fruit abbreviation
    return tree_list        # return unique strings abbreviations of trees from adjacent cells


def fruit_logic(fruit_coordinates):
    """
    Determine what type of tree should be grown among the list given trees using the logic of 'M' > all fruits, 'J' >
        'F', 'W', and 'G', 'F' > 'G', 'W' > 'F', 'G' > 'W', if 'F', 'W', 'G', 'J' compete for same cell, it produces
        a 'M', and if 'F', 'W', and 'G' compete for same cell, it produces '_'.

    fruits: list; trees abbreviations around particular cell
    return: string of fruit abbreviations to grow
    """
    # if there is no fruit in fruits, then produce "_"
    if len(fruit_coordinates) == 0:
        return "_"
    # megafruit dominates all
    elif "M" in fruit_coordinates:
        return "M"
    elif "J" in fruit_coordinates:
        # all 4 fruits: return megafruit
        if "F" in fruit_coordinates and "W" in fruit_coordinates and "G" in fruit_coordinates:
            return "M"
        # joltfruit dominates all except megafruit
        return "J"
    # 3 regular fruits: nothing spreads
    elif "F" in fruit_coordinates and "W" in fruit_coordinates and "G" in fruit_coordinates:
        return "_"
    # waterfruit dominates firefruit
    elif "F" in fruit_coordinates and "W" in fruit_coordinates:
        return "W"
    # firefruit dominates grassfruit
    elif "F" in fruit_coordinates and "G" in fruit_coordinates:
        return "F"
    # grassfruit dominates waterfruit
    elif "W" in fruit_coordinates and "G" in fruit_coordinates:
        return "G"
    # else: only one type of fruit: return that fruit
    return fruit_coordinates[0]


def spring(garden_array):
    """
    This function simulates a one year growth of the garden_array

    garden: array; matrix of fruits
    return: new garden, which grows yearly is applicable
    """
    # copy garden_array to build a new array with yearly planted fruits
    new_garden = garden_array.copy()
    # for each cell in the garden
    for i in range(len(garden_array)):
        for j in range(len(garden_array)):
            # if cell is empty (there is no fruit yet)
            if garden_array[i][j] == "_":
                # get its adjacent cells
                adjacent_fruits = around_fruits(i, j, garden_array)
                fruits = fruit_type(adjacent_fruits, garden_array)
                # determine, which types of fruits current cell is surrounded
                fruit = fruit_logic(fruits)
                # assign new fruit to the cell in new garden or stay empty
                new_garden[i][j] = fruit
    return new_garden

def fall(garden_array, total_fruits):
    """
    This function simulates the harvesting of fruits in the fall

    garden_array: array; a matrix with fruits
    total_fruits: list; list of counts of harvest from previous years
    return: list of integers that represent the total fruits in the garden_array and a list of integers that are
            harvested
    """
    # initiate list with harvest equal to zero to count current year"s harvest
    year_harvest = [0, 0, 0, 0, 0]
    # for each cell in garden
    for i in range(len(garden_array)):
        for j in range(len(garden_array[i])):
            # if there is fruit in the cell
            if garden_array[i][j] != "_":
                # determine its abbreviation index from constant fruits_list
                index = fruits_list.index(garden_array[i][j])
                # add 1 to the value with index "index" in year harvest and total harvest lists
                year_harvest[index] += 1
                total_fruits[index] += 1
    return total_fruits, year_harvest


def grow_garden(garden_array):
    """
    This function simulates growing the garden within all of the years it can grow

    garden_array: array; matrix with fruits (list of lists of strings)
    """
    # initiate list with harvest equal to zero to count all years harvest
    total_fruits = [0, 0, 0, 0, 0]
    # assign years counter to 0
    years = 0
    # while garden is growing
    while True:
        # get an updated garden_array based off from the spring function
        spring_garden = spring(garden_array.copy())
        # count yearly and total harvest
        if years > 0:
            total_fruits, year_harvest = fall(garden_array, total_fruits)
        # if garden does not grow anymore return lists with harvests and years counter
        if np.all(garden_array == spring_garden) and years > 0:
            return total_fruits, year_harvest, years
        # in other go to next year
        years += 1
        # update garden
        garden_array = spring_garden

def harvest():
    """
    This function goes through each text file and performs all of the function prior to harvest() and prints out the
        dedicated results
    """
    text_files = ["pokefruit_celadonfarm.txt", "pokefruit_palletfarm.txt", "pokefruit_pewterfarm.txt",
                  "pokefruit_saffronfarm.txt", "pokefruit_viridianfarm.txt"]
    for file in text_files:
        farm_array = initial_garden(file)
        total_yield, final_year_harvest, total_years = grow_garden(farm_array)
        # print summary
        print("Fruits yield from final year:")
        print("****************************")
        for (fruit, x) in fruit_value:
            print(fruit, ":", final_year_harvest[x])
        print()
        print("Total farm yield after", total_years, "years:")
        print("**********************************")
        for (fruit, x) in fruit_value:
            print(fruit, ":", total_yield[x])
        print()
### ADD THE '#' BELOW TO GO THROUGH THE TESTING ###
harvest()
# prints the program from start to finish
#print(time.time() - start_time)