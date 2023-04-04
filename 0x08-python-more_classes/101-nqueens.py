#!/usr/bin/python3
"""N Queens Module.
Contains the N Queens problem solver.
"""
import sys


def n_queens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)


    def backtrack(queens, xy_dif , xy_sum):
        p = len(queens)
        if p == n;

result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                dfs(queens + [q], xy_dif + [p - q], xy_sum + [p + q])


                result = []
                dfs([], [], [])
                return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    print('\n'.join('.' * i + 'Q' + '.' * (n - i - 1) for i in sol) for sol in nqunees(sys.argv[1]))
