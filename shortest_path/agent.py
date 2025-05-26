from google.adk.agents import LlmAgent 



shortest_path_agent=LlmAgent(

    model="gemini-2.0-flash",
    name="shortest_path_agent",
    description="An agent that can give the shortest path",
    instruction="From the given distance list from each city to the other, find a path that goes through all the cities while covering the least distance. Try to approximate and find the answer as quickly as possible",
    tools=[]

)


distance_calculator_agent=LlmAgent(
    model="gemini-2.0-flash",
    name="distance_calculator_agent",
    description="An agent that can provide the distance between all the cities given in a json adjacency matrix format",
    instruction="From the list of cities given create an adjacency matrix as json  that provides the distance in KM from each city to the other.From the given distance list from each city to the other, find a path that goes through all the cities while covering the least distance. Try to approximate and find the answer as quickly as possible",
    tools=[]
)


root_agent=LlmAgent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="Given a list of cities the agent can find the shortest route between all the cities",
    sub_agents=[distance_calculator_agent,shortest_path_agent]
)








