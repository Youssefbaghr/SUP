def hanoi(n, source="A", auxiliary="B", destination="C"):
    if n <= 0:
        return []

    if n == 1:
        return [(source, destination)]

    return (
        hanoi(n - 1, source, destination, auxiliary)
        + [(source, destination)]
        + hanoi(n - 1, auxiliary, source, destination)
    )

moves = hanoi(3)
for m in moves:
    print(m[0], "->", m[1])
