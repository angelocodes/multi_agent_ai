from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

@CrewBase
class MultiAgentAi():
    """MultiAgentAi crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],  # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool(
                search_url="https://google.serper.dev/news",
                n_results=2,
            )]
        )

    @agent
    def scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['scraper'],  # type: ignore[index]
            verbose=True,
            tools=[ScrapeWebsiteTool()]
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],  # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],  # type: ignore[index]
        )

    @task
    def scraping_task(self) -> Task:
        return Task(
            config=self.tasks_config['scraping_task'],  # type: ignore[index]
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],  # type: ignore[index]
        )

    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'],  # type: ignore[index]
            output_file='final_post.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MultiAgentAi crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
