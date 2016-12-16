

;; Data units
x = 800
y = 1800
r = 1000

;; Window units
i = 500

x_coos = indgen(r) + x
y_coos = indgen(r) + y
d = data[x:x+r-1, y:y+r-1, 0]^0.5

im = image( $
    d, $
    x_coos, $
    y_coos, $
    layout=[1,1,1], $
    margin=0, $
    location=[1000,1000], $
    ;dimensions=[i, i] $
    ;image_dimensions=[i,i] $
    axis_style = 2 $
    )


end
