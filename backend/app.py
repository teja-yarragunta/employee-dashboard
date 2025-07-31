from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
print(os.getenv("MONGO_URI")) 

app = Flask(__name__)
CORS(app)

# Get the Mongo URI from the environment
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)
try:
    mongo.db.command("ping")
    print("Connected to MongoDB!")
except Exception as e:
    print(f"MongoDB connection error: {e}")

print(os.getenv("MONGO_URI"))


frontend_folder = os.path.join(os.getcwd(), "..", "frontend")
dist_folder = os.path.join(frontend_folder, "dist")

# Serve static files
@app.route("/", defaults={"filename": ""})
@app.route("/<path:filename>")
def index(filename):
    if not filename:
        filename = "index.html"
    return send_from_directory(dist_folder, filename)

from routes import *  # Import routes here to avoid circular import issues
print(app.url_map)  # Print the updated URL map after importing routes

if __name__ == "__main__":
    app.run(debug=True)
