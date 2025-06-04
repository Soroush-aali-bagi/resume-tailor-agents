import os
import asyncio
from openai import OpenAI
from dotenv import load_dotenv
from resume_agents.resume_agents import create_resume_generator, create_resume_evaluator
from utils.file_utils import read_context, save_resume
from agents import Runner

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Read context files
resume_gen_instructions = read_context("./../context/resume_gen_instructions.txt")
judge_instruction = read_context("./../context/judge_instruction.txt")
original_resume = read_context("./../context/previous_resume.txt")
job_description = read_context("./../context/job_description.txt")

# Create agents
resume_generator = create_resume_generator(resume_gen_instructions)
resume_evaluator = create_resume_evaluator(judge_instruction)

async def main():
    # Initialize variables
    max_iterations = 6
    current_iteration = 1
    print("Starting resume improvement loop...")

    resume_gen_prompt = f"""
    Refine my resume for this job description.
    ----
    ## Here's my current resume:
    {original_resume}
    ----
    ## Here's the job description:
    {job_description}
    """

    while current_iteration < max_iterations:
        print(f"\nIteration {current_iteration}/{max_iterations}")

        # Generate new resume
        result = await Runner.run(
            resume_generator,
            resume_gen_prompt
        )
        new_resume = result.final_output

        print("Saving resume ", current_iteration, " ...")
        save_resume(new_resume, f"./../resumes/new_resume-{current_iteration}.md")

        print("Evaluating resume...")

        # Evaluate the new resume
        judge_prompt = f"""
        ## Here's my original resume:
        {original_resume}
        ----
        ## Here's the new generated resume:
        {new_resume}
        ----
        ## Here's the job description:
        {job_description}
        """
        result = await Runner.run(
            resume_evaluator,
            judge_prompt
        )
        evaluation = result.final_output

        print("Saving feedback ...")
        save_resume(evaluation.rewrite_instruction, f"./../resumes/feedback-{current_iteration}.txt")

        print("\nEvaluation Results:")
        print(f"Resume Passed: {evaluation.resume_passed}")
        print(f"Feedback: {evaluation.rewrite_instruction}")

        if evaluation.resume_passed:
            break
        else:
            resume_gen_prompt = f"""
            Here is some feedback about the resume you previously generated:
            {evaluation.rewrite_instruction}
            ----
            Generate a new resume.
            ----
            Here's my original resume:
            {original_resume}
            ----
            Here's the job description:
            {job_description}
            ----
            Here's the resume you previously generated:
            {new_resume}
            """

        current_iteration += 1

    if current_iteration == max_iterations:
        print("\nResume improvement process terminated because it reached max iterations!")
    else:
        print("\nResume improvement process completed successfully!")
    print(f"Final resume saved as: resumes/generated_resume_{current_iteration}.md")

if __name__ == "__main__":
    asyncio.run(main()) 