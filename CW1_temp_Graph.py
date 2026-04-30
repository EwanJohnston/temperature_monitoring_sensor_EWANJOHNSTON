def tempGraph(xs,ys,temp_c):
    str_current_datetime =str(current_datetime) ## turns date_time into a string##
    xs.append(dt.datetime.now().strftime('%H:%M:%S:%F')) ##appends current_datetime to x-axis##
    ys.append(temp_c) ## appends temp_c values yo y-axis
    
    
    xs = xs[-0:]
    ys=ys[:]
    
    
    
    ##Formatting the graph##
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature (Celsius) over time')
    plt.ylabel('Temperature (deg C)')
    plt.plot(ys ,color ='r', marker = 'o', )

##plot the graph##
    plt.plot(xs,ys)
    
    
    ## pause for roughly 10 minutes inbetween plots##
    plt.pause(500)
    
    ##saves graph with uniwue file name each time##
    plt.savefig("temp"+ str_current_datetime +".png")