; Filename:         general_imaging.pro
; Last modified:    21 November 2016
; Programmer:       Laurel Farris
; Description:      template to use for any image or plot
; Notes:            position must be called as a property, otherwise all images appear
;                       in the same place on top of each other


;; Window
w = window($
    dimensions=[700,820], /buffer, title="", $
    location=[x_offset, y_offset])  ; window's screen offset (not the actual graphic)

; window methods
w.window.SetCurrent


;; Dimensions

;n = num_images in a single dimension
;w = length of window in pixels
;gap = 50 pixels
;image_length = ( w - (n+1)*gap ) / n

;x1 = gap & y1 = gap
;x2 = x1 + image_length + gap
;x3 = x2 + image_length + gap ... etc.

;position1 = [x1, y1, x1 + image_length, y1 + image_length]
;position2 = [x2, y2, x2 + image_length, y2 + image_length]
; etc...

;; Imaging

im = image(data, $
    x, y, $
    /current, /device, $
    min_value=min_value, max_value=max_value, $
    xrange=, yrange=, $
    image_dimensions=[width (ncols), height (nrows)], $  ;; affects labels, not physical size of graphic, $
    image_location=[x, y], $
    title="title", $
    axis_style=2, font_size=8, $
    aspect_ratio=x/y, $
    ;layout=[ncols, nrows, index], $
    ;margin=[left, bottom, right, top], $
    location=[x_offset, y_offset], $
    dimensions=[width, height], $
    scale_center=n, scale_factor=n, $
    /overplot, $
    /order, $
    xtickdir=1, xticklen=0.03, xsubticklen=n, xmajor=n, xminor=n, xtickinterval=20, $
    xtitle="title", xtickfont_name="x", xtickfont_size="x", xtickfont_style=n, $
    xcolor="", xtext_color="", xtext_orientation="", xtextpos="", xshowtext=1, $
    xlog="", xthick="", xtickinterval="", xticklayout="", xtickunits="", $
    xstyle="", xtickname="", xtickformat="", xtickvalues="", $
    name="", $  ;; Use this to retrieve image using bracket notation! ,$
    rgb_table=color_table $

    )
    im.position = [x, y]
    im.scale, 2, 2, /reset  ;; Need a way to get default dimensions and set this accordingly!

end

;;; Colorbar

cbar = colorbar( $
    /data, $
    /device, $
    /normal, $
    /relative, $
    target=im, $
    orientation=0|1, $
    position=[], $
    rgb_table=[[r], [g], [b]] $
    )


cbar.range=[min,max]    ; ignored if TARGET is set
cbar.major=-1           ; number of major tick marks (IDL decides); 0=no tick marks
cbar.minor=-1           ; number of minor tick marks (IDL decides); 0=no tick marks
cbar.tickinterval=      ; ignores MAJOR
cbar.tickname=          ;string array of tick LABELS
cbar.tickvalues=0       ;array of tick mark LOCATIONS (IDL decides)
cbar.tickformat=        ;(see AXIS function)
cbar.ticklayout=0       ;axis line, tick marks, and tick labels; 1=labels; 2=box around labels

cbar.tickdir=0|1    ; Draw tickmarks facing inwards|outwards
cbar.ticklen=0.25   ; Relative to width of cbar... I think
cbar.subticklen=0.5 ; Relative to length of major ticks
cbar.thick=1        ; 0-10 increases thickness

cbar.clip=1
cbar.taper=2

cbar.textpos=1  ; 1 = tick labels and axis title above axis (0 = below...)
cbar.text_orientation=0  ; angle [degrees] of tick mark labels
cbar.title=""
cbar.font_name=""   ;"Times"|"Helvetica"|...
cbar.font_size=16   ;target font size appears to carry over to colorbar font size
cbar.font_style=""  ;"normal"|"bold"|"italic"|"bold italic"
cbar.color=""       ;color of border and tick marks
cbar.text_color=""  ;color of axis text (=COLOR by default)
cbar.border=0       ;1 = border around colorbar

cbar.window  ; (get only)
cbar.hide=0|1

;;; Contour
;
;;cont = contour(data, x, y)
;;cont.n_levels=
;;cont.c_value=
;
;;cont = contour(bp1, xrange, yrange, c_value=2,n_levels=2,overplot=1)
;;center=symbol(/data_array,x[0],y[0],symbol=3,sym_size=6)
;

;;;; PLOT procedure

!P.COLOR = 0
!P.BACKGROUND = 255

plot, x, y, background=255

; PLOT function

function make_colorbar, my_target, my_rgb_table, my_title
    cbar = colorbar( target=my_target, rgb_table=my_rgb_table, title=my_title )
    cbar.orientation=0
    cbar.position=[0.05, 0.80, 0.95, 0.84]
    cbar.border=1
    cbar.font_style='italic'
    cbar.textpos=1
    cbar.ticklen=0.3
    cbar.subticklen=0.5
    cbar.major=11
    cbar.minor=4
    ;cbar.tickinterval=20.0
    ;cbar.tickvalues=make_array( 11, start=min_value, increment=(max_value-min_value)/10. )
    end


p = scatterplot(r, c, axis_style=2, /current)
;; Adjust min/max of y range
;;p.max_value =
;;p.min_value =

;; Set padding between data and axes. THIS OVERRIDES [XY]RANGE! But not min|max_value.
;;p.xstyle = 0|1|2|3

;; Set range of both x and y values
;;p.xrange =
;;p.yrange =


;; Adjust apparent ratio of axes (using their ORIGINAL data values,
;;      not the range being plotted... or not. Maybe just need to set aspect_ratio
;;      before setting x and y ranges, according to the range values, and NOT the originals.)
;;p.aspect_ratio = n

;;p.position = [x[i], y[i]]
;;p.scale, 0.4, 0.4

;;p.rgb_table = color_table.(3)
;;p.magnitude = t  ; vector that determines color (rgb_table) of each symbol
;;p.color =  ; color of plot line (PLOT only)
;;p.vert_colors =  ; (PLOT only)

;;p.symbol="dot")
;;p.sym_color =
;;p.sym_filled = 1  ; set to fill symbols
;;p.sym_fill_color =  ; matches sym_color by default
;;p.sym_increment = 1  ; INT, number of plot vertices between symbols
;;p.sym_size = 2.0
;;p.sym_thick =  ; = 1.0 --> 10.0

;;p.name = ""  ; use to retrieve graphic using array index notation
;;p.title = "$\lambda$ = " + strtrim(string(waves[i]),2) +  " $\AA$, log(T) = " + temps[i] + " K"
;;p.font_size=fontsize
;;p.tickfont_size=10
;;p.xtickdir = 0|1       ; ticks facing in|out
;;p.xtickfont_name = 'times'
;;p.xtickformat
;;p.xticklen = 0.03
;;p.yticklen = 0.03
;;p.xsubticklen = 0.5  ; = 0.5 (half of major tick length by default)
;;p.xmajor = 9   ; number of major tick marks
;;p.xminor = 5   ; number of minor tick marks (between each major tick mark)
;;p.ymajor = 11
;;p.xminor = 5
;;p.xtickfont_size = 10     ; size of tick labels and axis labels (depending on order?)
;;p.ytickfont_size = 10
;;p.xtitle = "radius [pixels]"
;;p.ytitle = "maximum cross-correlation"

my_colorbar =  make_colorbar(p, color_table.(3), cbar_title[j])

STOP




end
