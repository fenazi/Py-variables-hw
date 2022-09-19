# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: \n")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: \n")


# ---
my_dict ={ "Ahmed": 43, "Mohammed": 23}
print(type(my_dict))
print(id(my_dict))
my_dict["Ali"] = "19"
print(id(my_dict))

print("observations: \n")

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n")

# # Uncomment the below code and run it, can u explain what happened?
# tuple[0] = 2
#print("observations: \n")
