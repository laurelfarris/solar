; Filename:         bp_read_fits.pro
; Last modified:    16 December 2016
; Programmer:       Laurel Farris
; Description:      Read header info from fits files and either read data as well or
;                       restore data from a .sav file
;                   Returns array of structures, one for each wavelength.
;                   Takes a minute or two to run... should only have to do this once
;                       for each IDL session.

; Keywords:         fname: partial name of file to be saved or restored
;                   waves: ARRAY of (string) wavelengths
;                   num: number of fits files to be read for each wavelength (optional)
;                   get_data: Set to use "read_sdo" to read data from fits files (optional)


function bp_read_my_fits, $
    path=path, waves=waves, fname=fname, num=num, get_data=get_data


    print, ''
    t1 = systime(/seconds)
    print, "Start: ", systime()

    A = []

    foreach wave, waves, i do begin

        print, wave

        ; file to save as or restore
        my_name = fname + wave + ".sav"
        fls = (file_search(path + "*" + wave + "A*.fits"))[0:num-1]


        ;; Data

        if keyword_set(get_data) then begin
            ; Read data from fits files
            cube = []
            foreach f, fls do begin
                read_sdo, f, index, data
                ; Lower left coords and dimensions (r) of coronal hole
                ; = image_location for graphic
                x = 800 & y = 1800 & r = 1000
                cube = [ [[cube]], [[ data[ x:x+r-1, y:y+r-1, * ] ]] ]
            endforeach
            save, cube, filename = path + my_name

        endif else begin
            ; Restore data from saved files
            restore, path + my_name

            ;; Trim coronal hole data cube down to BP of interest, with dimensions r x r
            r = 100
            x_start = 280 & x_end = x_start + r
            y_start = 780 & y_end = y_start + r

            cube = temporary(cube[x_start:x_end-1, y_start:y_end-1, *])

        endelse


        ;; Header (run whether reading fits data or restoring saved data)

        read_sdo, fls, index, data, /nodata

        s = { $
            wavelength: index[0].wavelnth, $
            xcen: index[0].xcen, $
            ycen: index[0].ycen, $
            time: strmid(index.date_obs, 18, 4) + 60.*strmid(index.date_obs, 14, 2), $
            data: cube[*, *, 0:num-1] }

        ; Should make A a structure instead, with tag for date and one for each wavelength.
        ;date: strmid(index[0].date_obs, 0, 10), $
        A = [A, s]

    endforeach

    t2 = systime(/seconds)
    print, "Finish: ", systime()
    print, format='("Took a total of ", F0.2 , " seconds.")', t2 - t1
    return, A

end
