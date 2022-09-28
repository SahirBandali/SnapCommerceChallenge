import pandas as pd
import re


def CleanAirlineCode(airlineCode):
    airlineList = airlineCode.split()

    for index, airlineVal in enumerate(airlineList):
        airlineList[index] = re.sub("[^A-Za-z]", "", airlineVal)

    return " ".join(airlineList)


data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

def CleanAirlineData(data):

    rows = data.split("\n")
    columns = rows[0].split(";")

    rows.pop()
    rows.pop(0)

    columns.pop()
    columns += ["To", "From"]

    df = pd.DataFrame(columns=columns)

    for index, row in enumerate(rows):
        contents = row.split(";")
        airlineCode, delayTime, flightCode, toFrom = contents

        if (index == 0):
            trackFlightCode = int(float(flightCode))

        flightCode = trackFlightCode
        trackFlightCode += 10

        toCountry = toFrom.split("_")[0].upper()
        fromCountry = toFrom.split("_")[1].upper()

        airlineCode = CleanAirlineCode(airlineCode)

        df.loc[index] = [airlineCode, delayTime,
                        flightCode, toCountry, fromCountry]
    
    return df


print(CleanAirlineData(data))
