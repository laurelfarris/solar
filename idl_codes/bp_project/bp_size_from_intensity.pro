
function intensity
    ;; Intensity of central pixel only
    ;; Last modified: 28 March 2016

    ; (temporarily making this a function because I added it to 'lightcurve_BPs.pro'
    ; for the purpose of condensing all my codes.)

    ;;; Values needed from data cube
    t = (size(cube))[3]
    tau = indgen(t)-(t/2)
    pixels = (size(cube))[1]

    ;;; Pixel values (bright points in coronal hole)
    x = [240,650,112,729]
    y = [1730,1340,1792,1447]


    file = 'lc.dat'
    openw, mylun, /get_lun, file

    for i = 0,299 do begin
        printf, mylun, i, cube[x[0],y[0],i]
    endfor

    free_lun, mylun

    end





;; begin lightcurve_BPs.pro :

; The purpose of this code is to produce a lightcurve
; for a bright point. Each pixel that is considered part
; of the BP (i.e. higher than some predetermined threshold)
; is added to the total sum for that time point.
; The total sum is then written to file to be read in for 
; plotting


; Open file for writing
file = 'bp1_lc_size.dat'
openw, mylun, /get_lun, file

; Values needed from data cube
t = (size(cube))[3]
tau = indgen(t)-(t/2)
pixels = (size(cube))[1]

; Pixel values
x = 240
y = 1730

; Define radius of pixels that may contain the BP
s = 20
threshold = 150



;; Define the bright point data cube
bp = cube[x-s:x+s, y-s:y+s, *]
length = n_elements(bp[*,0,0])

; Set mask to array size of bp, all elements=0
mask = intarr(length, length, t)

; Array that only has values greater than threshold
;mask[where(bp gt threshold, /NULL)] = 1
;bp = bp*mask

for n = 0, t-1 do begin
    ii=0
    tot=0
    for x0 = x-s, x+s do begin
        jj=0
        for y0 = y-s, y+s do begin
            ;print, jj
            if bp[ii,jj,n] ge threshold then begin
                mask[ii,jj,n] = 1
                tot++
            endif
            jj++
        endfor
        ii++
    endfor
    bp[*,*,n] = bp[*,*,n] * mask[*,*,n]
    printf, mylun, n+1, tot, total(bp[*,*,n])
endfor

free_lun, mylun


;; Initiate total intensity value
;sum = 0
;for n = 0,t-1
;    for i = x-s, x+s do begin
;        for j = y-s, y+s do begin
;            if cube[i,j,n] gt threshold then begin
;                sum = sum + cube[i,j,n]
;            endif
;        endfor
;    endfor

;; write sum to file, then increase n


end
