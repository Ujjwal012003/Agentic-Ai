# ⚔️ The Debating Agent Crew

![Repo Status](https://img.shields.io/badge/status-active-green)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
![License](https://img.shields.io/badge/license-MIT-blue)

Welcome to the Debating Agent project, powered by **`crewAI`**. This project demonstrates a multi-agent system where AI agents take on the roles of a debater and a judge to analyze and form a verdict on a complex topic.

---
## How It Works

This crew consists of two specialized agents that collaborate to perform a comprehensive analysis:

* **🧠 The Debater Agent:** Takes a stance on a given topic, researches compelling arguments and potential counter-arguments, and builds a powerful, evidence-based case.
* **⚖️ The Judge Agent:** Analyzes the debate, evaluates the evidence and logic presented, and provides a final, strategic verdict on which argument is more sound.

---
## ⚙️ Setup and Installation

Follow these steps to get the Debating Agent Crew running on your local machine.

### Step 1: Clone the Repository

First, clone the main repository and navigate into the correct project directory.
```bash
git clone [https://github.com/Ujjwal012003/Agentic-Ai.git](https://github.com/Ujjwal012003/Agentic-Ai.git)
cd Agentic-Ai/Debating_Agent/crew/debate
```

### Step 2: Install `uv`

This project uses **`uv`** for fast and efficient package management. If you don't have it, install it with pip:
```bash
pip install uv
```

### Step 3: Install Project Dependencies

The simplest way to create the virtual environment and install all necessary packages is by using the `crewai` command-line tool.
```bash
crewai install
```
This command will use `uv` to create a `.venv` folder and install all the dependencies listed in your `pyproject.toml` file.

---
## 🔑 Configuration

Before running the crew, you must provide your Large Language Model (LLM) API key.

1.  Find the `.env` file in the project directory.
2.  Open it and add your API key. Depending on the model you're using in `agents.yaml`, it will look like one of these:
    ```
    OPENAI_API_KEY="sk-..."
    ```
    or
    ```
    GOOGLE_API_KEY="..."
    ```

---
## 🚀 Running the Agent

With the setup complete, you can now run the agent crew. Execute the following command from the project's root directory:
```bash
crewai run
```
By default, the agents will begin their debate on the topic defined in `src/debate/main.py` and, upon completion, will generate a `report.md` file in the root folder containing the judge's final verdict.

---
## 🔧 Customizing Your Crew

You can easily adapt this project to debate any topic you want:

* **Modify Agents:** Edit `src/debate/config/agents.yaml` to change the roles, goals, or backstories of your agents.
* **Modify Tasks:** Edit `src/debate/config/tasks.yaml` to change the instructions or expected outputs for the tasks.
* **Set the Topic:** Open `src/debate/main.py` to change the input `topic` for the debate.

---
## Support

For more help or information about `crewAI`, check out the official resources:
* [Official Documentation](https://docs.crewai.com)
* [GitHub Repository](https://github.com/joaomdmoura/crewAI)
* [Discord Community](https://discord.com/invite/X4JWnZnxPb)
