import os
import numpy as np
# import sample_input #  input sample file

#X number of buildings in a city. The number of buildings may vary
#  Input is a matrix, list of lists

class Matrix:
    def __init__(self, m) -> list:
        self.count_cities = count_cities
        self.count_water = count_water
        pass

class City:
    def __init__(self) -> None:
        pass
    city = '#'
    def __citycount__(self):
        pass

class CityCount:
    def __init__(self, count_cities) -> None:
        self.count_cities = count_cities

class Water:
    def __init__(self) -> None:
        pass
    water = '.'

class WaterCount:
    def __init__(self) -> None:
        pass

class Mountain:
    def __init__(self) -> None:
        mountain = '^'
        pass

class MountainCount:
    def __init__(self) -> None:
        pass

##  Question can you have a  matrix of string  values 
def compar_array(m1, m2, m3):
    pass

def check_valid_matrix(m):
    #check if matrix is valid containing no unexpected characters
    if (m == list):
        pass
    pass
    
# def count_features(count_list, position_list, list_num, list):
#     count_list += 1
#     position_list.append((list_num, list))
#     return count_list, position_list

def count_features(list_to_count, count_list, match, position_list, list_num):
    for i in range(len(list_to_count)):
        count_list += 1
        if list_to_count[i] == match:
            position_list.append((list_num, i))
    # count_list += 1
    # position_list.append((list_num, list))
    return count_list, position_list

def examine_matrix(m : list) -> list:
    # for now keep with example of 3 but expand to unlimited list size.
    # new tuple pair of list index as a row
    top_row, middle_row, bottom_row = m[0], m[1], m[2]
    total_city_count = 0
    total_water_count = 0
    positions_of_cities = []
    positions_of_water = []
    
    #First Row
    print('First Row')
    positions_of_cities2 = []
    # for i in top_row: ## change to enumerate
    #     print(i)
    #     if i == '#': # skip first value
    #         total_city_count += 1
    #         positions_of_cities.append((1, [i])) #top_row.index(i)
    #     if i =='.':
    #         total_water_count += 1
    #         positions_of_water.append((1, top_row.index(i)))
        # if current_value and i[-1] == "#": # no bridge needed
        #     print(" contains two # next to each other")

    # second attempt trying to add position of array
    #this wil set I to the index
    # for i in range(len(top_row)):
    #     print(i)
    #     total_city_count += 1
    #     if top_row[i] == '#':
    #         positions_of_cities.append((1, i))


    # middle_row
    # print('Second Row')
    # count_features2(list_to_count, count_list, match, position_list, list_num):
    count_features(middle_row, total_city_count, '#', positions_of_cities, 2)
    count_features(middle_row, total_water_count, '.', positions_of_water, 2)

    # Last Row
    count_features(bottom_row, total_city_count, '#', positions_of_cities, 3)
    count_features(bottom_row, total_water_count, '.', positions_of_water, 3)
            
    
    print('city count: ', total_city_count,
     ' water count: ', total_water_count,
     ' positions of cities list1:', positions_of_cities)
    return "hey this is filler"
    
    
def create_bridge(m : list):
    pass
    # takes in complete matrix and compair with 

# define what close to each other means. if position is a match and one link away. = bridge contender
# if position is within 1 of range between the three.

sample_input_matrix = [['#', '.', '.', '.', '#'],
                       ['.', '.', '#', '.', '.'],
                       ['#', '.', '.', '.', '#']]

result_dict = {'#': '🏙', '.': '🌊', '^':'🏔'}

def draw_scape(m: list):
    pass
    # draw array with emojis


examine_matrix(sample_input_matrix)

####
# gaveYard
 # print("city")
            # print("first value is the first one")
            #  log position and append to array as tuple pair
            # first_compare.append(([i].index,[i])) #position in list and value
            # print(first_compare)
            # continue # diff of pass vs continue
        # current_value = i # sets to value
        # print(current_value)
        # print([i][-1])
        # print(i[-1])