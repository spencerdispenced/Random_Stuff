
stack = []

num = 14356

while num > 0:
    stack.insert(0, num % 2)
    num = int(num / 10)

print(stack)

# def fun(num):
#     if num == 1:
#         return num
#     else:
#         value = fun(num-1)
#         return num * value + num


# print(fun(4))
