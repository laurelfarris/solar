; Filename:         bp_read_fits.pro
; Last modified:    12 December 2016
; Programmer:       Laurel Farris
; Description:      Input path to fits files, string array of wavelengths,
;                       and x/y data range.
;                   Returns structure with header info and/or data array.


function bp_read_my_fits, path=path, wave=wave, num=num, nodata=nodata


    fls = file_search(path + "*" + wave + "A*.fits")
    if keyword_set(num) then fls=fls[0:num]
    read_sdo, fls, index, data, nodata=nodata

    if nodata eq 0 then begin
        x = 800
        y = 1800
        r = 1000

        my_data = data[ x:x+r, y:y+r, * ]

        save, my_data, filename = path + "cube_" + wave + ".sav"

    endif else begin
        restore, path + "cube_" + wave + ".sav"
    endelse

    wavelength = index.wavelnth
    obs_date = index.date_obs
    obs_time = index.t_obs
    xcen = index.xcen
    ycen = index.ycen



    return, s

end
