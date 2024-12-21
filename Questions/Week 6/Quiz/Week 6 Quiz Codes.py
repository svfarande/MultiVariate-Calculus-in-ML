# 1. Linear regression

# Q.3 ---------------------------------
# See what m and c do to the fit
m = 1.2 ; c = 0.1
p = [m,c]
line(p)

# Replace m and c with values that minimise χ^2.
p = [m, c]

# Q.5 ---------------------------------
# Here the function is defined
def linfit(xdat,ydat):
  # Here xbar and ybar are calculated
  xbar = np.sum(xdat)/len(xdat)
  ybar = np.sum(ydat)/len(ydat)

  # Insert calculation of m and c here. If nothing is here the data will be plotted with no linear fit

  # Return your values as [m, c]
  return [m, c]

# Produce the plot - don't put this in the next code block
line()

# Here the function is defined
def linfit(xdat,ydat):
  # Here xbar and ybar are calculated
  xbar = np.sum(xdat)/len(xdat)
  ybar = np.sum(ydat)/len(ydat)

  # Insert calculation of m and c below

  # Return your values as [m, c]
  return [m, c]
  
# Don't include line() in this answer box

# Q.6 ---------------------------------

from scipy import stats

# Use the stats.linregress() method to evaluate regression
regression = 

line(regression)

from scipy import stats

# Use the stats.linregress() method to evaluate regression
regression = 

# Don't use line(regression) in this code box
