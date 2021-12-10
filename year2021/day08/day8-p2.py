import sys

to_int = { 'a' : 6, 'b' : 5, 'c' : 4, 'd' : 3, 'e' : 2, 'f' : 1, 'g' : 0 } 

def count_bits(number):
    count = 0
    for i in bin(number):
        if i == '1':
            count += 1
    return count

def code_to_bin(code):
    number = 0
    for i in range(len(code)):
        number |= (1 << to_int[code[i]])

    return number

def get_number(compare, codes, dif):
    for c in codes:
        potential_num = compare ^ c
        if count_bits(potential_num) == dif:
            return c

    return -1

def get_decoded_dict(codes):
    decoded = [0] * 10
    decoded[8] = 127
   
    code_length_five = []
    code_length_six = []

    for c in codes:
        if len(c) == 2:
            decoded[1] = code_to_bin(c)
        elif len(c) == 3:
            decoded[7] = code_to_bin(c)
        elif len(c) == 4:
            decoded[4] = code_to_bin(c)
        elif len(c) == 5:
            code_length_five.append(code_to_bin(c))
        elif len(c) == 6:
            code_length_six.append(code_to_bin(c))

    decoded[9] = get_number((decoded[4] | (decoded[1] ^ decoded[7])), code_length_six, 1)
    code_length_six.remove(decoded[9])
    decoded[3] = get_number(decoded[1], code_length_five, 3)
    code_length_five.remove(decoded[3])
    decoded[2] = get_number(decoded[4], code_length_five, 5)
    code_length_five.remove(decoded[2])
    decoded[5] = code_length_five[0]
    decoded[6] = get_number(decoded[5], code_length_six, 1)
    code_length_six.remove(decoded[6])
    decoded[0] = code_length_six[0]

    decoded_dict = { decoded[0] : 0, decoded[1] : 1, decoded[2] : 2, decoded[3] : 3, 
                    decoded[4] : 4, decoded[5] : 5, decoded[6] : 6, decoded[7] : 7, 
                    decoded[8] : 8, decoded[9] : 9 }

    return decoded_dict   

sum = 0

for line in sys.stdin:
    codes = line.split(" |")[0].split()
    outputs = line.split("| ")[1].split()

    decoded_dict = get_decoded_dict(codes)

    bcd = 0
    for i in range(4):
        coded = code_to_bin(outputs[i])
        decoded = decoded_dict[coded]
        if i == 0:
            bcd += decoded * 1000
        elif i == 1:
            bcd += decoded * 100
        elif i == 2:
            bcd += decoded * 10
        else:
            bcd += decoded
    sum += bcd

print(sum)