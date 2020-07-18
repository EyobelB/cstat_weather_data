# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Eyobel Berhane
# Section:      520
# Assignment:   Lab 7b
# Date:         28 10 2019

import csv
from statistics import stdev

#Open the file with reading permissions
with open("WeatherDataWindows.csv",'r') as weatherFile:

    #Set up an array to search with
    tempMaxStrings = []
    tempMaxArray = []
    tempMinStrings = []
    tempMinArray = []
    precipitationStrings = []
    precipitation = []
    humidityAvgStrings = []
    humidityAvg = []

    highTempMayAVG = []
    mayTempFloat = []

    dayCount = float(1095)

    #Set up a file reader
    fileRow = csv.reader(weatherFile)

    #Read each row, gathering whatever data is needed
    for row in fileRow:
        tempMaxStrings.append(row[1])
        tempMinStrings.append(row[3])
        precipitationStrings.append(row[13])
        humidityAvgStrings.append(row[8])
        checkString = row[0]
        #Check the average high within May 2015
        if checkString[0] == "5" and checkString[4:8] == "2015":
            highTempMayAVG.append(row[1])

    #Cut out the headers from the data sets
    tempMaxStrings = tempMaxStrings[1:len(tempMaxStrings)]
    tempMinStrings = tempMinStrings[1:len(tempMinStrings)]
    precipitationStrings = precipitationStrings[1:len(precipitationStrings)]
    humidityAvgStrings = humidityAvgStrings[1:len(humidityAvgStrings)]

    #Run this loop to convert the string arrays into usable number values
    for num in range(0, len(tempMaxStrings)):
        tempMaxArray.append(int(tempMaxStrings[num]))
        tempMinArray.append(int(tempMinStrings[num]))
        precipitation.append(float(precipitationStrings[num]))
        humidityAvg.append(int(humidityAvgStrings[num]))
    for each in highTempMayAVG:
        mayTempFloat.append(float(each))

    #Sort particular arrays
    tempMaxArray.sort()
    tempMinArray.sort()

    #Calculate needed statistics based on sorted data
    tempMax = tempMaxArray[len(tempMaxArray) - 1]
    tempMin = tempMinArray[0]
    precipitationAverage = round(sum(precipitation) / len(precipitation),6)
    precipitationSTD = round(stdev(precipitation),6)
    daysPast70Humid = float(0)
    mayTempAVG = round((sum(mayTempFloat) / float(31)),2)

    for humidity in humidityAvg:
        if humidity >= 70:
            daysPast70Humid += float(1)
        else:
            continue
    percentPast70 = round(((daysPast70Humid / dayCount) * 100),3)

    #Print the needed statistics
    print("Across the 3 years, the highest temperature was " + str(tempMax) + "F")
    print("The lowest temperature was " + str(tempMin) + "F")
    print("The month of May 2015 had an average high temperature of " + str(mayTempAVG) + "F")
    print("The average precipitation was " + str(precipitationAverage) + "in")
    print("The standard deviation of precipitation was " + str(precipitationSTD) + "in")
    print(str(percentPast70) + "%", "of days had an average humidity of 70% or higher")

