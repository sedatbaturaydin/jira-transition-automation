import os
from dotenv import load_dotenv
from jira import JIRA

load_dotenv()

jira_url = os.getenv('JIRA_URL')
jira_username = os.getenv('JIRA_USERNAME')
jira_token = os.getenv('JIRA_API_TOKEN')

jira = JIRA(jira_url, basic_auth=(jira_username, jira_token))
issue_key = "ARZ-3112"

issue= jira.issue(issue_key)

status_name = issue.fields.status.name
status_code = issue.fields.status.id

print(f"{status_name} {status_code}")

