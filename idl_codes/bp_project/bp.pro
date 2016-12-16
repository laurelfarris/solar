; Filename:         bp.pro
; Last modified:    13 December 2016
; Programmer:       Laurel Farris
; Description:      Main program to run other bp procedures
;                   Should be able to run this from start to finish.


function bp, output, $
    read_fits=read_fits, align=align, run_cc=run_cc, make_str=make_str, gr=gr


    path = "/solarstorm/laurel07/data/aia/"
    temps = ['6.8', '5.6, 7.0', '5.8', '6.2, 7.3', '6.3', '4.7']
    waves = ['94','131','171','193','211','304'] ;,'335']



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
    endif

end

path = "/solarstorm/laurel07/data/aia/"
temps = ['6.8', '5.6, 7.0', '5.8', '6.2, 7.3', '6.3', '4.7']
waves = ['94','131','171','193','211','304','335']
waves = waves[0:5]

f = "coronal_hole_"
f = "aligned_"

;; 1  Use procedure "bp_read_fits.pro" to read data and/or headers from fits files.
resolve_routine, "bp_read_my_fits", /either
;A = bp_read_my_fits( path=path, waves=waves, fname=f, num=300, get_data=0)


;; 2  Use procedure "bp_align.pro" to align the data
resolve_routine, "bp_align", /either
;bp_align, A, path=path, waves=waves, sav=1


;; 3  Run cross-correlation on aligned data cubes
resolve_routine, "bp_run_correlation", /either
bp_run_correlation, A[3], sav=0


;; 4
;resolve_routine, "bp_graphics_test", /either

end
