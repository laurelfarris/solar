; Filename:         bp.pro
; Last modified:    29 November 2016
; Programmer:       Laurel Farris
; Description:      Main program to run other bp procedures
;                   Should be able to run this from start to finish.


function bp, $
    path, x_center, y_center, waves, temps, $
    read_fits=read_fits, align=align, run_cc=run_cc, make_str=make_str, gr=gr


    ;; 1  Use procedure "bp_read_fits.pro" to read data and/or headers from fits files.
    if keyword_set(read_fits) then begin
        resolve_routine, "bp_read_my_fits"
        ;bp_read_my_fits, path=path, x=x, y=y, wave=wave, $
        ;    my_header=h, my_data=d
    endif


    ;; 2  Use procedure "bp_align.pro" to align the data
    if keyword_set(align) then begin
        resolve_routine, "bp_align", /is_function
        foreach w, wave do begin
            restore, path + "cube_" + w + ".sav"
            cube = bp_align(data, sav=0)
            save, cube, filename=path + "aligned_" + w + ".sav"
        endforeach
    endif


    ;; 3  Run cross-correlation on aligned data cubes
    if keyword_set(run_cc) then begin
        resolve_routine, "bp_run_correlation", /either

        foreach w, waves, i do begin

            restore, path + 'aligned_' + w + '.sav'
            cube = cube[200:300, 200:300, *]
            ; may be able to return just one array here, but doesn't matter for now
            bp_run_correlation, cube, $
                x0, y0, radius, max_cc, max_tt
            save, cube, x0, y0, radius, max_cc, max_tt, filename = path + 'cc_' + w + '.sav'

        endforeach
        return, 0
    endif

    ;; 4  Make Structures
    if keyword_set(make_str) then begin

        tags = [ 'wavelength', 'temperature', 'x_ref', 'y_ref', 'radius', 'max_cc', 'max_tt' ]
        A = []

        foreach w, waves, i do begin
            print, i
            restore, path + 'cc_' + w + '.sav'
            s = create_struct( $
                tags, $
                w, temps[i], x0, y0, radius, max_cc, max_tt )
            A = [A, s]
        endforeach

        return, A

    endif


    ;; 5  Graphics
    if keyword_set(gr) then begin
        resolve_routine, "bp_graphics", /either
        bp_graphics, A, /make_images, make_colorbar=0, buffer=0, sav=0
        ;bp_graphics, /make_images, j=0, make_colorbar=1, buffer=0, path=path, sav=0
        ;bp_graphics, path=path, /make_plots,  j=3, make_colorbar=0, buffer=0
        return, 0
    endif

end


;; Main level code
path = "/solarstorm/laurel07/data/aia/"
temps = ['6.8', '5.6, 7.0', '5.8', '6.2, 7.3', '6.3', '4.7']
waves = ['94','131','171','193','211','304'] ;,'335']
x_center = 1140 & y_center = 2360

;;; also need desired range to align and to cut out for analysis?

A = bp( path, x_center, y_center, waves, temps, /make_str )


end
