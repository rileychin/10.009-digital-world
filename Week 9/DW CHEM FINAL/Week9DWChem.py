import numpy as np
import scipy.constants as c #constants for whatever
import math #basic math operations

import cmath #complex math

def spherical_to_cartesian(r,theta,phi):
    x = r*(np.sin(theta))*(np.cos(phi))
    y = r*(np.sin(theta))*(np.sin(phi))
    z = r*(np.cos(theta))
    return round(x,5),round(y,5),round(z,5)
	
#########################################################
def cartesian_to_spherical(x, y, z):
    r = (x**2+y**2+z**2)**0.5
    if r == 0:
        theta = np.arccos(0)
    else:    
        theta = np.arccos(z/r)
    if r != 0:
        phi = np.arccos(x/(r*(np.sin(theta))))
    else:
        phi = np.arctan(0)

    return round(r,5),round(theta,5),round(phi,5)
############################################################

pi = c.pi
j = 1j


def angular_wave_func(m, l, theta, phi):
    if l == 0 and m == 0:
        Y = np.sqrt(1 / (4 * pi))
    elif l == 1:
        if m == 1:
            Y = -np.sqrt(3 / (8 * c.pi)) * np.sin(theta) * np.exp(phi * j)
        elif m == 0:
            Y = np.sqrt(3 / (4 * pi)) * np.cos(theta)
        elif m == -1:
            Y = np.sqrt(3 / (8 * c.pi)) * np.sin(theta) * np.exp(phi * -j)
    elif l == 2:
        if m == 2:
            Y = np.sqrt(15 / (32 * pi)) * np.power(np.sin(theta), 2) * np.exp(
                2 * phi * j)
        elif m == 1:
            Y = -np.sqrt(15 /
                         (8 * pi)) * np.cos(theta) * np.sin(theta) * np.exp(
                             phi * j)
        elif m == 0:
            Y = np.sqrt(5 / (16 * pi)) * (3 * np.power(np.cos(theta), 2) - 1)
        elif m == -1:
            Y = np.sqrt(15 /
                        (8 * pi)) * np.cos(theta) * np.sin(theta) * np.exp(
                            phi * -j)
        elif m == -2:
            Y = np.sqrt(15 / (32 * pi)) * np.power(np.sin(theta), 2) * np.exp(
                2 * phi * -j)
    elif l == 3:
        if m == 3:
            Y = -np.sqrt(35 / (64 * pi)) * np.power(np.sin(theta), 3) * np.exp(
                3 * phi * j)
        elif m == 2:
            Y = np.sqrt(105 / (32 * pi)) * np.cos(theta) * np.power(
                np.sin(theta), 2) * np.exp(2 * phi * j)
        elif m == 1:
            Y = -np.sqrt(21 / (64 * pi)) * np.sin(theta) * (
                5 * np.power(np.cos(theta), 2) - 1) * np.exp(phi * j)
        elif m == 0:
            Y = np.sqrt(7 / (16 * pi)) * (
                5 * np.power(np.cos(theta), 3) - 3 * np.cos(theta))
        elif m == -1:
            Y = np.sqrt(21 / (64 * pi)) * np.sin(theta) * (
                5 * np.power(np.cos(theta), 2) - 1) * np.exp(phi * -j)
        elif m == -2:
            Y = np.sqrt(105 / (32 * pi)) * np.cos(theta) * np.power(
                np.sin(theta), 2) * np.exp(2 * phi * -j)
        elif m == -3:
            Y = np.sqrt(35 / (64 * pi)) * np.power(np.sin(theta), 3) * np.exp(
                3 * phi * -j)
    return np.round(Y, 5)
##################################################################
import scipy.constants as c #constants for whatever
import math #basic math operations
import numpy as np #extra
import cmath #complex math

def radial_wave_func(n, l, r):
    a = c.physical_constants["Bohr radius"][0]
    if n == 1 and l == 0:
        R = 2 * np.exp(-r / a)
    elif n == 2:
        if l == 0:
            R = 1 / np.sqrt(2) * (1 - r / (2 * a)) * np.exp(-r / (2 * a))
        elif l == 1:
            R = 1 / np.sqrt(24) * (r / a) * np.exp(-r / (2 * a))
    elif n == 3:
        if l == 0:
            R = 2 / (81 * np.sqrt(3)) * (27 - 18 * (r / a) + 2 * np.power(
                (r / a), 2)) * np.exp(-r / (3 * a))
        elif l == 1:
            R = 8 / (27 * np.sqrt(6)) * (1 - r / (6 * a)) * (r / a) * np.exp(
                -r / (3 * a))
        elif l == 2:
            R = 4 / (81 * np.sqrt(30)) * np.power(
                (r / a), 2) * np.exp(-r / (3 * a))
    elif n == 4:
        if l == 0:
            R = 1 / 4 * (1 - 3 / 4 * (r / a) + 1 / 8 + np.power(
                (r / a), 2) - 1 / 192 * np.power(
                    (r / a), 3)) * np.exp(-r / (4 * a))
        elif l == 1:
            R = np.sqrt(5) / (16 * np.sqrt(3)) * (r / a) * (
                1 - 1 / 4 * (r / a) + 1 / 80 + np.power(
                    (r / a), 2)) * np.exp(-r / (4 * a))
        elif l == 2:
            R = 1 / (64 * np.sqrt(5)) * np.power(
                (r / a), 2) * (1 - 1 / 12 * (r / a)) * np.exp(-r / (4 * a))
        elif l == 3:
            R = 1 / (768 * np.sqrt(35)) * np.power(
                (r / a), 3) * np.exp(-r / (4 * a))
    return np.round(R, 5)
