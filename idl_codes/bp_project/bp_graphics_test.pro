; Filename:         bp_graphics.pro
; Last modified:    05 December 2016
; Programmer:       Laurel Farris
; Description:      Make images and plots of cc and tt for bp


pro bp_graphics, buffer=buffer, make_plots=make_plots, make_images=make_images, $
    j=j, make_colorbar=make_colorbar, sav=sav


    ;; Colors and other aesthetics

    bk = [000,000,000]
    wh = [255,255,255]
    rd = [204,000,000]
    og = [255,128,000]
    ye = [255,255,000]
    gr = [000,153,000]
    lg = [102,255,102]
    cy = [000,153,153]
    bl = [000,000,204]
    pr = [148,000,211]
    in = [075,000,130]

    color_table = { $
        im_colors:0, $
        cc_colors:colortable( [[wh], [bk]] ), $
        ;cc_colors2:colortable( [[wh], [rd], [og], [ye], [gr], [bl], [pr]]), $
        tt_colors:colortable([ [wh], [rd], [ye], [bl], [wh] ], $
            indices=[0, 1, 128, 254, 255], stretch=[0, 10, -10, 0] ), $
        plot_colors:colortable([ [rd], [0,0,0], [bl] ]) }

    fontsize = 8 & fontname = "Helvetica"


    ;; Data

    ; title = "$\lambda$ = " + w + " $\AA$, log(T) = " + temps[i] + " K"
    ; title = "Frame " + strtrim(string(i+start), 1) + " for $\lambda$ = " + waves[0] ]


;    my_title = []
;    my_data = []
;    foreach w, waves, i do begin
;
    ;; Restore aligned data set
;        restore, path + "aligned_" + waves[i] + ".sav"
;        s = (size(cube))[1]
;        z = 200
;        my_data = [ [[ my_data ]], [[ cube[z:s-z, z:s-z, 0] ]] ]
    ; ... This should be saved as a cube, just like cc and tt. Less confusing...

