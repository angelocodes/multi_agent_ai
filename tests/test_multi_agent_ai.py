from multi_agent_ai.crew import MultiAgentAi

def test_all_agent_initialization():
    crew=MultiAgentAi()
    assert crew.researcher() is not None
    assert crew.scraper() is not None

def test_all_tasks_initializable():
    crew=MultiAgentAi()
    assert crew.research_task() is not None
    assert crew.scraping_task() is not None

def test_scraper_has_tool():
    crew =MultiAgentAi()
    scraper = crew.scraper()
    assert scraper.tools, "Scraper agent should have atleast one tool"
    assert any("ScrapeWebsiteTool" in str(tool.__class__) for tool in scraper.tools)

def test_crew_creation():
    crew_instance = MultiAgentAi()
    crew=crew_instance.crew()
    assert crew is not None
    assert len(crew.tasks)==4, "Crew should have 4 tasks"
    assert len(crew.agents)==4, "Crew should have 4 agents"