def sample_matrix():
    sample_input_matrix = [['#', '.', '.', '.', '#'],
                           ['.', '.', '#', '.', '.'],
                           ['#', '.', '.', '.', '#']]
    return sample_input_matrix


def sample_explained():
    # desired output and logged data from processing a matrix
    row_one = ['City', 'Water', 'Water', 'Water', 'City']
    row_one_city_logged = [(1, 0), (1, 4)]

    matrix_cities_logged = [(1, 0), (1, 4), (2, 2),(3, 0), (3, 4)]