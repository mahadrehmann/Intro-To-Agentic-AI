'''
Section 3: Implement using the OODA Loop (Observe-Orient-Decide-Act) 
Agent Purpose (Travel Itinerary Planner Agent): 
This AI agent helps users plan a day of travel by: 
Fetching tourist attractions in a given city. 
Checking local weather to adjust recommendations. 
Suggesting indoor/outdoor activities based on weather. 
Estimating time required for each activity. 

Agent Workflow: 
Input: User query (e.g., "Plan a day in Barcelona"). 

Tools: 
attractions_tool(location) → Returns ["Sagrada Familia", "Park Güell"]. 
weather_tool(location) → Returns {"condition": "rainy", "temp": 16}. 
time_estimator(activity) → Returns {"Sagrada Familia": "2 hours"}. 
Output: Structured itinerary with weather-adjusted activities and time estimates. 

Task: 
Build the agent using the OODA framework, where: 
Observe: Parse user input (e.g., "Plan a day in Berlin" → {"location": "berlin", "intent": "itinerary"}). 

Orient: 
Check if the user specified weather constraints (e.g., "if it rains"). 
Prioritize indoor activities for bad weather. 

Decide: Decide which action to take. Like, take out activities according to the weather conditions and estimated time. 

Act: Execute tools and compile results. 
Example Output: 
{ 
 "location": "berlin", 
 "weather": {"condition": "sunny", "temp": 22}, 
 "itinerary": [ 
  {"activity": "Museum Island", "time": "3 hours", "type": "indoor"} 
 ] 
} 
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


class TravelIterneryAgent:
    def __init__(self):
        pass

    def observe(self):
        place = input("Where do you want to plan a day in? ")
        syntax = {"location": place, "intent": "itinerary"}
        return self.orient(syntax)

    def orient(self, place):
        weather = weather_tool(place)

        if weather["condition"] == "rainy":
            activity ="indoor"
        else:
            activity ="anywhere"

        return self.decide(activity, place)


    def decide(self, activity, place):
        time = time_estimator(activity)

        if activity == "outdoor":
            activ = attractions_tool(place)
        else:
            activ = attractions_tool(place)

        return self.act(place,activ, time)


    def act(self, place, activity, time):
        return { 
                "location": place, 
                "weather": {"condition": "sunny", "temp": 22}, 
                "itinerary":[{"activity": activity, "time": time, "type": "indoor"}] 
            } 
    

iter = TravelIterneryAgent()
print(iter.observe())