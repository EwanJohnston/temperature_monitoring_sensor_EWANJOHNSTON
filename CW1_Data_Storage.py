def DataStorage(temp_c,current_datetime):
    temp_c=str(temp_c) ##converts temp_c into string data type for storage##
    str_current_datetime =str(current_datetime) ## converts current_datetime to string for file naming##
    with open("temp" + str_current_datetime+".txt", "a") as f: ##saves the file with differwent name each time##
        f.write(temp_c +"\n") ##writes all temp_c values gathered into file##
        