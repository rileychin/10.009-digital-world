#Q1: Create a function called mgrid that takes in six arguments xstart, xend, xpoints, ystart, yend, ypoints. The first three arguments specifies the starting, ending and the number of points in the x axis. The last three arguments does the same for the y axis. The function should return a list of lists as described in numpy.mgrid when the step length is a complex number. You are not allowed to use numpy.mgrid or any other built-in function in your code, but you are strongly suggested to use numpy.mgrid to test your version of mgrid.




def mgrid2d(xstart, xend, xpoints, ystart, yend, ypoints):
    # initialize a list to store the grid points that will be returned
    xr=[]
    yr=[]
    
    # initialize the first x value
    xval = xstart
    
    # initialize a variable to count the number of x points
    xcount = 0
    
    # Calculate the step size for x and y, replace None with the right expression
    xstep = (xend-xstart)/(xpoints-1)
    ystep = (yend-ystart)/(ypoints-1)
    
    while xcount < xpoints:
        # initialize the first y value, replace None with the right value
        yval = ystart
        
        # initialize the variable to count the number of y points, replace None with the right value
        ycount = 0
        
        # initialize temporary lists
        xrow = []
        yrow = []
        
        while ycount < ypoints:
            # write code to add the current x value to the temporary x list
            xrow.append(xval)

        
            # write code to add the current y value to the temporary y list
            yrow.append(yval)

        
            # increase the y value by the step size in y
            yval += ystep

        
            # increase the counter for the number of y points
            ycount += 1

        # Add the temporary x list to the final x list
        xr.append(xrow)

    
        # Add the temporary y list to the final y list
        yr.append(yrow)

    
        # increase x value by the step size in x
        xval += xstep

    
        # increase the counter for the number of x points
        xcount += 1

        
    return xr, yr

# Test:
# assert statement will throw error if the result is wrong
# no output will be produced for correct results

# Test:
# assert statement will throw error if the result is wrong
# no output will be produced for correct results

assert np.shape(mgrid2d(0, 4, 5, 0, 4, 5)) == np.shape(np.mgrid[0:4:5j,0:4:5j])
assert np.allclose(mgrid2d(0, 4, 5, 0, 4, 5), np.mgrid[0:4:5j,0:4:5j])

assert np.shape(mgrid2d(0, 5, 15, 0, 4, 10)) == np.shape(np.mgrid[0:5:15j,0:4:10j])
assert np.allclose(mgrid2d(0, 5, 15, 0, 4, 10), np.mgrid[0:5:15j,0:4:10j])







############################################################################33


#Q2. Create a function called mgrid that takes in nine arguments, three to specify each x, y, and z axis. The first three input arguments specifies the start (xstart), end (xend), and the number of points (xpoints) in the x axis. Similarly for the y and z axis. The function should return a list of lists as described in numpy.mgrid. You are not allowed to use numpy.mgrid or any other built-in function. However, you can use numpy.mgrid to test your own function and compare the result.

def mgrid3d(xstart, xend, xpoints, 
            ystart, yend, ypoints, 
            zstart, zend, zpoints):
    xr = []
    yr = []
    zr = []
    xval = xstart
    xcount = 0

    # calculate the step size for each axis
    xstep = (xend-xstart)/(xpoints-1)
    ystep = (yend-ystart)/(ypoints-1)
    zstep = (zend-zstart)/(zpoints-1)
    
    while xcount < xpoints:
        # initialize y points
        # create temporary variable to store x, y and z list
        yval = ystart
        ycount=0
        xrow =[]
        yrow=[]
        zrow=[]
        
    
        while ycount < ypoints:
            # initialize z points
            # create temporary variable to store the inner x, y, and z list
            zval=zstart
            zcount=0
            xxrow=[]
            yyrow=[]
            zzrow=[]
        
            while zcount < zpoints:
                # add the points x, y, and z to the inner most list
                xxrow.append(xval)
                yyrow.append(yval)
                zzrow.append(zval)
            
                # increase z point
                zval += zstep
            # add the inner most lists to the second lists
            xrow.append(xxrow)
            yrow.append(yyrow)
            zrow.append(zzrow)
        
            # increase y point
            yval+= ystep
        # add the second lists to the returned lists
        xr.append(xrow)
        yr.append(yrow)
        zr.append(zrow)
    
        # increase x point
        xval+=xstep
        
    return np.array([xr, yr, zr])

# Test:
# assert statement will throw error if the result is wrong
# no output will be produced for correct results

assert np.shape(mgrid3d(0, 4, 5, 0, 4, 5, 0, 4, 5)) == np.shape(np.mgrid[0:4:5j,0:4:5j,0:4:5j])
assert np.allclose(mgrid3d(0, 4, 5, 0, 4, 5, 0, 4, 5), np.mgrid[0:4:5j,0:4:5j,0:4:5j])

assert np.shape(mgrid3d(0, 5, 15, 0, 4, 10, 1, 2, 3)) == np.shape(np.mgrid[0:5:15j,0:4:10j,1:2:3j])
assert np.allclose(mgrid3d(0, 5, 15, 0, 4, 10, 1, 2, 3), np.mgrid[0:5:15j,0:4:10j,1:2:3j])
