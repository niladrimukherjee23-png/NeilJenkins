import sys

# Check if an argument is provided for name, otherwise set a default
if len(sys.argv) > 1:
    var1 = sys.argv[1]
else:
    var1 = "User"  # Default name if no argument is provided

var3 = ["B", "C", "D"]

if any(char in var3 for char in var1):
    print(var1)
else:
    print("Wrong Name")
