
lattitude = #North Positive South Negative
longitude = #west in negative east positive
elevation = #elevation correction factor
julianDate = 

daysSince2000 = julianDate - 2451545 + 68.184 / 86400  # number of days since Jan 1st, 2000 at midnight accounting for leap seconds (DUT1 for UTC)
meanSolarTime = daysSince2000 - longitude/360 #Time of mean solar noon in terms of fractional days since Jan 1st, 2000 at midnight
meanSolarAnomaly = (357.5291+0.98560028*meanSolarTime)%360 #solar mean anomoly
elipLongitude = (meanSolarAnomaly+centre+180+102.9372)%360 #eliptic/celestural longitude 
solarDec = asin(sin(elipLongitude)*sin(23.44)) #Declination of the sun, 23.44 deg is the earth's maximum axial tilt 
hourAngle = acos(sin(-2.076*sqrt(elevation)/60)-sin(lattitude)*sin(solarDec))/(cos(lattitude)*cos(solarDec))
solarTransit = 2451545 + meanSolarTime + 0.0053*sin(meanSolarAnomaly) - 0.0069*sin(2*elipLongitude)

sunRise = solarTransit - hourAngle/360
sunSet = solarTransit + hourAngle/360