#!/bin/python3

def print_matrix(matrix):
    res_str = ""
    for row in matrix:
        for el in row:
           res_str += str(el)+" "
        res_str += "\n"
    print(res_str)

def is_connected(matrix,i_r,i_c,s_r,s_c):
    n_r = len(matrix)-1
    n_c = len(matrix[0])-1
    if 0<=i_r+s_r<=n_r and 0<=i_c+s_c<=n_c:
        if matrix[i_r+s_r][i_c+s_c]==1:
            return True
    return False

def get_connected_cells(matrix,index):
    connected = set()
    i_r,i_c = index
    for s_r in [-1,0,1]:
        for s_c in [-1,0,1]:
            if (is_connected(matrix,i_r,i_c,s_r,s_c)):
                connected.add((i_r+s_r,i_c+s_c))
    return connected

def connectedCell(matrix,solution):
    clusters = []
    empyt_set = set()
    for i,row in enumerate(matrix):
        for j,cell in enumerate(row):
            if cell == 1:
                connected_cells = get_connected_cells(matrix,(i,j))
                new_cluster = True
                for c,cluster in enumerate(clusters):
                    if connected_cells.intersection(cluster) != empyt_set:
                        clusters[c] = cluster.union(connected_cells)
                        new_cluster = False
                if new_cluster:
                    clusters.append(connected_cells)
    max_size = 0
    for cluster in clusters:
        size =  len(cluster)
        if size>max_size:
            max_size = size
    print(max_size,solution)
    return max_size


if __name__ == '__main__':
    with open("./test_cases/case_0.txt") as test_case:
        with open("./test_cases/case_0_solutions.txt") as solutions:

            n = int(test_case.readline().strip())

            m = int(test_case.readline().strip())

            matrix = []

            for _ in range(n):
                matrix.append(list(map(int, test_case.readline().rstrip().split())))

            solution = int(solutions.readline().rstrip())

            result = connectedCell(matrix,solution)