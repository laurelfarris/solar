#
# Use timelag.pro to get highest correlation values(cc) within a specified radius for
# randomly generated pixel values, along with the corresponding timelag and
# distance from pixel in quesion (in pixels for now).
# Save values in a separate file for each pixel (but try to figure
#  out how to do this in one file).
# 
# Last modified: 12/02/15


t = (SIZE(cube))[3]
tau = INDGEN(t)-(t/2)
pixels = 2001

# assign a 'radius' in pixels
radius = 50

# Number of pixels to run through
num_pairs = 8

# Generate random numbers to choose as pixels
for k = 0, num_pairs-1 do begin
  
  x = radius + fix((pixels-2*radius)*randomu(seed,1))
  y = radius + fix((pixels-2*radius)*randomu(seed,1))
  x = x[0]
  y = y[0]
  
  #open files for writing
  if k lt 10 then file='corrValues0'+strtrim(string(k),1)+'.dat' $
  else file='corrValues'+strtrim(string(k),2)+'.dat'
  openw, mylun, /get_lun, file

  #printf, mylun, ''
  #printf, mylun, 'Pixel coordinates: ' + string(x) + string(y)
  #printf, mylun, '-----------------------------------------------'

  #cycle through entire square (for one pixel)
  for i = x-radius, x+radius do begin
    for j = y-radius,y+radius do begin
      # Run timelag for [x,y] and [i,j]
      timelag, cube[x,y,*], cube[i,j,*], tau, maxcor
      # only use cc values higher than 0.5
      if maxcor[1] gt 0.5 then begin
        distance=sqrt( (i-x)^2 + (j-y)^2 )
        printf, mylun, x, y, distance, maxcor[1], maxcor[0]
      endif
    endfor
  endfor

free_lun, mylun
endfor

end
