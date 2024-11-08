# Shopping Assistant

This project is a shopping assistant that allows users to interact with an AI-powered assistant to manage a shopping cart, add products, view the cart, calculate totals, and proceed to checkout. The assistant can be accessed via both a command-line interface and a web application built using Flask.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Folder Structure](#folder-structure)
3. [Setup Instructions](#setup-instructions)
4. [Database Setup and Importing Data](#database-setup-and-importing-data)
5. [Running the Project](#running-the-project)
6. [Testing and Validation](#testing-and-validation)
7. [Common Issues and Solutions](#common-issues-and-solutions)

### Project Overview

The shopping assistant uses OpenAI's GPT-4 model for managing conversation flow, while product-related actions (e.g., adding items to cart, viewing the cart) are handled using Python functions. The web app provides an easy-to-use interface for interacting with the assistant.

### Folder Structure

The project files are organized as follows:

```
shopping_assistant/
  |- app.py                # Flask web app for the shopping assistant
  |- shopping_assistant.py # The core logic for cart management and OpenAI integration
  |- setup_database.py     # Script to set up the database schema
  |- import_data.py        # Script to import product data into the database
  |- templates/
      |- index.html        # Frontend HTML file for the web app
  |- static/
      |- styles.css        # Stylesheet for the web interface
      |- script.js         # JavaScript for handling chat interactions in the web app
  |- product_reviews.db    # SQLite database file for product information
  |- README.md             # Project documentation
```

### Setup Instructions

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**

   Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd shopping_assistant
   ```

2. **Create a Virtual Environment**

   Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**

   Install the necessary packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure you have the following in your `requirements.txt`:
   ```
   Flask
   openai
   sqlalchemy
   flask-session
   ````

4. **Set OpenAI API Key**

   Set up your OpenAI API key by either exporting it as an environment variable or directly in your Python files:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"  # Linux/MacOS
   set OPENAI_API_KEY="your_openai_api_key"     # Windows
   ```

### Database Setup and Importing Data

1. **Create Database Schema**

   Run the `setup_database.py` script to create the necessary database schema:
   ```bash
   python setup_database.py
   ```

2. **Import Product Data**

   Use the `import_data.py` script to populate the database with product information:
   ```bash
   python import_data.py
   ```
   Ensure the `product_reviews.db` file is created successfully and contains product data.

### Running the Project

You can run the shopping assistant either as a command-line assistant or as a web app.

#### 1. Running via Command Line

To start the assistant in the terminal, use:
```bash
python shopping_assistant.py
```
This will start a conversation in the terminal where you can interact with the assistant, add items to your cart, and proceed to checkout.

#### 2. Running via Flask Web App

To run the Flask web app, use:
```bash
python app.py
```
Once the server starts, navigate to `http://127.0.0.1:5000/` in your browser. You can then interact with the shopping assistant through the web interface.

### Testing and Validation

1. **Testing Scenarios**
   - Test various shopping scenarios to ensure the assistant responds accurately and manages the cart correctly.
   - Example scenarios include adding multiple items, checking the cart contents, removing items, and calculating the total.

2. **Edge Case Handling**
   - Ensure the assistant handles cases such as adding items not in inventory, checking out with an empty cart, or providing invalid inputs.

3. **Sample Conversations**
   - Test conversations with different commands such as:
     - "Add 2 roses to my cart."
     - "View my cart."
     - "Proceed to checkout."
     - "What is the total?"

### Common Issues and Solutions

1. **Cart Not Retaining Items**
   - Ensure the Flask session is correctly configured, and `session.modified = True` is used after any changes to maintain session state.

2. **OpenAI API Issues**
   - Make sure the OpenAI API key is set correctly as an environment variable or in the code.
   - Check that your API usage limits have not been exceeded if you receive rate-limit errors.

3. **Port Already in Use**
   - If the default port (`5000`) is in use, specify a different port when running Flask:
   ```bash
   python app.py --port 5001
   ```

4. **Debugging Tips**
   - Use `print()` statements in `shopping_assistant.py` to debug any unexpected behavior when interacting with the assistant.
   - Use Flask’s debug mode (`debug=True`) to get detailed error messages in the web app.

### Contact Information

If you have any questions or need further assistance, feel free to contact the project maintainer.

Happy Shopping!

