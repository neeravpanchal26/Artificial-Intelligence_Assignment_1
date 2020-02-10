# Imports
import numpy as np
from scipy import stats
import matplotlib.pyplot as plot


def import_data(filename, delimit):
    return np.genfromtxt(filename, delimiter=delimit)


myData = import_data('59.csv', ';')

# *****Testing****
# myData = np.zeros(shape=(5, 2))
# myData[0][0] = 1
# myData[0][1] = 4
# myData[1][0] = 3
# myData[1][1] = 6
# myData[2][0] = 5
# myData[2][1] = 10
# myData[3][0] = 5
# myData[3][1] = 12
# myData[4][0] = 6
# myData[4][1] = 13

X = myData[:, 0]

Y = myData[:, 1]

sumX = np.sum(X)

sumY = np.sum(Y)

# 1 Mean of X
meanX = myData.mean(axis=0)[0]

# 2 Mean of Y
meanY = myData.mean(axis=0)[1]

# 3 Standard deviation for X
stdX = myData.std(axis=0)[0]

# 4 Standard deviation for Y
stdY = myData.std(axis=0)[1]

# 5 Correlation Calculation
x = X - meanX

y = Y - meanY

xy = x * y

sumXy = np.sum(xy)

sqrX = np.sum(x ** 2)

sqrY = np.sum(y ** 2)

r = sumXy / np.sqrt(sqrX * sqrY)

# Slope Calculation
b = (r * stdY) / stdX

# Intercept Calculation
A = meanY - (b * meanX)

# *****Testing****
getStats = stats.linregress(X, Y)

# Predicted Y
predictedY = b * X + A

# Error Calculation
error = Y - predictedY

# SSE
SSE = np.sum(error ** 2)


# Testing
def testing(value):
    return b * value + A


# Outputs
output1 = testing(77)
output2 = testing(175)
output3 = testing(475)
output4 = testing(17)
output5 = testing(9)

# Plotting
plot.scatter(myData[:, 0], myData[:, 1], c="blue")
plot.plot(predictedY)
plot.xlabel("Minutes Studying (m)")
plot.ylabel("Percentage (%)")
plot.title("Education Stuff")
plot.show()
