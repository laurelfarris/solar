import numpy as np
from scipy.interpolate import interp2d


def shift_sub(image, x0, y0):
    '''
    Purpose:            Shift a (2D) image with subpixel accuracies
    Calling sequence:   Result = shift_sub(image, x0, y0)
    Notes:              Thoroughly converted from the IDL version,
                        although dimensions are questionable
    Last updated:       04 August 2016
    '''

    if int(x0)-x0 == 0. & int(y0)-y0 == 0.:
        image = np.roll(image, x0, axis=1)
        image = np.roll(image, y0, axis=0)
        return image

    s = image.shape
    x = np.matrix(np.ones(s[0])).reshape(s[0], 1) * np.matrix(np.arange(s[1]))
    y = np.matrix(np.arange(s[0])).reshape(s[0], 1) * np.matrix(np.ones(s[1]))

    ''' Set interpolation values '''
    x1 = np.max([0, (x-x0), (s[1]-1.)])
    y1 = np.max([0, (y-y0), (s[0]-1.)])

    ''' return interpolated image '''
    return interp2d(x1, y1, image, kind='cubic')


def alignoffset(image, reference):
    ''' Determine the offsets of an image with respect to a reference image '''
    si = image.shape
    sr = reference.shape

    ''' Check that images have the same dimensions '''
    if not (si[1] == sr[1] and si[0] == sr[0]):
        print 'Incompatible Images : alignoffset'
        return [0, 0.]

    nx = 2**int(np.log(si[1])/np.log(2.))
    nx = nx * (1 + (si[1] > nx))
    ny = 2**int(np.log(si[0])/np.log(2.))
    ny = ny * (1 + (si[0] > ny))

    image1 = image - np.mean(image)
    reference1 = reference - np.mean(image)
    if nx != si[1] or ny != si[2]:
        image1 = congrid(image1, nx, ny, cubic=-0.5)
        reference1 = congrid(reference1, nx, ny, cubic=-0.5)
    
    sigma_x = nx/6.
    sigma_y = ny/6.
    xx = (np.matrix(np.arange(nx))).reshape(nx.shape[0],1) * np.matrix(np.ones(ny))
    xx = xx - nx * (xx > nx/2)
    yy = (np.matrix(np.ones(nx))).reshape(nx.shape[0],1) * np.matrix(np.arange(ny))
    yy = yy - ny * (yy > ny/2)
    ### window = np.roll()
    window = np.sqrt(window)

    

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
