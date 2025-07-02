'''
Section 4: Implement using BDI (Believe, Desire, Intention) 
Agent purpose: 
Create an agent that takes user preference based on weather like sunny or rainy and tells the user about places to visit. 
Objective: 
Build an agent that: 
Believe: Extracts and stores key facts from user input to form the agent's beliefs 
Desires: Highlights what the user wants and sends it to the ‘intend’ function. 
Intends: Executes tool (suggest places depend on user specified weather)  

Outputs: list of places according to the weather conditions specified. 
'''


def attractions_tool(location): 
    print(f"Fetching Attractions in {location}")
    return  ["Sagrada Familia", "Park Güell"]

def weather_tool(location): 
    print(f"Fetching the Weather of {location}")
    return {"condition": "rainy", "temp": 16}

def time_estimator(activity):
    print(f"Estimating Time of {activity}")
    return {"Sagrada Familia": "2 hours"}


class BDI:
    def __init__(self):
        pass
    
    def believe(self, weather):
        if "rainy" in weather:
            interst = "rainy"
        elif "sunny" in weather:
            interst = "sunny"
        elif "cloudy" in weather:
            interst = "cloudy"

        return self.desire(interst)        

    def desire(self, interest):
        print("After desiring, I believe the interest is:", interest)

        if interest == "rainy":
            print("This shows the user likes cold places, I'll suggest somwhere wehre monsoon hits\n")
        elif interest == "sunny" :
            print("This shows the user likes hot places, I'll suggest somwhere Where there's plenty of sunlight\n")        
        elif interest =="cloudy":
            print("This shows the user likes cool places, I'll suggest somwhere where its naturally hazy\n")

        return self.intention(interest)

    def intention(self, weather):
        if weather == "rainy":
            return "Northern Areas: Naran, Khagan"
        elif weather == "sunny" :
            return "Balochistan"      
        elif weather =="cloudy":
            return "Kohat"


bdi =BDI()

weath = input("What kind of weather do you like? ")

answer = bdi.believe(weath)
print("I suggest you go to:", answer)

