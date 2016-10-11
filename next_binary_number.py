def get_next_binary_number(input):

    next_zero = "False"
    backwards = reversed(list(enumerate(input)))
    input = list(input)
    for index, item in backwards:

        if index == 0 and next_zero == "True":
            input[index] = "1"
            input.append("0")
            break

        if item == "0" and next_zero == "False":
            input[index] = "1"
            break

        if item == "1" and next_zero == "False":
            input[index] = "0"
            next_zero = "True"
            continue

        if item == "1" and next_zero == "True":
            input[index] = "0"
            continue

        if item == "0" and next_zero == "True":
            input[index] = "1"
            break

    return "".join(input)

def test():
    numbers = range(2,1000)
    for i in numbers:
        input = bin(i)[2:]
        next_number = bin(i+1)[2:]
        result = get_next_binary_number(input)
        if result == next_number:
            print(str(result)+" Success! "+str(i))
        else:
            print(str(result)+" Fail! expected "+next_number)
test()