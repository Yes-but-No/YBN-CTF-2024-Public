from random import shuffle, choice

# flag must be long enough
flag = b'YBN24{u_should_have_made_used_of_the_flag_format_before_:/_kn@psacK_prim3s_c0rRupt55}'

def get_randbytes(length):
    result = []

    # at least 4 unique bytes with only one bit is 1 
    result.append("0"*7 + "1" + "0"*0)
    result.append("0"*6 + "1" + "0"*1)
    result.append("0"*5 + "1" + "0"*2)
    result.append("0"*4 + "1" + "0"*3)

    for _ in range(length-4):
        temp_byte = ""
        for _ in range(8):
            temp_byte += choice(["0", "1"])
        result.append(temp_byte)
        
    shuffle(result)
    return result

some_randbytes = get_randbytes(len(flag.decode()[6:-1]))