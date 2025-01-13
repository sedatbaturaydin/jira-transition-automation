import os
from dotenv import load_dotenv
from jira import JIRA

load_dotenv()

jira_url = os.getenv('JIRA_URL')
jira_username = os.getenv('JIRA_USERNAME')
jira_token = os.getenv('JIRA_API_TOKEN')

jira = JIRA(jira_url, basic_auth=(jira_username, jira_token))

issue_key = "ARZ-3112"

try:
    transitions = jira.transitions(issue_key)
    print("Geçerli transitionlar:")
    for transition in transitions:
        print(f"ID: {transition['id']}, Ad: {transition['name']}")
except Exception as e:
    print(f"Error occupied: {e}")
