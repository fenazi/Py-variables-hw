# ---
str = "Hello world"
print(type(str))
print(hex(id(str)))
str +=  " from twuaiq!"
print(hex(id(str)))

print("observations: \n")

# ---
list = [1,2,3]
print(type(list))
print(hex(id(list)))
list[0] = 5
print(hex(id(list)))

print("observations: \n")


# ---
my_dict ={ "Ahmed": 43, "Mohammed": 23}
print(type(my_dict))
print(hex(id(my_dict)))
my_dict["Ali"] = "19"
print(hex(id(my_dict)))

print("observations: \n")

# --- 
tuple = 1,2,3
print(type(tuple))
print(hex(id(tuple)))

print("observations: \n")

# # Uncomment the below code and run it, can u explain what happened?
# tuple[0] = 2
#print("observations: \n")

