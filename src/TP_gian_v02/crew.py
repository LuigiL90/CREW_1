from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from tools.custom_tool import *
from crewai import Agent, Crew, Process, Task, LLM

import os
from dotenv import load_dotenv
load_dotenv()

llm = LLM(

   model="gpt-4o-mini",

   temperature=0.2,

)

@CrewBase
class SurpriseTravelCrew():
    """Surprise Travel Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def personalized_activity_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['personalized_activity_planner'],
            tools=[SerperDevTool(), ScrapeWebsiteTool() ],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )
    
    @agent
    def restaurant_scout(self) -> Agent:
        return Agent(
            config=self.agents_config['restaurant_scout'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )
    
    @agent
    def weather_forecast(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_forecast'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose = True,
            allow_delegation=True,
            llm=llm,
        )
    
    @agent
    def itinerary_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_compiler'],
            tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )
    
    @task
    def personalized_activity_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['personalized_activity_planning_task'],
            agent=self.personalized_activity_planner(),
        )
    
    @task
    def restaurant_scouting_task(self) -> Task:
        return Task(
            config=self.tasks_config['restaurant_scouting_task'],
            agent=self.restaurant_scout(),
        )
    
    @task
    def weather_forecast_task(self) -> Task:
        return Task(
            config=self.tasks_config['weather_forecast_task'],
            agent=self.weather_forecast(),
        )

    @task
    def itinerary_compilation_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_compilation_task'],
            agent=self.itinerary_compiler(),
            human_input=True,
            output_json=Itinerary,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates a SurpriseTravel Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            json_dict = True,
        )