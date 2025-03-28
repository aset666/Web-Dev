def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

# Example usage
N = int(input("Enter a number: "))
for square in square_generator(N):
    print(square, end=" ")
