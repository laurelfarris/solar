; Programmer:           Laurel Farris
; Description:          Using (aligned) data cubes,
;                           run cross-correlation and save max value, along with
;                           x and y coordinates, timelag, and distance from reference pixel
; Last modified:        16 December 2016


pro bp_run_correlation, A, sav=sav


    for i = 3, 3 do begin

        cube = A[i].data

        ;; num images, array of possible timelags,
        t = (size(cube))[3]
        ;; Array of possible timelags [image number]
        ;tau = indgen(t)-(t/2)
        ;; possible timelags [minutes], using the observation time from fits header
        tau = (A[i].time)/60.
        ;; length of data dimensions 1 and 2
        s1 = (size(cube))[1]
        s2 = (size(cube))[2]


        ;x0 = 50 & y0 = 50
        ;x1 = 66 & y1 = 47
        ;x2 = 60 & y2 = 63
        ;timelag, cube[x0,y0,*], cube[x1,y1,*], tau, c, maxcor


        ;; Initialize arrays for values of interest.
        max_cc = fltarr(s1, s2, /nozero)
        max_tt = fltarr(s1, s2, /nozero)

        ;; Coordinates for center and four pixels around the center
        ;;      (kind of hacky at the moment... )
        xc = s1/2 & yc = s2/2
        x0 = [xc, xc+1, xc-1, xc, xc]
        y0 = [yc, yc, yc, yc+1, yc-1]

        resolve_routine, "timelag", /either

        for j = 0, n_elements(x0)-1 do begin
            
            for y = 0, s2-1 do begin
            for x = 0, s1-1 do begin

                ;; Run timelag.pro, returns maxcor=[tt, cc]
                timelag, cube[x0[j], y0[j], *], cube[x, y, *], tau, maxcor

                ;; Make 2D data arrays for cc and tt
                max_cc[x,y] = max_cc[x,y] + maxcor[1]
                max_tt[x,y] = max_tt[x,y] + maxcor[0]

                endfor
                endfor 

        endfor


        ;; Append cc and tt arrays to structure (A[i])
        A[i] = create_struct( 'cc', max_cc, 'tt', max_tt, A[i] )


    endfor

    if keyword_set(sav) then begin
        save, xc, yc, max_cc, max_tt, filename = path + 'cc_' + w + '.sav'
    endif

end
