from pydantic import BaseModel
from agents import Agent, ModelSettings

class JudgeOutput(BaseModel):
    resume_passed: bool
    rewrite_instruction: str

def create_resume_generator(instructions: str) -> Agent:
    return Agent(
        name="Resume Generator",
        instructions=instructions,
        model_settings=ModelSettings(temperature=0.6)
    )

def create_resume_evaluator(instructions: str) -> Agent:
    return Agent(
        name="Resume Evaluator",
        instructions=instructions,
        model_settings=ModelSettings(temperature=0.0),
        output_type=JudgeOutput
    ) 