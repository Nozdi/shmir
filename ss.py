"""
Module for editing/parsing .ss files generated by mfold.
"""

def parse_ss(file_name):
    """Function for parse ss file and gives tuples with first
        and last column on output
        input: string
        output: list of tuples with two elements"""
    read_data = []
    with open(file_name, "r") as ss_file:
        for line in ss_file.readlines():
            splited = line.split()
            read_data.append(map(int, [splited[0], splited[-1]]))
    return read_data


def to_normal():
    """
    Creates files with parsed data from all templates
    """
    for name in ('miR-122', 'miR-155', 'miR-21', 'miR-30a', 'miR-31'):
        with open(name, "w") as new_file:
            for elem in parse_ss(name + ".ss"):
                new_file.write(" ".join(elem)+"\n")


def parse_score(name):
    """
    Parses files with score to list of tuple and score value
    input: string
    output: float, list of three element lists
    """
    data = []
    with open(name) as score_file:
        max_score = float(score_file.readline())
        for line in score_file:
            number, pair, score = line.split()
            data.append([map(int, [number, pair]), int(score)])
    return max_score, data
    
def max_score(name):
    """
    Parses files with score to list of tuple and score value
    input: string
    output: int   
    """
    score = 0
    with open(name) as score_file:
        for line in score_file:
            number, pair, score_unit = line.split()
            score = score + int(score_unit)
    return score
