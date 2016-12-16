


a = randomu(seed, 100)

b = shift(a, -10)
d = shift(a, 10) * 100
e = a * 100
f = a + 100


x = a[10:90]
xs = d[10:90]

x = asin(a)
xs = (asin(a))*2.

x = a
xs = f

tau = indgen(n_elements(x))

timelag, x, xs, tau, c, maxcor
print, maxcor


end
