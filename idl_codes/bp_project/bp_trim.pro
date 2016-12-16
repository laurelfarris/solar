; Programmer:           Laurel Farris
; Description:          Trim coronal hole data down to BP of interest
;                       Separate from bp_read_fits because want to do this quickly,
;                           but not necessarily every time, i.e. pick different BP.
; Last modified:        15 December 2016


pro bp_trim, A


    r = 100
    x_start = 280 & x_end = x_start + r
    y_start = 780 & y_end = y_start + r

    ;; Trim CH data cube to r x r, centered at a BP
    sub = A
    A[*].data = A[*].data[x_start:x_end, y_start:y_end, *]


end