;    endforeach

    ;; Images of one wavelength over several time steps
    ;start = 42
    ;my_data = cube[*,*,start:start+5]

    ;my_data[where(my_data lt 0.0)] = 0.0

    ;; Change timelag from image number/cadence to minutes
    ;tt = (tt * 12.) / 60.

    my_data = x

    ;; Create structure of data cubes (images, cc images, and tt_images)
    d = { $
        im_data:my_data, $
        cc_data:cc, $
        tt_data:tt }

    ;; Cut off timelag for cc values less than 0.5
    d.tt_data[ where(cc lt 0.5) ] = -10000.0

    ;; Min/max values to plot for each data cube
    data_range = [ $
        [0, max(d.im_data)], $
        [0.0, max(d.cc_data)], $
        [min(tt), round(max(tt))], $
        [-150, 150] ]

    ;; Create graphics window
    wy = 830 & wx = wy * (8.5/11.0)
    ;wy = 600 & wx = wy
    w = window( dimensions=[wx, wy], location=[0, 0], buffer=buffer )

    ;; Create coordinates that can be used for any size or number of graphics.
    ;; First figure out how much space you need between bottom/left and axis labels.
    ;; Then length of side is four times that.
    n = 3
    gap = 50.
    side = (wy - gap * 4.) / n
    x1 = gap & x2 = x1 + side + gap
    y1 = gap & y2 = y1 + side + gap & y3 = y2 + side + gap
    ;; Still not sure of better way to call position coos in loop...
    x = [x2, x2, x2, x1, x1, x1]
    y = [y1, y2, y3, y1, y2, y3]

    ;; Axis labels
        labels = [ $
            'x [pixels]', $
            'y [pixels]', $
            'radius [pixels]', $
            'radius [arcseconds]', $
            'radius [km]', $
            'intensity [counts, arbitrary]', $
            'maximum cross-correlation', $
            'timelag [cadence units]', $
            'timelag [minutes]' ]


    ;; Start graphics

    for i = 0, n_elements(A)-1 do begin

        my_title = "$\lambda$ = " + waves[i] + " $\AA$, log(T) = " + temps[i] + " K"

        if keyword_set(make_images) then begin
        ;;; color x0, y0 in every image!

            n = sqrt(n_elements(A[i].max_cc))
            my_data = x
            cc = reform(A[i].max_cc, n, n)
            tt = reform(A[i].max_tt, n, n)

            p = image( cc, $
                /current, /device, axis_style=2, $
                ;image_location=[1090, 2580], $
                position = [ x[i], y[i], x[i] + side, y[i] + side] $
                )
        endif


        if keyword_set(make_plots) then begin

            r = A[i].radius
            c = A[i].max_cc
            t = A[i].max_tt

            ; Scale timelag by 1/3 ;; or use some array manipulation to sort, then cut
            ;r = r[where(abs(t) le 50)] ;c = c[where(abs(t) le 50)] ;t = t[where(abs(t) le 50)]

            ;intensity = transpose(d.(0)[1090:1190, 2580:2680,i])
            ;re_intensity = (reform( intensity, 10201 ))  ; /max(intensity)
            ;x_data = r
            ;y_data = re_intensity
            x_data = t[where(c ge 0.5)]
            y_data = c[where(c ge 0.5)]

            x_r = max(x_data) - min(x_data)
            y_r = max(y_data) - min(y_data)

            p = scatterplot(x_data, y_data, $
                /current, $
                /device, $
                axis_style=2, $
                position = [ x[i], y[i], x[i] + side, y[i] + side], $
                xstyle=1, ystyle=1, $
                aspect_ratio = (x_r)/(y_r), $
                magnitude = t, $
                symbol='dot', sym_filled = 1, sym_size = 1.0 $
                )
        endif


        ;; Set properties that apply to both images and plots.
        p.title=my_title
        p.font_size=fontsize
        ;p.xrange = [0, 35]
        ;p.yrange = [0, max(y_data)]
        ;p.min_value=data_range[0,j]
        ;p.max_value=max(d.(j)[*,*,i])
        ;p.rgb_table=color_table.(j)

        ;; Axes properties
        p.xtickdir=1 & p.xticklen=0.03 & p.xminor=5 & p.xtickinterval=(x_r/15)
        p.ytickdir=1 & p.yticklen=0.03 & p.yminor=5 & p.ytickinterval=(y_r/10)
        p.xtickfont_size=fontsize & p.ytickfont_size=fontsize


    endfor


    ;; Colorbar
    if keyword_set(make_colorbar) then begin

        cx1 = x2 + side + 0.5*gap
        cy1 = gap
        cx2 = cx1 + 0.5*gap
        cy2 = wy - gap

        cbar = colorbar( orientation=1, /device, position=[cx1, cy1, cx2, cy2] )

        ;cbar.rgb_table=color_table.(j))  ;; Is this needed for plots? Or at all?
        cbar.range=[ data_range[0, j], data_range[1,j] ]

        cbar.tickinterval=( data_range[1,j] - data_range[0,j] ) / 20
        cbar.ticklen=0.3
        cbar.subticklen=0.5

        cbar.textpos=1
        cbar.font_size=fontsize
        cbar.font_style="italic"
        cbar.title=labels[j]
        cbar.border=1

    endif

    x_title = text(0.5, 0.02, xlabel, $
        font_size=fontsize, font_name=fontname, alignment=0.5)
    y_title = text(0.02, 0.5, ylabel, $
        font_size=fontsize, font_name=fontname, alignment=0.5, orientation=90)

    if keyword_set(sav) then begin
        b = ''
        read, b, prompt="Save figure (y/n)? "
        if b eq "y" then begin
            fname = ''
            read, fname, prompt="Enter file name to save: "
            p.save, "Figures/" + fname, resolution=300
        endif
    endif

STOP

end
