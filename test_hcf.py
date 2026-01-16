import sys

# Check if two arguments are provided
if len(sys.argv) != 3:
    print("Usage: python hcf_lcm.py <number1> <number2>")
    sys.exit(1)

# Read numbers from command line arguments
a = int(sys.argv[1])
b = int(sys.argv[2])

# Function to calculate HCF (GCD)
def hcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Calculate HCF
h = hcf(a, b)

# Calculate LCM using formula: LCM * HCF = a * b
l = (a * b) // h

# Display results
print(f"HCF of {a} and {b} is: {h}")
print(f"LCM of {a} and {b} is: {l}")
