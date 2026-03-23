import pytest
from src.agent import MyAgent

@pytest.fixture
def agent():
    return MyAgent()

def test_capital_of_france(agent):
    assert agent.run("What is the capital of France?") == "Paris"

def test_author_of_1984(agent):
    assert agent.run("Who wrote '1984'?") == "George Orwell"

def test_unknown(agent):
    assert agent.run("What is the speed of light?") == "I don't know."
