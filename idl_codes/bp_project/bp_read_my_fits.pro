; Filename:         bp_read_fits.pro
; Last modified:    07 December 2016
; Programmer:       Laurel Farris
; Description:      Input path to fits files, string array of wavelengths, and x/y data range.
;                   Returns headers and/or data arrays.
;                   Optional keywords to set depending on what header info you want.


pro bp_read_my_fits, path=path, get_data=get_data


    waves = ['94','131','171','193','211','304'] ;,'335']
    temps = ['6.8', '5.6, 7.0', '5.8', '6.2, 7.3', '6.3', '4.7']
    x = 1140 & y = 2360


    ;; Header

    foreach w, waves, i do begin
    
        fls = file_search(path + "*" + w + "A*.fits")
        read_sdo, fls, index, data, /nodata

        wavelength = index.wavelnth
        temperature = temps[i]
        obs_date = index.date_obs
        obs_time = index.t_obs
        xcen = index.xcen
        ycen = index.ycen

;        save, wavelength, temperature, obs_date, obs_time, xcen, ycen, $
;            filename = path + "header_" + waves[i] + ".sav"


    ;; Data

    if keyword_set(get_data) then begin
        r = 500
        x1 = x - r/2 & x2 = x1 + r
        y1 = y - r/2 & y2 = y1 + r

        my_data = data[ x1:x2, y1:y2, * ] 

        save, my_data, filename = path + "cube_" + waves[i] + ".sav"

    endif

    endforeach

       
end
