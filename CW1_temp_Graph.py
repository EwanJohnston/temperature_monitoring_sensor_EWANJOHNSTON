def tempGraph(xs,ys,temp_c):
    str_current_datetime =str(current_datetime)
    xs.append(dt.datetime.now().strftime('%H:%M:%S:%F'))
    ys.append(temp_c)
    
    
    xs = xs[-0:]
    ys=ys[:]
    
    
    
    
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature (Celsius) over time')
    plt.ylabel('Temperature (deg C)')
    plt.plot(ys ,color ='r', marker = 'o', )


    plt.plot(xs,ys)
    
    
    
    plt.pause(500)
    
    plt.savefig("temp"+ str_current_datetime +".png")