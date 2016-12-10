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
;;	      Slight alterings by Laurel Farris 2015, commented with 
;;               double semi-colons (;;)
;
;-
PRO align_cube3, cube, x_sdv, y_sdv ;quiet=quiet, shifts=shifts ... ?

sz = SIZE( cube ) ; For accessing data cube dimensions
ref = REFORM( cube[*,*,(sz[3]/2)] ) ;; Use middle image as ref
shifts = FLTARR( 2, sz[3] ) ;; shift in x and y (2) for every image (sz[3]).

;; Align to first image if no reference image is specified
;IF ( N_ELEMENTS(ref) EQ 0 ) THEN ref=REFORM( cube[*, *, 0] ) ELSE ref=ref 
;IF ~(quiet) THEN PRINT,'   image      x offset      y offset'

;PRINT, "Start:	", SYSTIME() ; Display time that code started running
FOR i = 0, sz[3]-1 DO BEGIN
;  	PRINT,i
   offset = ALIGNOFFSET( cube[*, *, i], ref )
    ;IF ~(quiet) THEN PRINT, i, offset[0], offset[1]
    ;IF ( offset[0] GT 30 ) THEN print, offset[0]
    ;IF ( offset[1] GT 30 ) THEN print, offset[1]
    ;IF abs(offset(0)) GT 30 THEN offset(0)=0.0
    ;IF abs(offset(1)) GT 30 THEN offset(1)=0.0
    cube[*, *, i] = ALIGN_SHIFT_SUB( cube[*, *, i], -offset[0], -offset[1] )
       ;; Not sure why offset values are set to be negative...
    shifts[*, i] = -offset
ENDFOR

;PRINT, "Finish: ", SYSTIME() ; Display time that code finished running
x_sdv = STDDEV( shifts[0,*] )
y_sdv = STDDEV( shifts[1,*] )
PRINT, FORMAT='("x stddev: ", F0.4)' , x_sdv
PRINT, FORMAT='("y stddev: ", F0.4)' , y_sdv

END
