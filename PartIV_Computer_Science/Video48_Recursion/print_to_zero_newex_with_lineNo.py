def print_to_zero(n):
    if n < 0:
        return
    print(n)
    print_to_zero(n - 1)

print_to_zero(5)
