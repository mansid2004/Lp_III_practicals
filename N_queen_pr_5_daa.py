def is_safe(board, row, col, n):
    for j in range(col):
        if board[row][j] == "Q":
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def solve(board, col, n, solutions):
    if col == n:
        solutions.append([" ".join(row) for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            solve(board, col + 1, n, solutions)
            board[i][col] = "x"


def print_solution(solutions):
    import random
    if not solutions:
        print("No solutions found.")
        return
    sol = random.choice(solutions)
    for row in sol:
        print(row)


def main():
    while True:
        try:
            n = int(input("Input size of chessboard? n = "))
            if n <= 3:
                print("Enter a value greater than or equal to 4")
                continue
            break
        except ValueError:
            print("Invalid value entered. Enter again.")

    board = [["x"] * n for _ in range(n)]
    solutions = []
    solve(board, 0, n, solutions)

    print("\nOne of the solutions is:\n")
    print_solution(solutions)
    print(f"\nTotal number of solutions = {len(solutions)}")


if __name__ == "__main__":
    main()
