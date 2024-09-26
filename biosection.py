# equation is a**2 - 4*a - 10
a = -2  # Start of interval
b = -1  # End of interval
max_iterations = 100

# Calculate initial function values
f_a = a**2 - 4*a - 10  # f(a)
f_b = b**2 - 4*b - 10  # f(b)

# Check if f(a) and f(b) have opposite signs
if f_a * f_b >= 0:
    print("Bisection method fails. f(a) and f(b) must have opposite signs.")
else:
    for i in range(max_iterations):
        c = (a + b) / 2  # Midpoint
        f_c = c**2 - 4*c - 10  # Evaluate f(c)

        # Print the current midpoint and its function value
        print(f"Iteration {i + 1}: c = {round(c, 4)}, f(c) = {f_c}")
        
        if f_c == 0:
            print(f"Exact root found: {round(c, 4)}")
            break

        # Narrow down the interval using the new condition
        if f_a * f_c <= 0:
            b = c  # Root is in the left half
            f_b = f_c  # Update f(b)
        else:
            a = c  # Root is in the right half
            f_a = f_c  # Update f(a)

    # Final midpoint after all iterations
    c = (a + b) / 2
    print(f"Approximate root after {max_iterations} iterations: {round(c, 4)}")