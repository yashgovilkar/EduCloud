from flask import Flask, jsonify

app = Flask(__name__)

# Database connection details (replace with your actual credentials)
DATABASE_URL = "postgresql://user:password@host:port/database"

# Connect to the database (implementation to be added later)


@app.route("/")
def hello_world():
    return "EduCloud API: Under development!"


if __name__ == "__main__":
    app.run(debug=True)
