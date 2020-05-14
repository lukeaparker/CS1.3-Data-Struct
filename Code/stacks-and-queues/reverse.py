
input_num = '22235253534090'

def reverse(input_num):
    stack1 = []
    stack2 = []
    for i in input_num:
        stack1.append(i)
    for i in stack1:
        pop = stack1.pop()
        stack2.insert(0, i)
    print(stack2)
    return stack2
        

reverse(input_num)


