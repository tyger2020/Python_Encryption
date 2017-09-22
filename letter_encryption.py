dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
        'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19,
        'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
dicti = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I',
         10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R',
         19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
print("Enter a letter code.")
list_of_output = []
dict_list = []
code_list = []
out_list = []
s = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
answer = input()
for letter in answer:
    list_of_output.append(letter)
#print (list_of_output)
for i in list_of_output:
    #print (dict[i])
    dict_list.append(dict[i])
print(dict_list)
for num in dict_list:
    if (num >= 1 and num <= 5):
        num *= 2
        code_list.append(num)
    elif (num >= 6 and num <= 10):
        num = (num%3)*5;
        code_list.append(num)
    elif (num >= 11 and num <= 15):
        num = (num//4)*8
        code_list.append(num)
    elif (num >= 16 and num <= 20):
        if (num == 16):
            code_list.append(70)
        elif (num == 17):
            code_list.append(80)
        elif (num == 18):
            code_list.append(90)
        elif (num == 19):
            code_list.append(100)
        else: #(num == 20):
            code_list.append(20)
    else:# (num >= 21 and num <= 26):
        if (num == 21):
            code_list.append(84)
        elif (num == 22):
            code_list.append(132)
        elif (num == 23):
            code_list.append(12)
        elif (num == 24):
            code_list.append(144)
        elif (num == 25):
            code_list.append(60)
        else:# (num == 26):
            code_list.append(12*13)
print (code_list)
displace = 1
for i in code_list:
    #print (dict[i])
    out_list.append(dicti[(displace+i%26)%26])
    displace = (displace+i%26)%26
print(out_list)