#####################################################################
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
                zcount+=1
            # add the inner most lists to the second lists
            xrow.append(xxrow)
            yrow.append(yyrow)
            zrow.append(zzrow)
        
            # increase y point
            yval+= ystep
            ycount+=1
        # add the second lists to the returned lists
        xr.append(xrow)
        yr.append(yrow)
        zr.append(zrow)
    
        # increase x point
        xval+=xstep
        xcount+=1
        
    return [xr, yr, zr]


###########################################################
def magni(im):
    v = np.vectorize(round)
    real = im.real
    imag = im.imag
    magnitude = (real**2 + imag**2)**0.5 #calculates magnitude of radial and imaginary component)
    
    return v(magnitude,5)

##################################################
def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    a=c.physical_constants['Bohr radius'][0]
    v = np.vectorize(round)
    lists = np.array (mgrid3d(-roa,roa,Nx,-roa,roa,Ny,-roa,roa,Nz))
    #print(lists)               
    
    x = v(lists[0],5) #returns x list from lists
    y = v(lists[1],5) #returns y list from lists
    z = v(lists[2],5) #returns z list from lists

    vs = np.vectorize(cartesian_to_spherical) #vectorize coordinates
    r,t,p = vs(x,y,z) # returns radius, theta, phi in vector form
    #print(r,'radius',t,'theta',p,'phi')
    
    vr = np.vectorize(radial_wave_func) #vectorize radial wave functions
    r_normal = r * a #denormalizes radius 
    r_func = vr(n,l,r_normal) #returns RADIAL solution in vector form
    #print(r_func,'radial')
    
    va = np.vectorize(angular_wave_func) #vectorize angular wave functions
    a_func = va(m,l,t,p) #returns ANGULAR solution in vector form
   # print(a_func,'angular')
    
    if m<0:
        angular = 1j/(2**(0.5)) * (a_func - ((-1**m) * va(abs(m),l,t,p)))
    elif m>0:
        angular = 1/(2**(0.5)) * (va(-abs(m),l,t,p) + ((-1**m) * a_func))
    else:
        angular = va(0,l,t,p)
        
    #print(angular,'1st')
    #print(angular[0],angular[1],'hello')
    angular = magni(angular)

    #print(angular)
    
    final_mag = v(((angular*r_func)**2),5)
    
  
    return (x,y,z,final_mag)


# Code to save the data to a file so that 
# you don't have to keep on computing it:

print('Test ')
x,y,z,mag=hydrogen_wave_func(2 ,1 ,1 ,8 ,2 ,2 ,2) #(n,l,m,roa,Nx,Ny,Nz)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)
print (x,y,z,mag)
x.dump('x_test.dat')
y.dump('y_test.dat')
z.dump('z_test.dat')
mag.dump('den_test.dat')


# Mayavi code:

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

###Volume slicer code:
import numpy as np

from traits.api import HasTraits, Instance, Array, \
    on_trait_change
from traitsui.api import View, Item, HGroup, Group

from tvtk.api import tvtk
from tvtk.pyface.scene import Scene

from mayavi import mlab
from mayavi.core.api import PipelineBase, Source
from mayavi.core.ui.api import SceneEditor, MayaviScene, \
                                MlabSceneModel

################################################################################
# Create some data
data = np.load('den_test.dat')

