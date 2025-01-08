from crew import SurpriseTravelCrew
import json
from tools.file_io import save_markdown

def run_crew():
    with open(r"C:\Users\luigi\OneDrive\Desktop\Lavoro\WORK KAD3\Progetto Aloha\QA_module_code\CREW_1\src\TP_gian_v02\data.json", 'r') as file:
        data = file.read()
    inputs = json.loads(data)
    
    result = SurpriseTravelCrew().crew().kickoff(inputs=inputs)
    
        # Save the result as markdown
    markdown_path = save_markdown(result)
    if markdown_path:
        print(f"Markdown file saved successfully: {markdown_path}")
    else:
        print("Failed to save the markdown file.")
    
    print(result)

run_crew()
