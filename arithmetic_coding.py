'''
Created on 27-Aug-2015

@author: savs95
'''
from decimal import Decimal
import decimal_2_binary
import math

content="apoorv vikram singh is a rockstar"

f=open('content.txt','r')
content=f.read()
f.close()

length=len(content)
symbol_map_int = dict([(chr(x), 0) for x in range (0,128)])
for i in content :
    symbol_map_int[i]+=1
            
symbol_map_prob = {}
for i in symbol_map_int:
    if symbol_map_int[i]!=0 :
        symbol_map_prob[i]=Decimal(symbol_map_int[i])/Decimal(length) # Creates a probability dictionary
            
low = Decimal(0)
       
range_dict={}
for i in symbol_map_prob :
    range_dict[i] = (low,low+symbol_map_prob[i],symbol_map_prob[i])
    low += symbol_map_prob[i]

def encoder():
        ans=[]
        symbol_map_int = dict([(chr(x), 0) for x in range (0,128)])
        for i in content :
            symbol_map_int[i]+=1
            
        symbol_map_prob = {}
        for i in symbol_map_int:
            if symbol_map_int[i]!=0 :
                symbol_map_prob[i]=Decimal(symbol_map_int[i])/Decimal(length) # Creates a probability dictionary
            
        low = Decimal(0)
        
        global range_dict
        range_dict={}
        for i in symbol_map_prob :
            range_dict[i] = (low,low+symbol_map_prob[i],symbol_map_prob[i])
            low += symbol_map_prob[i]
            
        low = Decimal(0)
        high = Decimal(1)   
        temp_str='' 
        total_len=0
        
        for i in content :
            temp_str += i 
            symbol_range = high - low
            high = low + symbol_range*(range_dict[i][1]) 
            low = low + symbol_range*(range_dict[i][0])
            if(len(temp_str)>= 4) :
                temp5 = (decimal_2_binary.convert(low,high),len(temp_str))
                ans.append(temp5)
                low = Decimal(0)
                high = Decimal(1)
                total_len += len(temp_str) 
                temp_str=''
                
        if(length-total_len > 0) :
            new_str = content[total_len:length]
            low = Decimal(0)
            high = Decimal(1)
            for i in new_str:
                symbol_range = high - low
                high = low + symbol_range*(range_dict[i][1]) 
                low = low + symbol_range*(range_dict[i][0])
            temp5 = (decimal_2_binary.convert(low,high),len(new_str))
            ans.append(temp5)
            
        compression_ratio=Decimal(0)
        numerator= Decimal(0)
        denominator = Decimal(0) 
        numerator = Decimal(math.log(len(range_dict))/math.log(2))
        sum1=Decimal(0)   
        for i in ans:
            sum1 += Decimal(len(i[0])/i[1])
        denominator = sum1/len(ans)
        compressed_ratio = numerator/denominator
        print compressed_ratio  
        return ans 
    
def decoder(coded):
    ans=''
    for k in coded:
        num=decimal_2_binary.convert_dec(k[0])
        for j in range(0,k[1]):
            for i in range_dict :
                if num >= range_dict[i][0] and num < range_dict[i][1] :
                    ans += i
                    num = (num - range_dict[i][0])/range_dict[i][2]
                    break
    return ans              
                    
print decoder(encoder())
        
            
