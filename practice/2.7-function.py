#global scope

global_var = 10 # Global variable

def print_global():
	print(global_var) # Accessing global variable

print_global() # Outputs: 10



#local scope

def my_function():
	local_var = 5 # Local variable
	print(local_var) # Accessing the local variable

my_function() # outputs 5
print(local_var) # Causes an error because the local variable does not exist at                     the global scope














