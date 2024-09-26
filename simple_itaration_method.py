# Initial guess 
# 2x**2-5x+3=0 main equation
x = 0  # Starting point
max_iterations = 100

# Simple iteration method
for i in range(max_iterations):
    x_new = (2 * x**2 + 3) / 5  # Update using the rearranged equation
    x_new_rounded = round(x_new, 4)  # Round to 4 decimal places
    print(f"Iteration {i + 1}: x = {x_new_rounded}")
    
    # Check if the new value is equal to the old value
    if x_new_rounded == round(x, 4):
        print(f"Converged to root: {x_new_rounded} after {i + 1} iterations.")
        break
    
    # Update x for the next iteration
    x = x_new
else:
    print(f"No convergence after {max_iterations} iterations. Final x: {round(x, 4)}")