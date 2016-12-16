; Programmer:           Laurel Farris
; Description:          Using (aligned) data cubes,
;                           run cross-correlation and save max value, along with
;                           x and y coordinates, timelag, and distance from reference pixel
; Last modified:        13 December 2016



pro bp_run_correlation, A, $
    x0, y0, radius, max_cc, max_tt


    foreach w, waves, i do begin


        ;; num images, array of possible timelags, length of data dimensions 1 and 2
        ;; Eventually use actual obs. times for tau
        t = (size(cube))[3]
        tau = indgen(t)-(t/2)
        side = (size(cube))[1]


        ;; Set up "reference" pixel as the brightest in first image in time series.
        ref = cube[*,*,0]
        location = where( ref eq max(ref) )
        x0 = fix(array_indices(ref, location))[0]
        y0 = fix(array_indices(ref, location))[1]

        ;; Initialize arrays for values of interest.
        radius = []
        max_cc = []
        max_tt = []

        ;; Run timelag.pro and save correlation, timelag, and radius values
        for y = 0, side-1 do begin
            for x = 0, side-1 do begin

                timelag, cube[x0, y0, *], cube[x, y, *], tau, maxcor

                radius = [radius, sqrt((x0-x)^2 + (y0-y)^2 ) ]
                max_cc = [max_cc, maxcor[1]]
                max_tt = [max_tt, maxcor[0]]

            endfor 
         endfor 

    endforeach

end
