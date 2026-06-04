
def print_multiplication_table(n=10, cell_width=4):
    print(" " * cell_width, end="")

    for j in range(1, n + 1):
        print(f"{j:>{cell_width}}", end="")
    print()

    total_width = cell_width + n * cell_width
    print("-" * total_width)

    for i in range(1, n + 1):
        print(f"{i:>{cell_width}}|", end="")
        for j in range(1, n + 1):
            print(f"{i * j:>{cell_width}}", end="")
        print()

if __name__ == "__main__":
    print_multiplication_table(10, cell_width=4)