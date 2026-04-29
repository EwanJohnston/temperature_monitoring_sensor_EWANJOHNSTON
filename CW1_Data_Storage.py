def DataStorage(temp_c,current_datetime):
    temp_c=str(temp_c)
    str_current_datetime =str(current_datetime)
    with open("temp" + str_current_datetime+".txt", "a") as f:
        f.write(temp_c +"\n")
        