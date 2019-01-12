import time

# def timer(start_time,str="Function"):
def timer(func,start_time,str,*args,**kwargs):
    """.. function:: timer(str="Function",func,start_time)

    This function is running the main functiob func and times it's process.
    
    Note that func.__name__ returns the name of func as a string
    This could be useful later

    """

    # Start time of sub process
    time_i = time.time()

    # Print Start function statement
    print()
    print("Start %s..." % str)

    # ----- Run function ------
    if callable(func):
        result = func(*args,**kwargs)
    else:
        func(*args,**kwargs)
    # -------------------------

    # End time of sub process
    time_f = time.time()

    # time difference in subprocess
    # Total time needed:
    dtime = time_f - time_i
    
    # Print Time from start of program and Time eeded for Meshing 
    print("Finished %s." % str)
    print("Time: %s sec -- dt: %s sec" % ((time.time() - start_time) , dtime))
    print()

    if callable(func):
        return result
    else:
        return