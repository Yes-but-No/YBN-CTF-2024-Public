"""
1. write
2. read
>> 1
Enter string
>> a
Enter address
>> -51                                                      # Bypass readonly issue using negative indexes in python! This lets us write data into the READ_ONLY region
string written successfully! You can view it at 948
1. write
2. read
>> 1
Enter string
>> 0                                                        # This gets overwritten into the length value of the previous string
Enter address
>> -52                                  
string written successfully! You can view it at 947
1. write
2. read
>> 2
Enter address
>> 948                                                      # Now by reading our first string, the program thinks it has a lot more characters and thus, prints the flag with it!
Your string: aYBN24{n3g4tive_inDexeS_aNd_struCt_ov3rfl0W!}
1. write
2. read
>>
"""