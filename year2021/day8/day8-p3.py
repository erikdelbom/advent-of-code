import sys 

#codes_dict = { 0 : '', 1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '' }

CORRECT_DICT = { 0 : 'abcefg', 1 : 'cf', 2 : 'acdeg', 3 : 'acdfg', 4 : 'bcdf', 
                 5 : 'abdfg', 6 : 'abdefg', 7 : 'acf', 8 : 'abcdefg', 9 : 'abcdfg' }

pair_dict = { 'a' : '', 'b' : '', 'c' : '', 'd' : '', 'e' : '', 'f' : '', 'g' : '' }

def get_difference(a, b):
    a_set = set(a)
    b_set = set(b)
    dif = a_set.symmetric_difference(b_set)

    ret = ''

    for i in dif:
        ret += i

    return ret

for line in sys.stdin:
    codes = line.split(" |")[0].split()
    outputs = line.split("| ")[1].split()

    scrambled_dict = CORRECT_DICT

    one = ''
    seven = ''
    four = ''

    

    for code in codes:
        code = ''.join(sorted(code))
        if len(code) == 2:
            one = code
        elif len(code) == 3: 
            seven = code
        elif len(code) == 4:
            four = code
    
    pair_dict['a'] = get_difference(one, seven)

    find_nine = four + pair_dict['a']
    find_nine = ''.join(sorted(find_nine))

    for i in 

    print(find_nine)
    # for c in codes:
    #     if len(c) == 2:
    #         codes_dict[1] = c
    #         codes_dict[0] += c
    #         codes_dict[3] += c
    #         codes_dict[9] += c
    # for c in codes:
    #     if len(c) == 4:
    #         codes_dict[1] = c
    #         codes_dict[0] += c
    #         codes_dict[3] += c
    #         codes_dict[9] += c
    


            
    #print(codes, end=' ')
    #print(outputs)