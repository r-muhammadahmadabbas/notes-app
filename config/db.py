from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Now it fetches the secret safely from the .env file
MONGO_URI = os.getenv("MONGO_URI")

conn = MongoClient(MONGO_URI)