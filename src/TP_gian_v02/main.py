from crew import SurpriseTravelCrew
import json

def run_crew():
    with open(r"C:\Users\morciano\Documents\GitHub\CREW_1\src\TP_gian_v02\data.json", 'r') as file:
        data = file.read()
    inputs = json.loads(data)
    
    result = SurpriseTravelCrew().crew().kickoff(inputs=inputs)
    print(result)

run_crew()