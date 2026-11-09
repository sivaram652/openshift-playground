from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page (root URL)
@app.route('/')
def home():
    return "<h1>Hello, World!</h1><p>Welcome to your first Flask app.</p>"

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
