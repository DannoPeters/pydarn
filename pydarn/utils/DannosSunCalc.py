
lattitude = #North Positive South Negative
elevation = #elevation correction factor
meanSolarTime = 
meanSolarAnomaly = (357.5291+0.98560028*meanSolarTime)%360 #solar mean anomoly
elipLongitude = (meanSolarAnomaly+centre+180+102.9372)%360
solarDec = asin(sin(elipLongitude)*sin(23.44)) #Declination of the sun, 23.44 deg is the earth's maximum axial tilt 
hourAngle = (sin(-2.076*sqrt(elevation)/60)-sin(lattitude)*sin(solarDec))/(cos(lattitude)*cos(solarDec))