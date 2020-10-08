from mayavi import mlab

mu, sigma = 0, 0.1 
x = np.load('x_test.dat')
y = np.load('y_test.dat')
z = np.load('z_test.dat')

density = np.load('den_test.dat')
figure = mlab.figure('DensityPlot')
pts = mlab.contour3d(density,contours=40,opacity=0.4)
mlab.axes()
mlab.show()