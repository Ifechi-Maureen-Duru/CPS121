import requests

def findTemperatureLive():  
    """Retrieve the current temperature in Wenham using data from localconditions.com."""
    try:
        # Get the weather page
        weather = requests.get("https://www.localconditions.com/weather-boston-massachusetts/01984/").text

        # The temperature can be found near the top of the page after the word "Wenham" and
        # immediately before the HTML code &deg; (the degree symbol)
        curLoc = weather.find("Wenham")
        if curLoc != -1:
            # Now, find the degree symbol ("&deg;") following the temperature
            degLoc = weather.find("&deg;", curLoc)
            # The temperature number is preceded by a pipe
            tempLoc = weather.rfind("|", 0, degLoc)
            # Temperature value is everything between the pipe (and space) and the degree symbol
            temperature = weather[tempLoc + 2:degLoc].strip()
            return f"Current temperature in Wenham is {temperature} degrees"
        else:
            return "Page format has changed; cannot find the temperature"
    except requests.RequestException as e:
        return f"Error fetching temperature: {e}"

if __name__ == "__main__":
    print(findTemperatureLive())


