# Company Research Crew

![crewAI](https://img.shields.io/badge/powered%20by-crewAI-blue?style=for-the-badge)

This project utilizes a crew of AI agents, powered by [crewAI](https://crewai.com), to conduct comprehensive research on a specified company and generate a detailed analytical report.

## Overview 📝

This crew automates the process of gathering and analyzing business intelligence. It consists of two specialized agents that work in sequence:

1.  **Senior Financial Researcher**: This agent uses web search tools to conduct thorough research on the target company. It focuses on the company's current health, historical performance, challenges, opportunities, and recent news.
2.  **Market Analyst and Report Writer**: This agent takes the raw research data, analyzes it for trends and insights, and compiles a professional, well-structured report.

The final output is a polished `report.md` file, saved in the `output/` directory, providing a comprehensive overview and market outlook for the company.

***

## Getting Started

Follow these instructions to set up and run the Company Research Crew on your local machine.

### Prerequisites

* Python `>=3.10 <3.14`
* An **OpenAI API Key** for the LLM.
* A **Serper API Key** for the web search tool.

### Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Install `uv`**: This project uses UV for fast dependency management.
    ```bash
    pip install uv
    ```

3.  **Install project dependencies**: Use the `crewai` command-line tool to set up the environment.
    ```bash
    crewai install
    ```

### Configuration

You must provide API keys for the services used by the crew.

1.  Create a `.env` file in the root directory of the project.
2.  Add your API keys to the `.env` file. **You need keys for both OpenAI and Serper.**

    ```env
    # .env file

    OPENAI_API_KEY="sk-..."
    SERPER_API_KEY="your_serper_key_here"
    ```

***

## Running the Crew 🚀

To kickstart your crew of AI agents and begin the financial analysis, simply run the following command from the project's root folder:

```bash
crewai run
