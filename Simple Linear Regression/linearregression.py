x = [1975, 1976, 1977, 1978, 1979, 1980,
 1981,1982, 1983,1984, 1985, 1986, 1987]

y = [2.9642, 2.9644, 2.9656, 2.9667, 2.9673,
2.9688, 2.9696, 2.9698, 2.9713, 2.9717,
2.9725, 2.9742, 2.9757]

xsum = sum(x)
ysum = sum(y)

n=len(x)


x_mean = xsum / n
y_mean = ysum / n

print(x_mean)
print(y_mean)

diff=0

for i in range(0, n):
	diff = diff + (x[i] - x_mean) * (y[i] - y_mean)

xvar = 0;

for i in x:
	xvar = xvar + (i - x_mean) * (i - x_mean)

t1 = diff / xvar

print('%.4f' %t1)

t0 = y_mean - t1 * x_mean

print('%.4f' %t0)

print("The estimated regression equation is %.4fx+ %.4f" % (t1, t0))

def predict(t1, t0, xval):
	yval = t1 * xval + t0
	return yval

y_pred = predict(t1, t0, 1981)
print(y_pred)
