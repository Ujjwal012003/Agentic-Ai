# src/financial_researcher/main.py

#!/usr/bin/env python
import os
from financial_researcher.crew import ResearchCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    This function prompts the user for a company name and
    then kicks off the crew to generate a research report.
    """
    # Prompt the user for the company name
    company = input("Please enter the company to research: ")

    inputs = {
        'company': company
    }

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the final result
    print("\n\n==================== FINAL REPORT ====================\n\n")
    print(result)

    print(f"\n\nReport for {company} has been saved to output/report.md")

if __name__ == "__main__":
    run()
