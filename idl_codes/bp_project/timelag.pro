
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

PRO timelag, x, xs, tau, c, maxcor

    maxcor=FLTARR(2)
    c = FLTARR( N_ELEMENTS(tau) )
    mx = MEAN(x)
    mxs = MEAN(xs)  
      
    ;; Calculate correlation for each possible timelag
    FOR i=0, N_ELEMENTS(tau)-1 DO BEGIN
         
        c[i] = TOTAL( (x-mx ) * SHIFT( (xs-mxs), tau[i] ) ) / $
               SQRT( TOTAL( (x-mx)^2 ) * TOTAL( (xs-mxs)^2 ) )
              
    ENDFOR

    ; window, 1
    ;PLOT, tau, c, yrange=[0,1], ytitle="max correlation", xtitle="timelag"
    ;p = plot(tau, c,  ytitle="max correlation", xtitle="timelag")

    ;; Save highest correlation value (bestcor) along with the corresponding
    ;;     timelag (tau(bestcor)).    

    bestcor=WHERE(c EQ MAX(c))
    IF N_ELEMENTS(bestcor) NE 1 THEN BEGIN
        ;PRINT,tau(bestcor),c(bestcor)
        bestcor=MEDIAN(bestcor)
    ENDIF

    ;Assign bestcor and its tau to maxcor (output)
    maxcor[0] = tau[bestcor]
    maxcor[1] = c[bestcor]


    ;print, 'line 1 lags line 2 by number of pixels corresponding to peak of graph'
   
END
