N = 8

board = [-1] * N

def safe(row, col):

    for i in range(row):

        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(row):

    if row == N:
        return True

    for col in range(N):

        if safe(row, col):

            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False


if solve(0):

    for row in range(N):

        for col in range(N):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

else:
    print("No solution")