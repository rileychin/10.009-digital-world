def binary_to_decimal(binstr): #hwQ1
    rev_binstr = ''
    decimal_sum = 0
    deci_dictionary = {}
    for i in binstr:
        rev_binstr = i + rev_binstr
    print(rev_binstr)
    for i in range(len(rev_binstr)):
        if rev_binstr[i] == '1':
            deci_dictionary[2**i] = 1
        else:
            deci_dictionary[2**i] = 0
        
    for i in deci_dictionary:
        decimal_sum += i * deci_dictionary[i]
    return decimal_sum

def uncompress(string): #hwQ2
    new_string = ''
    for i in range(0,len(string),2):
        
        new_string += int(string[i]) * string[i+1]
    return new_string

def get_base_counts2(dna): #hwQ3
    new_dict = {'A' : 0, 'C':0,'G':0, 'T':0}
    for i in dna:
        print(i, ord(i),'11')
        if (ord(i) >= 65) and (ord(i) <=90):
            if i == 'A':
                new_dict['A'] += 1

            elif i == 'C':
                new_dict['C'] +=1

            elif i == 'G':
                new_dict['G'] +=1

            elif i == 'T':
                new_dict['T'] +=1
        else:
            return "The input DNA string is invalid"
    return new_dict


    
