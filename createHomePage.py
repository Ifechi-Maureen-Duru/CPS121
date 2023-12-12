import requests
from findTemperatureLive import findTemperatureLive
from sentence import sentence

def findTemperature(zip_code):
    try:
        weather = requests.get(f"https://www.localconditions.com/weather-{zip_code}/").text
        
        curLoc = weather.find("current_temp")
        if curLoc != -1:
            degLoc = weather.find("&deg;", curLoc)
            # The temperature number is preceded by a pipe
            tempLoc = weather.rfind("|", 0, degLoc)
            # Temperature value is everything between the pipe (and space) and the degree symbol
            temperature = weather[tempLoc + 2:degLoc].strip()
            return f"Current temperature in {zip_code} is {temperature}°F"
        else:
            return "Unable to fetch temperature"
    except requests.RequestException as e:
        return f"Error fetching temperature: {e}"

def createHomePage(emailuser, zip_code):
    username = emailuser
    firstname, lastname = emailuser.split(".")

    wenham_temperature = findTemperatureLive()
    other_location_temperature = findTemperature(zip_code)
    
    random_sentence = sentence()

    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{firstname.capitalize()}'s Home Page</title>
    </head>
    <body>
        <h1>Welcome to {firstname.capitalize()}'s Home Page</h1>
        <p>
            Hi! My name is {firstname.capitalize()}. This is my home page!
        </p>
        <hr>
        <p>
            Here is my picture.
        </p>
        <img src="{username}.jpg" alt="Picture of {firstname.capitalize()}"
             width="300"
             height="400" />
        <p>
            Current temperature in Wenham: {wenham_temperature}
        </p>
        <p>
            Temperature in {zip_code}: {other_location_temperature}
        </p>
        <p>
            Random Sentence: {random_sentence}
        </p>
    </body>
    </html>
    '''

    with open(f"{emailuser}.html", "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    email_user = "Maureen.Duru"
    input_zip_code = input("Enter a different zip code: ")
    createHomePage(email_user, input_zip_code)
