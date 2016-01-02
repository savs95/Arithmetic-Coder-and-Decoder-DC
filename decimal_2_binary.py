'''
Created on 27-Aug-2015

@author: savs95
'''

from decimal import Decimal

def length(inp_1, inp_2): # inp_1 must be smaller than inp_2
    inp_1 = Decimal(inp_1)
    inp_2 = Decimal(inp_2)
    iterator = 1
    final_number = ''
    ans = Decimal(0)
    while not (ans >=  inp_1 and ans < inp_2) :
        temp = Decimal(1)/Decimal(pow(2,iterator))
        temp2 = ans+temp
        iterator += 1
        if (temp2 >= inp_1 and temp2 < inp_2) :
            final_number = final_number + '1'
            ans = temp2
        elif (temp2 >= inp_2):
            final_number = final_number + '0'
        else :
            final_number = final_number + '1'
            ans=temp2
    return (len(final_number))
    
def convert(inp_1, inp_2): # inp_1 must be smaller than inp_2
    inp_1 = Decimal(inp_1)
    inp_2 = Decimal(inp_2)
    iterator = 1
    final_number = ''
    ans = Decimal(0)
    while not (ans >=  inp_1 and ans < inp_2) :
        temp = Decimal(1)/Decimal(pow(2,iterator))
        temp2 = ans+temp
        iterator += 1
        if (temp2 >= inp_1 and temp2 < inp_2) :
            final_number = final_number + '1'
            ans = temp2
        elif (temp2 >= inp_2):
            final_number = final_number + '0'
        else :
            final_number = final_number + '1'
            ans=temp2
    return (final_number)
    

def convert_dec(string):
    num=Decimal(0)
    for i in range(len(string)):
        if string[i]=='1':
            num+=Decimal(1)/Decimal(pow(2,i+1))
    return num        
    