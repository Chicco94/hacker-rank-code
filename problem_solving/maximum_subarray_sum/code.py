#!/bin/python3

import math
import os
import random
import re
import sys
from functools import cache
import time
from bisect import bisect,insort

@cache
def get_sub_sum(temp_sum,removed,added,modulo):
    return (temp_sum-removed+added)%modulo

def maximumSum_iter_2(a, m, a_sum):
    if len(a) == 0: return 0
    if len(a) == 1: return a[0]%m

    first = a[0]
    last = a[-1]

    return max(
            a_sum,
            maximumSum_iter_2(a[1:],m,get_sub_sum(a_sum,first,0,m)),
            maximumSum_iter_2(a[0:-1],m,get_sub_sum(a_sum,last,0,m))
        )

def maximumSum_2(a, m):
    return maximumSum_iter_2(a,m,sum(a)%m)

def maximumSum_iter_3(a, m, a_sum, do_left=True):
    if len(a) == 0: return 0
    if len(a) == 1: return a[0]%m
    first = a[0]
    last = a[-1]

    return max(
            a_sum,
            maximumSum_iter_3(a[1:],m,get_sub_sum(a_sum,first,0,m)) if do_left else a_sum,
            maximumSum_iter_3(a[0:-1],m,get_sub_sum(a_sum,last,0,m),do_left=False)
        )

def maximumSum_3(a, m):
    return maximumSum_iter_3(a,m,sum(a)%m)


def maxSubarray(a,m):
    N = len(a)
    cumulative_sums = []
    sum_so_far = 0
    max_sum = 0

    for i in range(N):
        sum_so_far = (sum_so_far + a[i]) % m        
        pos = bisect(cumulative_sums, sum_so_far)
        d = 0 if pos == i else cumulative_sums[pos]
        max_sum = max(max_sum, (sum_so_far + m - d) % m)
        insort(cumulative_sums, sum_so_far)
    return max_sum



def maximumSum_1(a, m):
    best_sub_a_sum = 0
    for l in range(1,len(a)+1):
        temp_sum = sum(a[0:l])%m
        if temp_sum>best_sub_a_sum:
                best_sub_a_sum = temp_sum
        for i in range(1,len(a)-l+1):
            temp_sum = get_sub_sum(temp_sum,a[i-1],a[i+l-1],m)
            if temp_sum>best_sub_a_sum:
                best_sub_a_sum = temp_sum
    return best_sub_a_sum

if __name__ == '__main__':
    with open("./test_cases/case_1.txt") as test_case:
        with open("./test_cases/case_1_solutions.txt") as solutions:

            q = int(test_case.readline().strip())
            print("tot cases: ",q)
            max_1_time = 0
            max_2_time = 0
            max_3_time = 0
            for i in range(q):
                first_multiple_input = test_case.readline().rstrip().split()
                n = int(first_multiple_input[0])
                m = int(first_multiple_input[1])
                a = list(map(int, test_case.readline().rstrip().split()))
                solution = int(solutions.readline().rstrip())

                start_time = time.time()
                r1 = maximumSum_1(a, m)
                time_1 = time.time()-start_time
                max_1_time += time_1

                start_time = time.time()
                r2= maxSubarray(a, m)
                time_2 = time.time()-start_time
                max_2_time += time_2

                start_time = time.time()
                r3= maximumSum_3(a, m)
                time_3 = time.time()-start_time
                max_3_time += time_3

                if (time_1 > 0.5 or time_2 > 0.5 or time_3 > 0.5):
                    print(f"{i} {time_1} {time_2} {time_3}")
                if (r1 != solution or r2 != solution or r3 != solution):
                    print(f"{i} {r1} {r2} {r3} {solution}")

            print("1:{}   2:{}   3:{}".format(max_1_time/q,max_2_time/q,max_3_time/q))

        