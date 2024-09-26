x = 0
max_iterations = 100


for i in range(max_iterations):

    f_x = 2*x**2 - 5*x+ 3

    df_x = 4*x - 5
    

    x_new = x - f_x / df_x
    
    if abs(x_new - x) < 0.0001:
        print("Root found:", x_new)
        break
    
    x = x_new
else:
    print("No solution found within the maximum number of iterations.")