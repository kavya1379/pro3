import sys

# Default values
default_p = 1000
default_r = 5
default_t = 2

# Check if user provided all 3 arguments
if len(sys.argv) == 4:
    # Using eval() to interpret numeric input (not a datatype function)
    p = eval(sys.argv[1])
    r = eval(sys.argv[2])
    t = eval(sys.argv[3])
else:
    # No input or incomplete input; use defaults
    print("No input or incomplete input given. Using default values.")
    p = default_p
    r = default_r
    t = default_t

# Calculate Simple Interest
si = (p * r * t) / 100

# Display results
print("Principal =", p)
print("Rate =", r)
print("Time =", t)
print("Simple Interest =", si)