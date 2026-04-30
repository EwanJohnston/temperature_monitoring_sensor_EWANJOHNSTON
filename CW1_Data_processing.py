    
def Data_processing():
    ##create variables for data processing
    min = None
    max= None
    sum = 0
    len= 0
    
    with open ('filemname') as f: ##ENTER THE CORRECT FILENAME##  

        ##find correct min, mac=x and average values##
        for line in f:       
            val = float(line.strip())
            if min is None or val < min:
                min = val
            if max is None or val > max:
                max = val
            sum +=val
            len+=1
            
    
    _avg = float(sum) /len
    ##prints values in console for user##
    print("Min temp:", min)
    print("Max temp:", max)
    print("Average temp:" , _avg)
    
def main():
    Data_processing()

main()