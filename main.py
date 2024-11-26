import sys
import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.environ["NOTION_INTEGRATION_TOKEN"])

DATABASE_ID = os.environ["DATABASE_ID"]

def create_notion_entry(content):
    new_page = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Task Name": {
                "title": [
                    {
                        "text": {
                            "content": content
                        }
                    }
                ]
            }
        }
    }
    notion.pages.create(**new_page)
    print(f"New entry created with content: {content}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        entry_content = " ".join(sys.argv[1:])
        create_notion_entry(entry_content)
    else:
        print("Please provide the content for the Notion entry.")