#!/bin/python3

from functools import cache
import math
import os
import random
import re
import sys

@cache
def cached_solve(x,y,a,a_next):
    if x != y:
        if (a_next != 0):
            if(a%2==0):
                return 'Even'
            else:
                return 'Odd'
        else:
            return 'Odd'
    else:
        if(a%2==0):
            return 'Even'
        else:
            return 'Odd'      



def solve(a, queries, solutions):
    for query,solution in zip(queries,solutions):
        x = query[0]
        y = query[1]
        try:
            res = cached_solve(x,y,a[x-1],a[x])
        except IndexError:
            res = cached_solve(x,y,a[x-1],None)
        if res != solution:
            print("x:{}\ty:{}\ta[x]:{}\tMine:{}\tReal:{}".format(x,y,a[x-1],res,solution))
                
            

if __name__ == '__main__':
    with open("./test_cases/case_5.txt") as test_case:
        arr_count = int(test_case.readline())
        arr = list(map(int, test_case.readline().rstrip().split()))
        q = int(test_case.readline().strip())
        queries = []
        for _ in range(q):
            queries.append(list(map(int, test_case.readline().rstrip().split())))
    
    with open("./test_cases/case_5_solutions.txt") as test_case:
        solutions = []
        for _ in range(q):
            solutions.append(test_case.readline().rstrip())

    solve(arr, queries,solutions)

