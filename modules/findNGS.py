# Find Nearest Gas Station For The Car Position
gasStationsLocations = [5, 11, 15, 21, 25, 31, 35, 41, 45, 51, 55, 61, 65]
carPosition = 66
differences = []

def findNearestStation():

    for i in range(len(gasStationsLocations)):

        difference = gasStationsLocations[i] - carPosition
        differences.append(abs(difference))

    # Find MinDistance and MaxDistance For The Car Position
    minNumIndex = differences.index(min(differences))
    maxNumIndex = differences.index(max(differences))

    print(f"The Nearest Gas Station is in: {gasStationsLocations[minNumIndex]} KM")
    print(f"The Farest Gas Station is in: {gasStationsLocations[maxNumIndex]} KM")


findNearestStation()

