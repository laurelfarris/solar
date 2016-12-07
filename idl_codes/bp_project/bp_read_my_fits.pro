; Filename:         bp_read_fits.pro
; Last modified:    02 December 2016
; Programmer:       Laurel Farris
; Description:      Input path to fits files, string array of wavelengths, and x/y data range.
;                   Returns headers and/or data arrays.
;                   Optional keywords to set depending on what header info you want.


pro bp_read_my_fits, path=path, x_center=x_center, y_center=y_center, wave=wave, $
    my_header=my_header, my_data=my_data

    fls = file_search(path + "*" + wave + "A*.fits")
    read_sdo, fls, index, data
    

    ;; Data

    print, "Start time for setting data range: ", systime()
    ;; Change these according to how big you want 2D data to be
    width = (size(data))[1] - 1
    length = (size(data))[3] - 1
    x1 = 0 & y1 = 0 & z1 = 0
    x2 = x1 + width & y2 = y1 + width & z2 = z1 + length


    my_data = data[ x1:x2, y1:y2, z1:z2 ] 
    print, "End time for setting data range: ", systime()


    ;; Header

    my_header = { $
        wavelength:index.wavelnth, $
        instrument:index.instrume, $
        obs_date:index.date_obs, $
        obs_time:index.t_obs, $
        cdelt1:index.cdelt1, $
        cdelt2:index.cdelt2, $
        naxis1:index.naxis1, $
        naxis2:index.naxis2, $
        xcen:index.xcen, $
        ycen:index.ycen $
    }

    save, data, filename = path + "cube_" + waves[i] + ".sav"

       
end
