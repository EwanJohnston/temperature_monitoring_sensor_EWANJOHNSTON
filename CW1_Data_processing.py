    
def Data_processing():
    min = None
    max= None
    sum = 0
    len= 0
    
    with open ('filemname') as f:  for line in f: ##ENTER THE CORRECT FILENAME##  
            val = float(line.strip())
            if min is None or val < min:
                min = val
            if max is None or val > max:
                max = val
            sum +=val
            len+=1
            
    
    _avg = float(sum) /len
    
    print("Min temp:", min)
    print("Max temp:", max)
    print("Average temp:" , _avg)
    
def main():
    Data_processing()

main()
