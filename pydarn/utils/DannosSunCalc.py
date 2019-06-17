import numpy as np
import math

lattitude = 52.1332 #North Positive, South Negative
longitude = -106.6700 #west in negative, east positive
elevation = 482 #elevation correction factor (meters)

day = 17
month = 6
year = 2019

decMonth = math.floor(275 * month / 9)
decYear = math.floor((month + 9) / 12)
decMultiYear = (1 + math.floor((year - 4 * math.floor(year / 4) + 2) / 3))
julianDate = decMonth - (decYear * decMultiYear) + day - 30

daysSince2000 = julianDate - 2451545 + 68.184 / 86400  # number of days math.since Jan 1st, 2000 at midnight accounting for leap seconds (DUT1 for UTC)
meanSolarTime = daysSince2000 - longitude/360 #Time of mean solar noon in terms of fractional days math.since Jan 1st, 2000 at midnight
meanSolarAnomaly = (357.5291+0.98560028*meanSolarTime)%360 #solar mean anomoly
centre = 1.9148*math.sin(meanSolarAnomaly)+0.0200*math.sin(2*meanSolarAnomaly)+0.003*math.sin(3*meanSolarAnomaly); #Equation of the centre, 1.9148 is coeficent for centre of the earth
elipLongitude = (meanSolarAnomaly+centre+180+102.9372)%360 #eliptic/celestural longitude 
solarDec = math.sin(math.sin(elipLongitude)*math.sin(23.44)) #Declination of the sun, 23.44 deg is the earth's maximum axial tilt 
hourAngle = math.acos(math.sin(-2.076*math.sqrt(elevation)/60)-math.sin(lattitude)*math.sin(solarDec))/(math.cos(lattitude)*math.cos(solarDec))
solarTransit = 2451545 + meanSolarTime + 0.0053*math.sin(meanSolarAnomaly) - 0.0069*math.sin(2*elipLongitude)

sunRise = solarTransit - hourAngle/360
sunSet = solarTransit + hourAngle/360

riseTime_H = math.trunc((sunRise - julianDate)*24)
riseTime_m = math.trunc((((sunRise - julianDate)*24)-riseTime_H)*60)
riseTime_s = math.trunc((((((sunRise - julianDate)*24)-riseTime_H)*60)-riseTime_m)*60)

setTime_H = math.trunc((sunSet - julianDate+0.5)*24)
setTime_m = math.trunc((((sunSet - julianDate+0.5)*24)-setTime_H)*60)
setTime_s = math.trunc((((((sunSet - julianDate+0.5)*24)-setTime_H)*60)-setTime_m)*60)



print("Julian Date: {Jdate}  \nSunrise: {sunRise}     Time: {rHH}:{rmm}:{rss} \nSunset: {sunSet}     Time: {sHH}:{smm}:{sss}".format(Jdate=julianDate, sunRise=sunRise, sunSet=sunSet, rHH=riseTime_H, rmm=riseTime_m, rss=riseTime_s, sHH=setTime_H, smm=setTime_m, sss=setTime_s))