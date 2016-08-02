import numpy as np
from scipy.interpolate import interp2d


def shift_sub(image, x0, y0):
    '''
    Purpose:            Shift a (2D) image with subpixel accuracies
    Calling sequence:   Result = shift_sub(image, x0, y0)
    Notes:              Thoroughly converted from the IDL version
                        (whose syntax is in docstrings right above the python bits),
                        but not very efficiently.
    Last updated:       07 July 2016
    '''

    image = np.array(image)
    if int(x0)-x0 == 0. & int(y0)-y0 == 0.:
        image = np.roll(image, x0, axis=1)
        image = np.roll(image, y0, axis=0)
        return image

    ''' Get dimensions of image '''
    s = image.shape
    x = np.broadcast_to( np.arange(s[1]), (s[0], s[1]) )
    y = (np.broadcast_to( np.arange(s[0]), (s[1], s[0]) )).transpose()

    ''' Set interpolation values '''
    x = np.max([0, (x-x0), (s[1]-1.)])
    y = np.max([0, (y-y0), (s[0]-1.)])

    ''' return interpolated image '''
    return interp2d(x1, y1, image, kind='cubic')


def alignoffset(image, reference):
    ''' Determine the offsets of an image with respect to a reference image '''
    si = image.shape
    sr = reference.shape

    if si[1] != sr[1] & si[0] != sr[0]:
        print 'Incompatible Images : alignoffset'
        return [0, 0.]

    nx = 2.**int(np.log(si[1])/np.log(2.))
    nx = nx*(1+(si[1] > nx))
    ny = 2**int(np.log(si[2])/np.log(2.))
    ny = ny*(1+(si[2] > ny))


    image1 = image - np.mean(image)
    reference1 = reference - np.mean(image)
    if nx != si[1] | ny != si[2]:
        image1 = congrid(image1, nx, ny, cubic=-0.5)
        reference1 = congrid(reference1, nx, ny, cubic=-0.5)
    return cor


def align_cube3(cube):
    ''' Finished! Needs to be tested though '''
    sz = cube.shape
    ''' Use middle image as reference (3D --> 2D) '''
    ref = np.reshape(cube[:,:,(sz[2])/2], (sz[0], sz[1]))
    shifts = np.zeros((sz[2], 2))

    print "Start: " + str(datetime.now())
    for i in range(sz[2]-1):
        offset = alignoffset(cube[:,:,i], ref)
        cube[:,:,i] = shift_sub(cube[:,:,i], -offset[0], -offset[1])
        shifts[:,i] = -offset
    print "Finish: " + str(datetime.now())
    x_sdv = np.std(shifts[0,:])
    y_sdv = np.std(shifts[1,:])

    print "x stddev: {:.4f}".format(x_sdv)
    print "y stddev: {:.4f}".format(y_sdv)


    return 0
