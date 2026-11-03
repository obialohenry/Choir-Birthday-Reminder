import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

APP_CREDENTIALS = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
SPREADSHEET_ID = os.environ["GOOGLE_SHEETS_SPREADSHEET_ID"]