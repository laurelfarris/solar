; Programmer:           Laurel Farris
; Description:          Using (aligned) data cubes,
;                           run cross-correlation and save max value, along with
;                           x and y coordinates, timelag, and distance from reference pixel
; Last modified:        05 December 2016


; Pixel coordinates for bp1
;x = 240
;y = 1730
; 'radius'
;r = 50
; open file for writing
;file = 'size.dat'
;openw, mylun, /get_lun, file
;for x0 = (x-r),(x+r) do begin
;    for y0 = (y-r),(y+r) do begin
;        d = sqrt( (x-x0)^2 + (y-y0)^2)
;        intensity = cube[x0,y0,0]
;        printf, mylun, d, intensity
;    endfor
;endfor
;free_lun, mylun


;; still need this?
; Open file to save data
        ;file = '~/research/new_codes/bp_size/' + wave[i] + '_bp_sizes.dat'
        ;openw, mylun, /get_lun, file
                ;printf, mylun, x, y, r, maxcor[1], maxcor[0]
        ;free_lun, mylun


pro bp_run_correlation, cube, $
    x0, y0, radius, max_cc, max_tt


    ;; Called individually for each wavelength/cube (for now).
    ;; Eventually should take structure that includes wavelength, time of obs, etc.

    ;; num images, timelag, length of data dimension
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



    ;; Center coos, change these for a different region
;    x1 = 50 & y1 = 50
;    x2 = 66 & y2 = 47
;    x3 = 60 & y3 = 63


end
