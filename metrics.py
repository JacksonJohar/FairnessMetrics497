import numpy as np
import statistics as stat

Rnums = []
Dwasted = []
Rwasted = []
Dfair = []
Rfair = []
totD = 0
totR = 0
totDWasted = 0
totRWasted = 0
totDWon = 0
totRWon = 0
totDFair = 0
totRFair = 0
shift = 0
bound = .05
k = -.2

#Generage random normal distributed numbers (mean, std dev, size)
Dnums = np.random.normal(.5, .05, size=(50))

for d in Dnums:
    totD = totD + d

    r = 1 - d
    Rnums.append(r)
    totR = totR + r

    if d > .5:
        waste = d - .5
        Dwasted.append(waste)
    else:
        waste = d
        Dwasted.append(waste)

    totDWasted = totDWasted + waste

    if r > .5:
        waste = r - .5
        Rwasted.append(waste)
    else:
        waste = r
        Rwasted.append(waste)

    totRWasted = totRWasted + waste

shift = (totD - totR)/100

for d in Dnums:
    fair = d - shift
    Dfair.append(fair)
    totDFair = totDFair + fair
    if fair > .5:
        totDWon = totDWon + 1


for r in Rnums:
    fair = r + shift
    Rfair.append(fair)
    totRFair = totRFair + fair
    if fair > .5:
        totRWon = totRWon + 1

#Metric Calculation

#Efficiency Gap
dEfficiencyGap = (totRWasted - totDWasted)/50 
rEfficiencyGap = (totDWasted - totRWasted)/50
print("D Efficiency Gap: " + str(round(dEfficiencyGap, 4)))
print("R Efficiency Gap: " + str(round(rEfficiencyGap, 4)))
print("")

#Mean Median Difference
dAverage = stat.mean(Dnums)
rAverage = stat.mean(Rnums)
dMedian = stat.median(Dnums)
rMedian = stat.median(Rnums)
dMeanMed = dMedian - dAverage
rMeanMed = rMedian - rAverage
print("D Mean-Med diff: " + str(round(dMeanMed, 4)))
print("R Mean-Med diff: " + str(round(rMeanMed, 4)))
print("")

#Partisan Bias
dPartisanBias = (totDWon - totDFair)/50
rPartisanBias = (totRWon - totRFair)/50
print("D Partisan Bias: " + str(round(dPartisanBias, 4)))
print("R Partisan Bias: " + str(round(rPartisanBias, 4)))
print("")


#Normalized Metrics

#Normalized Efficiency Gap
normDGap = dEfficiencyGap/bound
normRGap = rEfficiencyGap/bound
print("Normalized D Efficiency Gap: " + str(round(normDGap, 4)))
print("Normalized R Efficiency Gap: " + str(round(normRGap, 4)))
print("")

#Normalized Mean Median Difference
normDMeanMed = dMeanMed/bound
normRMeanMed = rMeanMed/bound
print("Normalized D Mean-Med diff: " + str(round(normDMeanMed, 4)))
print("Normalized R Mean-med diff: " + str(round(normRMeanMed, 4)))
print("")

#Normalized Partisan Bias
normDPartisanBias = dPartisanBias/bound
normRPartisanBias = rPartisanBias/bound
print("Normalized D Partisan Bias: " + str(round(normDPartisanBias, 4)))
print("Normalized R Partisan Bias: " + str(round(normRPartisanBias, 4)))
print("")


#Calculate Final Combined Metric
dCombined = np.exp(k * ( (pow(normDGap, 2)) + (pow(normDMeanMed, 2)) + (pow(normDPartisanBias, 2))))
rCombined = np.exp(k * ( (pow(normRGap, 2)) + (pow(normRMeanMed, 2)) + (pow(normRPartisanBias, 2))))
print ("D Combined: " + str(dCombined))
print ("R Combined: " + str(rCombined))