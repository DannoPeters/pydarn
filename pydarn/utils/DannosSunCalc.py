import numpy as np
import math


def meanSolarAnomaly(time):
	return (0.9856 * time) - 3.289


def trueLongitude(time):
	meanAnom = meanSolarAnomaly(time)
	trueLon = meanAnom + (1.916 * math.degrees(math.sin(math.radians(meanAnom))) + math.degrees((0.020 * math.sin(2 * math.radians(meanAnom))))) + 282.634
	while (trueLon > 360 or trueLon < 0):
		if trueLon > 360:
			trueLon -= 306
		if trueLon < 0:
			trueLon += 360
	return trueLon


def rightAscension(time):
	trueLon = trueLongitude(time)
	rightAsc = math.degrees(math.atan(0.91764 * math.tan(math.radians(trueLon))))

	while (rightAsc > 360 or rightAsc < 0):
		if rightAsc > 360:
			rightAsc -= 306
		if rightAsc < 0:
			rightAsc += 360

	#correct quadrant
	trueLonQuad  = (math.floor( trueLon/90)) * 90
	rightAscQuad = (math.floor(rightAsc/90)) * 90
	rightAsc = rightAsc + (trueLonQuad - rightAscQuad)

	return rightAsc/15 #convert to hours


def solarHour(time, zenith, lattitude):
	trueLon = trueLongitude(time)
	sinDec = 0.39782 * math.sin(math.radians(trueLon))
	cosDec = math.cos(math.asin(sinDec))
	cosH = (math.cos(math.radians(zenith)) - (sinDec * math.sin(math.radians(lattitude)))) / (cosDec * math.cos(math.radians(lattitude)))
	return math.degrees(math.acos(cosH))


def localMeanTime(time, solarHr):
	solarHr = solarHour(time, zenith, lattitude)
	rightAsc = rightAscension(time)
	meanTime = solarHr + rightAsc - (0.06571 * time) - 6.622
	return meanTime


def UTC_MeanTime(time, lonHour):
	UTC = time - lonHour

	while (UTC > 24 or UTC < 0):
		if UTC > 24:
			UTC -= 24
		if UTC < 0:
			UTC += 24

	return UTC


def localTimezone(UTCtime, localOff):
	localTime = UTCtime + localOff
	return localTime


def JulianDate(day, month, year):
	decMonth = math.floor(275 * month / 9)
	decYear = math.floor((month + 9) / 12)
	decMultiYear = (1 + math.floor((year - 4 * math.floor(year / 4) + 2) / 3))
	return (decMonth - (decYear * decMultiYear) + day - 30)


def JulianDate2(day, month, year):
	# The value 'march_on' will be 1 for January and February, and 0 for other months.
    march_on = math.floor((14 - month) / 12)
    year = year + 4800 - march_on
    # And 'month' will be 0 for March and 11 for February. 0 - 11 months
    month = month + 12 * march_on - 3

    y_quarter = math.floor(year / 4)
    jdn = day + math.floor((month * 153 + 2) / 5) + 365 * year + y_quarter

    julian = year < 1582 or year == (1582 and month < 10) or (month == 10 and day < 15)
    if julian:
        reform = 32083 # might need adjusting so needs a test
    else:
        reform = math.floor(year / 100) + math.floor(year / 400) + 32030.1875 # fudged this

    return jdn - reform


lattitude = 52.1332 #North Positive, South Negative
longitude = -106.6700 #west in negative, east positive
elevation = 482 #elevation correction factor (meters)

zenith = 90.8333

day = 17
month = 6
year = 2019
julianDate = JulianDate(day, month, year)

"""
daysSince2000 = julianDate - 2451545 + 68.184 / 86400  # number of days math.since Jan 1st, 2000 at midnight accounting for leap seconds (DUT1 for UTC)
meanSolarNoon = daysSince2000 - longitude/360 #Time of mean solar noon in terms of fractional days math.since Jan 1st, 2000 at midnight
meanSolarAnomaly = (357.5291+0.98560028*meanSolarNoon)%360 #solar mean anomoly
centre = 1.9148*math.sin(math.radians(meanSolarAnomaly))+0.0200*math.sin(2*math.radians(meanSolarAnomaly))+0.003*math.sin(3*math.radians(meanSolarAnomaly)); #Equation of the centre, 1.9148 is coeficent for centre of the earth
elipLongitude = (meanSolarAnomaly+math.degrees(centre)+180+102.9372)%360 #eliptic/celestural longitude 
solarDec = math.degrees(math.asin(math.sin(math.radians(elipLongitude))*math.sin(math.radians(23.44)))) #Declination of the sun, 23.44 deg is the earth's maximum axial tilt 
hourAngle = math.degrees(math.acos((math.sin(math.radians(-2.076*math.sqrt(elevation)/60))-math.sin(math.radians(lattitude))*math.sin(math.radians(solarDec)))/(math.cos(math.radians(lattitude))*math.cos(math.radians(solarDec)))))
solarTransit = 2451545 + meanSolarNoon + 0.0053*math.sin(math.radians(meanSolarAnomaly)) - 0.0069*math.sin(math.radians(2*elipLongitude))

sunRise = solarTransit - hourAngle/360
sunSet = solarTransit + hourAngle/360

riseTime_H = math.trunc((sunRise - julianDate)*24)
riseTime_m = math.trunc((((sunRise - julianDate)*24)-riseTime_H)*60)
riseTime_s = math.trunc((((((sunRise - julianDate)*24)-riseTime_H)*60)-riseTime_m)*60)

setTime_H = math.trunc((sunSet - julianDate+0.5)*24)
setTime_m = math.trunc((((sunSet - julianDate+0.5)*24)-setTime_H)*60)
setTime_s = math.trunc((((((sunSet - julianDate+0.5)*24)-setTime_H)*60)-setTime_m)*60)
"""


#Method 2

lonHour = longitude/15
tRise = julianDate + ((6 - lonHour) / 24)
tSet = julianDate + ((18 - lonHour) / 24)

Rise_SolarHour = (360 - solarHour(tRise, zenith, lattitude))/15
Set_SolarHour = solarHour(tSet, zenith, lattitude)/15

localMeanRise = localMeanTime(tRise, Rise_SolarHour)
localMeanSet = localMeanTime(tSet, Set_SolarHour)
UTC_Rise = UTC_MeanTime(localMeanRise, lonHour)
UTC_Set = UTC_MeanTime(localMeanSet, lonHour)
Local_Rise = localTimezone(UTC_Rise, -6)
Local_Set = localTimezone(UTC_Set, -6)

riseTime_H = math.trunc(Local_Rise)
riseTime_m = math.trunc((Local_Rise-riseTime_H)*60)
riseTime_s = math.trunc((((Local_Rise-riseTime_H)*60)-riseTime_m)*60)

setTime_H = math.trunc(Local_Set)
setTime_m = math.trunc((Local_Set-setTime_H)*60)
setTime_s = math.trunc((((Local_Set-setTime_H)*60)-setTime_m)*60)


print("Julian Date: {Jdate}  \nSunrise: {sunRise}     Time: {rHH}:{rmm}:{rss} \nSunset: {sunSet}     Time: {sHH}:{smm}:{sss}".format(Jdate=julianDate, sunRise=localMeanRise, sunSet=localMeanSet, rHH=riseTime_H, rmm=riseTime_m, rss=riseTime_s, sHH=setTime_H, smm=setTime_m, sss=setTime_s))