################################################################################
# The object implementing the dialog
class VolumeSlicer(HasTraits):
    # The data to plot
    data = Array()

    # The 4 views displayed
    scene3d = Instance(MlabSceneModel, ())
    scene_x = Instance(MlabSceneModel, ())
    scene_y = Instance(MlabSceneModel, ())
    scene_z = Instance(MlabSceneModel, ())

    # The data source
    data_src3d = Instance(Source)

    # The image plane widgets of the 3D scene
    ipw_3d_x = Instance(PipelineBase)
    ipw_3d_y = Instance(PipelineBase)
    ipw_3d_z = Instance(PipelineBase)

    _axis_names = dict(x=0, y=1, z=2)


    #---------------------------------------------------------------------------
    def __init__(self, **traits):
        super(VolumeSlicer, self).__init__(**traits)
        # Force the creation of the image_plane_widgets:
        self.ipw_3d_x
        self.ipw_3d_y
        self.ipw_3d_z


    #---------------------------------------------------------------------------
    # Default values
    #---------------------------------------------------------------------------
    def _data_src3d_default(self):
        return mlab.pipeline.scalar_field(self.data,
                            figure=self.scene3d.mayavi_scene)

    def make_ipw_3d(self, axis_name):
        ipw = mlab.pipeline.image_plane_widget(self.data_src3d,
                        figure=self.scene3d.mayavi_scene,
                        plane_orientation='%s_axes' % axis_name)
        return ipw

    def _ipw_3d_x_default(self):
        return self.make_ipw_3d('x')

    def _ipw_3d_y_default(self):
        return self.make_ipw_3d('y')

    def _ipw_3d_z_default(self):
        return self.make_ipw_3d('z')


    #---------------------------------------------------------------------------
    # Scene activation callbaks
    #---------------------------------------------------------------------------
    @on_trait_change('scene3d.activated')
    def display_scene3d(self):
        outline = mlab.pipeline.outline(self.data_src3d,
                        figure=self.scene3d.mayavi_scene,
                        )
        self.scene3d.mlab.view(40, 50)
        # Interaction properties can only be changed after the scene
        # has been created, and thus the interactor exists
        for ipw in (self.ipw_3d_x, self.ipw_3d_y, self.ipw_3d_z):
            # Turn the interaction off
            ipw.ipw.interaction = 0
        self.scene3d.scene.background = (0, 0, 0)
        # Keep the view always pointing up
        self.scene3d.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleTerrain()


    def make_side_view(self, axis_name):
        scene = getattr(self, 'scene_%s' % axis_name)

        # To avoid copying the data, we take a reference to the
        # raw VTK dataset, and pass it on to mlab. Mlab will create
        # a Mayavi source from the VTK without copying it.
        # We have to specify the figure so that the data gets
        # added on the figure we are interested in.
        outline = mlab.pipeline.outline(
                            self.data_src3d.mlab_source.dataset,
                            figure=scene.mayavi_scene,
                            )
        ipw = mlab.pipeline.image_plane_widget(
                            outline,
                            plane_orientation='%s_axes' % axis_name)
        setattr(self, 'ipw_%s' % axis_name, ipw)

        # Synchronize positions between the corresponding image plane
        # widgets on different views.
        ipw.ipw.sync_trait('slice_position',
                            getattr(self, 'ipw_3d_%s'% axis_name).ipw)

        # Make left-clicking create a crosshair
        ipw.ipw.left_button_action = 0
        # Add a callback on the image plane widget interaction to
        # move the others
        def move_view(obj, evt):
            position = obj.GetCurrentCursorPosition()
            for other_axis, axis_number in self._axis_names.items():
                if other_axis == axis_name:
                    continue
                ipw3d = getattr(self, 'ipw_3d_%s' % other_axis)
                ipw3d.ipw.slice_position = position[axis_number]

        ipw.ipw.add_observer('InteractionEvent', move_view)
        ipw.ipw.add_observer('StartInteractionEvent', move_view)

        # Center the image plane widget
        ipw.ipw.slice_position = 0.5*self.data.shape[
                    self._axis_names[axis_name]]

        # Position the view for the scene
        views = dict(x=( 0, 90),
                     y=(90, 90),
                     z=( 0,  0),
                     )
        scene.mlab.view(*views[axis_name])
        # 2D interaction: only pan and zoom
        scene.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleImage()
        scene.scene.background = (0, 0, 0)


    @on_trait_change('scene_x.activated')
    def display_scene_x(self):
        return self.make_side_view('x')

    @on_trait_change('scene_y.activated')
    def display_scene_y(self):
        return self.make_side_view('y')

    @on_trait_change('scene_z.activated')
    def display_scene_z(self):
        return self.make_side_view('z')


    #---------------------------------------------------------------------------
    # The layout of the dialog created
    #---------------------------------------------------------------------------
    view = View(HGroup(
                  Group(
                       Item('scene_y',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       Item('scene_z',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       show_labels=False,
                  ),
                  Group(
                       Item('scene_x',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       Item('scene3d',
                            editor=SceneEditor(scene_class=MayaviScene),
                            height=250, width=300),
                       show_labels=False,
                  ),
                ),
                resizable=True,
                title='Volume Slicer',
                )


m = VolumeSlicer(data=data)
m.configure_traits()