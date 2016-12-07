; Programmer:       Laurel Farris
; Filename:         bp_align.pro
; Last modified:    28 November 2016
; Function(s):      align_cube3.pro, alignoffset.pro, align_shift_sub.pro
; Description:      Align images


function bp_align, data_in, path=path, wave=wave, sav=sav
;pro bp_align, path, wave, data_in, data_out, sav=sav


        cube = data_in

        ;; Do first alignment. Note this may take a while, depeding on size of cube
        align_cube3, cube, x, y  ;; don't actually need y, but whatev.
        stds = [x]
        align_cube3, cube, x, y
        stds = [stds, x]

        k = 1
        while (stds[k] lt stds[k-1]) do begin
            align_cube3, cube, x, y
            stds = [stds, x]
            k=k+1
        endwhile

        print, "Finished with alignment"


    ;; Now you have an aligned, limb-subtracted data cube!
    ;; Run cross-correlation procedure(s), or whatever analysis suits your fancy.

    return, cube

end
