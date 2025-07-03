from agent import graph
from dotenv import load_dotenv
import json
from langsmith import traceable
from pprint import pprint

load_dotenv()

sample_data = {
    "today": {
        "revenue": 1500,
        "cost": 1000,
        "customers": 50
    },
    "yesterday": {
        "revenue": 1000,
        "cost": 700,
        "customers": 50
    }
}

@traceable
def run_graph():
    return graph.invoke(sample_data)

output = run_graph()

with open("output.json", "w") as f:
    json.dump(output, f, indent=2)

print(json.dumps(output, indent=4))