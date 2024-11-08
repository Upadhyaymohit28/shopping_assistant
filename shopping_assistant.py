import openai
from sqlalchemy import create_engine, Column, String, Float, Text, or_
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up OpenAI API key
openai.api_key = "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"

# ================================
# Database Setup
# ================================
engine = create_engine('sqlite:///product_reviews.db', echo=False)
Base = declarative_base()

class ProductReview(Base):
    __tablename__ = 'product_reviews'

    product_id = Column(String, primary_key=True)
    product_name = Column(String)
    category = Column(String)
    discounted_price = Column(Text)
    actual_price = Column(Text)
    discount_percentage = Column(Text)
    rating = Column(Float)
    rating_count = Column(Text)
    about_product = Column(Text)
    img_link = Column(Text)
    product_link = Column(Text)

Session = sessionmaker(bind=engine)
db_session = Session()

# ================================
# GPT-4 Integration
# ================================
conversation_history = [
    {"role": "system", "content": "You are a helpful shopping assistant, who helps users find products, calculate totals, manage the cart, and process orders."}
]

def get_gpt4_response(user_input):
    """
    Sends user input to the GPT-4 model and retrieves the response.
    """
    conversation_history.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=conversation_history,
        max_tokens=150,
        temperature=0.7
    )
    assistant_response = response['choices'][0]['message']['content'].strip()
    conversation_history.append({"role": "assistant", "content": assistant_response})
    return assistant_response

# ================================
# Cart Management Functions
# ================================

def add_to_cart(product_name, session, quantity=1):
    """
    Adds a product to the user's cart based on the product name.
    """
    # Search for the product in the database using the given product name
    result = db_session.query(ProductReview).filter(
        ProductReview.product_name.ilike(f"%{product_name}%")
    ).first()
    
    if result:
        # Check if the item already exists in the cart to update the quantity
        existing_item = next((item for item in session["shopping_cart"] if item["name"] == result.product_name), None)
        if existing_item:
            existing_item["quantity"] += quantity
        else:
            # Add a new item to the cart with the specified quantity
            item = {"name": result.product_name, "price": result.discounted_price, "quantity": quantity}
            session["shopping_cart"].append(item)
        return f"{quantity}x {result.product_name} has been added to your cart."
    
    return f"Product '{product_name}' not found in our inventory."

def view_cart(session):
    """
    Displays the current items in the user's cart.
    """
    if session["shopping_cart"]:
        response = "Your cart contains:\n"
        for item in session["shopping_cart"]:
            response += f"- {item['name']} (x{item['quantity']}) - Price: {item['price']}\n"
        return response
    return "Your cart is empty."

def calculate_total(session):
    """
    Calculates the total price of all items in the user's cart.
    """
    if not session["shopping_cart"]:
        return "Your cart is empty."
    total_price = sum(float(item["price"]) * item["quantity"] for item in session["shopping_cart"])
    return f"The total for your items in the cart is ${total_price:.2f}."

def checkout(session):
    """
    Processes the checkout for the current cart.
    """
    if not session["shopping_cart"]:
        return "Your cart is empty. Add items before checking out."
    
    order_id = str(len(session.get("orders", [])) + 1).zfill(5)
    orders = session.get("orders", [])
    orders.append({"order_id": order_id, "items": session["shopping_cart"].copy()})
    session["orders"] = orders
    session["shopping_cart"] = []  # Clear the cart after checkout
    return f"Your order #{order_id} has been placed successfully! Expected delivery is within 3-5 business days."

# ================================
# Handle Intent Function
# ================================

def handle_intent(user_input, session):
    """
    Handles user input by calling the appropriate cart or assistant functions.
    """
    user_input_lower = user_input.lower()

    # Handle cart operations and other actions
    if "add to cart" in user_input_lower or "add" in user_input_lower:
        # Extract product name and quantity
        quantity = 1
        parts = user_input_lower.split()
        if "add" in parts:
            index = parts.index("add")
            if len(parts) > index + 1 and parts[index + 1].isdigit():
                quantity = int(parts[index + 1])
                product_name = ' '.join(parts[index + 2:])
            else:
                product_name = ' '.join(parts[index + 1:])
        return add_to_cart(product_name, session, quantity)

    elif "view cart" in user_input_lower or "what's in my cart" in user_input_lower:
        return view_cart(session)

    elif "checkout" in user_input_lower:
        return checkout(session)

    elif "total" in user_input_lower:
        return calculate_total(session)

    else:
        # Fallback to GPT-4 for general questions or product recommendations
        return get_gpt4_response(user_input)

# ================================
# Command-Line Assistant Function
# ================================

def start_assistant():
    """
    Starts the command-line shopping assistant.
    """
    # Local session equivalent for the command line
    session = {"shopping_cart": [], "orders": []}
    print("Hello! I'm your Shopping Assistant, Tan. How can I help you today?")

    while True:
        user_input = input("> ")
        if not user_input.strip():
            print("Goodbye! Have a great day!")
            break

        # Pass the local session to the handle_intent function
        response = handle_intent(user_input, session)
        print(response)

# Only run the assistant if this script is executed directly
if __name__ == "__main__":
    start_assistant()
