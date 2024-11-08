from flask import Flask, render_template, request, jsonify, session
from shopping_assistant import handle_intent
from flask_session import Session

# Set up Flask application
app = Flask(__name__)

# Session configuration
app.secret_key = "super_secret_key"  # Set a secret key for session encryption
app.config["SESSION_TYPE"] = "filesystem"  # Use filesystem session storage
Session(app)  # Initialize session

@app.route('/')
def home():
    """
    Renders the homepage where the shopping assistant interface is displayed.
    """
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    """
    Handles user input from the web interface, processes it using `handle_intent`, and returns the assistant's response.
    """
    user_input = request.json['message']

    # Initialize session variables if not already present
    if "shopping_cart" not in session:
        session["shopping_cart"] = []  # Shopping cart to store items user wants to buy
    if "orders" not in session:
        session["orders"] = []  # Stores placed orders

    # Pass the session to `handle_intent` for processing
    assistant_response = handle_intent(user_input, session)

    # Update the session to reflect changes in shopping cart or orders
    session.modified = True

    # Return the response to be displayed in the UI
    return jsonify({'response': assistant_response})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
