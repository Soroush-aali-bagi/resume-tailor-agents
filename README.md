# AI-Powered Resume Tailoring Agent System

> A modular LLM-based agent system that automatically tailors resumes to job descriptions using a multi-agent evaluation loop — powered by OpenAI's GPT models.



## 🔍 What Is This?

This project implements an intelligent **LLM loop** to automate resume customization for job applications in **computer science and machine learning** fields. It combines two specialized AI agents:

- **Resume Generator Agent**: Tailors the user's original resume to match a new job description, inserting relevant keywords and removing irrelevant content.
- **Resume Judge Agent**: Evaluates the modified resume across six critical hiring criteria and provides rewrite instructions only for the weak areas.

This architecture simulates a real-world feedback loop between a job applicant, a resume writer, and a recruiter.



## 🚀 Key Features

- **LLM-Orchestrated Feedback Loop**: Uses a modular "Judge + Generator" system that mimics iterative human editing.
- **AI Agent Reasoning**: Employs task-specific prompting and chain-of-thought evaluation to enforce strict resume guidelines.
- **LLM Loop Architecture**: Inspired by recent LLM agent frameworks for autonomous refinement workflows.
- **Markdown-Based Resume Editing**: Easy to diff and track changes.
- **No Hallucinations Policy**: Resume generator is constrained not to fabricate experiences, enforced by the Judge agent.
- **Precision Evaluation**: Judge evaluates each criterion independently and only generates rewrite instructions for failed ones.



## Project Structure

```
ai-resume-optimizer/
├── src/                      # Source code directory
│   ├── resume_agents/        # Resume-specific agent implementations
│   │   ├── __init__.py      # Package exports
│   │   └── resume_agents.py # Resume agent implementations
│   ├── utils/               # Utility functions
│   │   ├── __init__.py     # Package exports
│   │   └── file_utils.py   # File handling utilities
│   └── main.py             # Main application entry point
├── context/                 # Input files directory
│   ├── resume_gen_instructions.txt  # Instructions for resume generation
│   ├── judge_instruction.txt        # Instructions for resume evaluation
│   ├── previous_resume.txt          # Your original resume
│   └── job_description.txt          # Target job description
├── resumes/                # Output directory for generated resumes
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- External `agents` package (for core agent functionality)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-resume-optimizer
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Prepare your input files in the `context/` directory:
   - Place your current resume in `context/previous_resume.txt`
   - Add the target job description in `context/job_description.txt`
   - (Optional) Customize the instructions in `resume_gen_instructions.txt` and `judge_instruction.txt`

2. Run the optimizer:
   ```bash
   python src/main.py
   ```

3. Check the results:
   - Generated resumes will be saved in the `resumes/` directory
   - Each iteration creates two files:
     - `new_resume-{iteration}.md`: The generated resume
     - `feedback-{iteration}.txt`: Feedback from the evaluator

## How It Works

1. The system reads your original resume and the job description
2. The Resume Generator agent creates an optimized version
3. The Resume Evaluator agent assesses the new version
4. If the resume doesn't meet requirements:
   - The feedback is used to generate another version
   - The process repeats (up to 6 iterations)
5. The final version is saved when either:
   - The evaluator approves the resume
   - The maximum number of iterations is reached

## Dependencies

- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management
- `pydantic`: Data validation
- `agents`: External package for core agent functionality

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or Open an Issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
