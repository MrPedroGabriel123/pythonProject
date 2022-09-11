print("Welcome to my first attempt to create a calculator in python")
print("I have 0 fucking clue what I'm doing, or how to create if and elif statements")
print("I'm just going to try and make it work, and then I'll figure out how to make it work properly")
print("Im just going to use my c# knowledge to try and make it work")
print("hope you guys dont fuck with my head and just keep watching my shit")
#começar a calculadora

print("Please Enter Your First Number")
var1 = input()
print("Please Enter Your Second Number")
var2 = input()
print("Please Enter Your Operator(+,-,*,/)")
var3 = input()
if var3 == "+":
    print(int(var1) + int(var2))
elif var3 == "-":
    print(int(var1) - int(var2))
elif var3 == "*":
    print(int(var1) * int(var2))
elif var3 == "/":
    print(int(var1) / int(var2))
else:
    print("Invalid Operator")

