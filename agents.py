from crewai import Agent, Task, Crew, Process,LLM
from crewai_tools import WebsiteSearchTool, SerperDevTool
import os
import logging
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ResearchAgent:

    def __init__(self):
        try:
            self.llm = LLM(
                model="openai/gpt-4o",
                temperature=0,
                api_key=os.getenv("OPENAI_API_KEY"), # Use environment variable
            )
            logging.info("LLM initialized successfully.")
        except Exception as e:
            logging.error(f"Error initializing LLM: {e}")
            raise

    def create_research_agent(self) -> Agent:
        try:
            return Agent(
                name="ResearchAgent",
                role="Senior Research Analyst",
                goal = "Conduct in-depth research on assigned topics using web search tools.",
                backstory= "An expert researcher skilled in gathering and synthesizing information from various online sources.",
                llm=self.llm,
                verbose=True,
                tools=[
                    WebsiteSearchTool(
                        name="Website Search",
                        description="Useful for searching specific websites for information.",
                        llm=self.llm,
                    )
                    # SerperDevTool(
                    #     name="Serper Dev",
                    #     description="Useful for performing general web searches to gather information.",
                    #     llm=self.llm, # Pass the GoogleGenerativeAI instance
                    #     api_key=os.getenv("SERPER_API_KEY"), # Ensure correct environment variable name for SerperDevTool
                    # ),
                ])
        except Exception as e:
            logger.error(f"Error creating ResearchAgent: {e}")
            raise

    def create_analysis_agent(self) -> Agent:
        try:
            return Agent(
                
                name="AnalysisAgent",
                role="Expert Data Analyst",
                goal = "Analyze and synthesize information gathered by ResearchAgent.",
                backstory= "An expert analyst skilled in interpreting data and drawing conclusions.",
                llm=self.llm,
                verbose=True,
            )
        except Exception as e:
            logger.error(f"Error creating AnalysisAgent: {e}")
            raise

    def create_summerizer_agent(self) -> Agent:
        try:
            return Agent(
                name="SummarizerAgent",
                role="Concise Report Writer",
                goal = "Summarize the findings from the research and analysis.",
                backstory= "An expert summarizer skilled in condensing information into clear and concise formats.",
                llm=self.llm,
                verbose=True,
            )
        except Exception as e:
            logger.error(f"Error creating SummarizerAgent: {e}")
            raise

    def create_research_task(self, agent: Agent, topic: str) -> Task:
        try:
            return Task(
                name="ResearchTask",
                description=f"Conduct research on the topic: {topic}",
                expected_output="To fetch relevant source of information",
                agent=agent,
            )
        except Exception as e:
            logger.error(f"Error creating ResearchTask: {e}")
            raise

    def create_analysis_task(self, agent: Agent, research_data: str) -> Task:
        try:
            return Task(
                name="AnalysisTask",
                description=f"Analyze the following research data: {research_data}",
                expected_output="A detailed analysis on given topic",
                agent=agent,
            )
        except Exception as e:
            logger.error(f"Error creating AnalysisTask: {e}")
            raise

    def create_summarization_task(self, agent: Agent, analysis_data: str) -> Task:
        try:
            return Task(
                name="SummarizationTask",
                description=f"Summarize the following analysis data: {analysis_data}",
                expected_output="A extractive summary of given input",
                agent=agent,
            )
        except Exception as e:
            logger.error(f"Error creating SummarizationTask: {e}")
            raise

    def run(self, topic: str) -> Optional[str]:
        try:
            research_agent = self.create_research_agent()
            analysis_agent = self.create_analysis_agent()
            summarizer_agent = self.create_summerizer_agent()

            research_task = self.create_research_task(research_agent, topic)
            analysis_task = self.create_analysis_task(analysis_agent, topic)
            summarization_task = self.create_summarization_task(summarizer_agent, topic)

            crew = Crew(
                name="ResearchCrew",
                agents=[research_agent, analysis_agent, summarizer_agent],
                tasks=[research_task, analysis_task, summarization_task],
                process = Process.sequential,
                verbose=True,

            )

            result = crew.kickoff()

            return str(result)


        except Exception as e:
            logger.error(f"Error running research process: {e}")
            return None