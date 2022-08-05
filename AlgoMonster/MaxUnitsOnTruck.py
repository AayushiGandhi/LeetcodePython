#https://www.youtube.com/watch?v=qZUokf5dwYw&ab_channel=SehoLim
#https://leetcode.com/problems/maximum-units-on-a-truck/

def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda box: box[1], reverse=True)

    total_units = 0
    for noOfBoxes, units in boxTypes:
        if truckSize < noOfBoxes:
            total_units += truckSize * units
            break

        total_units += noOfBoxes * units
        truckSize -= noOfBoxes

    return total_units