;+
; ROUTINE:    align_cube3
;
; PURPOSE:    align a series of images in a data cube to
;             the first image
;
; USEAGE:     align_cube3, cube
;
; INPUT:      cube = array of images (x,y,t)
;
; OUTPUT:     cube = data aligned to the first image
 
; Example:    
;             
; AUTHOR:     Peter T. Gallagher, July 2001
;   	      Altered by James McAteer March 2002 with ref optional 
;                input
;             Altered by Shaun Bloomfield April 2009 with optional 
;                output of calculated shifts
;
;-

; Used by Laurel Farris;     Last modified:  13 December 2016


PRO align_cube3, cube, avg

    ;; Get number of images in data cube (length of third dimension, if you will).
    sz = (size(cube))[3]
    ;; Use middle image as ref
    ref = REFORM( cube[*,*,(sz/2)-1] )
    ;; 2xN array for shifts in x and y for every image, for a total of N images.
    shifts = FLTARR( 2, sz)


    PRINT, "Start:	", SYSTIME()
    FOR i = 0, sz-1 DO BEGIN
        
        ;print, i
        offset = ALIGNOFFSET( cube[*, *, i], ref )
        ;IF ~(quiet) THEN PRINT, i, offset[0], offset[1]
        ;IF ( offset[0] GT 30 ) THEN print, offset[0]
        ;IF ( offset[1] GT 30 ) THEN print, offset[1]
        ;IF abs(offset(0)) GT 30 THEN offset(0)=0.0
        ;IF abs(offset(1)) GT 30 THEN offset(1)=0.0
        cube[*, *, i] = ALIGN_SHIFT_SUB( cube[*, *, i], -offset[0], -offset[1] )
        shifts[*, i] = -offset
    ENDFOR

    PRINT, "Finish: ", SYSTIME()

    ;; Save the standard deviation in shifts (to account for both directions)
    ;;  to use as a test for when to stop the alignment.
    x_sdv = STDDEV( shifts[0,*] )
    y_sdv = STDDEV( shifts[1,*] )
    
    x_sdv = mean( abs( shifts[0,*] ))
    y_sdv = mean( abs( shifts[1,*] ))

    avg = MEAN([x_sdv, y_sdv])
    PRINT, FORMAT='("avg. shift: ", F0.4)' , avg

END
