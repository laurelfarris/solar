
;+ 
;
;PURPOSE    To calculate the maximum crosscorrelation of two lightcurves
;
;USEAGE     timelag,timeseries1,timeseries2,array of possible timelags, result
;
;INPUT      two time series , array of possible timelags (in terms of pixels)
;
;OUTPUT     result, an array of cross correlation values for each timelag
;
;EXAMPLE    IDL>tau=findgen(100)/10 -5  ;creates a array of 100 elements each 0.1 apart
;   	                                 from -5 to 4.9
;   	    IDL>timelag,time1,time2,tau,c
;AUTHOR     R.T.James McAteer and Peter T. Gallager
;   	    august 2001
;   version 1.0 asks for peak of graph
;   version 1.1 calculates and records peak of graph. realised that there is no 
;   	    	point in having tau in terms of less than integer values. SHIFT 
;   	    	function just moves the elements along an integer number.
;-

PRO timelag, x, xs, tau, maxcor;, xx, yy ; input x,xs,tau... output maxcor(2x1)

;ii = string(xx)
;jj = string(yy)
  
maxcor=FLTARR(2)
c = FLTARR( N_ELEMENTS(tau) )
    
mx = MEAN(x)
mxs = MEAN(xs)  
  
;; Calculate correlation for each possible timelag
FOR i=0, N_ELEMENTS(tau)-1 DO BEGIN
     
  c( i ) = TOTAL( ( x - mx ) * SHIFT( ( xs - mxs ), tau( i ) ) ) / $
           SQRT( TOTAL( ( x - mx )^2 ) * TOTAL( ( xs - mxs )^2 ) )
          
ENDFOR

;; Save highest correlation value (bestcor) along with the corresponding
;;     timelag (tau(bestcor)).    

bestcor=WHERE(c EQ MAX(c))
IF N_ELEMENTS(bestcor) NE 1 THEN BEGIN
	;PRINT,tau(bestcor),c(bestcor)
	bestcor=MEDIAN(bestcor)
ENDIF

;Assign bestcor and its tau to maxcor (output)
maxcor[0]=tau[bestcor]
maxcor[1]=c[bestcor]
   
END

;cc = string(c(bestcor))
;tt = string(tau(bestcor))

; Plot all correlation values vs. timelag
;!P.MULTI=[0,1,1,0,0]
;window,0,xsize=850,ysize=250
;color=0
;background=255
;charsize=1.25
;PLOT,tau,c, yrange=[min(c),max(c)],$
;    color=color,background=background,charsize=charsize, $
;    xstyle=1,ystyle=1, ytitle='correlation', $
;    xtitle='timelag     coords = ('+ii+', '+ jj+'), cc = '+cc+ $
;                        '   tau = '+tt
