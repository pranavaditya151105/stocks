import os
from database import get_collection
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    print("Testing connection to MongoDB Atlas...")
    try:
        # Check if environment variable is loaded
        mongo_uri = os.getenv("MONGO_URI")
        if not mongo_uri or "<db_username>" in mongo_uri:
            print("ERROR: MONGO_URI is missing or still contains placeholders in .env")
            return

        # Attempt to get collection (this triggers MongoClient initialization)
        collection = get_collection()
        
        # Simple operation to verify connection
        count = collection.count_documents({})
        print(f"SUCCESS: Connected to database. Current document count: {count}")
        
    except Exception as e:
        print(f"CONNECTION FAILED: {e}")
        print("\nPossible issues:")
        print("1. IP Address not whitelisted in Atlas.")
        print("2. Incorrect username or password in .env.")
        print("3. Special characters in password not URL-encoded.")

if __name__ == "__main__":
    test_connection()
