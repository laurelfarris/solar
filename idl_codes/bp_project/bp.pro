; Filename:         bp.pro
; Last modified:    29 November 2016
; Programmer:       Laurel Farris
; Description:      Main program to run other bp procedures
;                   Should be able to run this from start to finish.


function bp, $
    ;path, waves, temps, x_cen, y_cen, $
    read_fits=read_fits, align=align, run_cc=run_cc, make_str=make_str, gr=gr


    path = "/solarstorm/laurel07/data/aia/"
    waves = ['94','131','171','193','211','304'] ;,'335']
    temps = ['6.8', '5.6, 7.0', '5.8', '6.2, 7.3', '6.3', '4.7']
    x = 1140 & y = 2360

	waves = ['211']

    ;; 1  Use procedure "bp_read_fits.pro" to read data and/or headers from fits files.
    if keyword_set(read_fits) then begin
		A = []
        resolve_routine, "bp_read_my_fits", /either
		foreach w, waves do begin
			s = bp_read_my_fits(path=path, wave=w, nodata=1)
			A = [A, s]
		endforeach
    endif

    fls = file_search(path + "cube_*.sav")
    for f, fls do begin
        restore, f
        s =


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

        tags = [ 'wavelength', 'temperature', 'x_ref', 'y_ref', 'radius', $
            'bp_im', 'cc_im', 'tt_im' ]
        A = []

        foreach w, waves, i do begin

            restore, path + 'cc_' + w + '.sav'
            s = create_struct( $
                tags, $
                w, temps[i], x0, y0, radius, cube, max_cc, max_tt )
            A = [A, s]
        endforeach


    endif


    ;; 5  Graphics
    if keyword_set(gr) then begin
        resolve_routine, "bp_graphics_test", /either
        bp_graphics_test, A, /make_images, j=1, make_colorbar=1, buffer=0, sav=0
        ;bp_graphics, /make_images, j=0, make_colorbar=1, buffer=0, path=path, sav=0
        ;bp_graphics, path=path, /make_plots,  j=3, make_colorbar=0, buffer=0
        return, A
    endif

end


A = bp( /read_fits)

;A = bp( path, waves, temps, x_center, y_center, /make_str, /gr)


end
