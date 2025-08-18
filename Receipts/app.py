# Import necessary modules from Flask
from flask import Flask, render_template, request

# Create an instance of the Flask application
app = Flask(__name__)

# Define the main route for the app, supporting both GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def receipt():
    transactions = []  # List to store each transaction
    total = 0          # Variable to keep the total cost

    # If the request is a POST (form submitted by user)
    if request.method == 'POST':
        # Collect lists of submitted items, quantities, and prices
        items = request.form.getlist('item')
        qtys = request.form.getlist('qty')
        prices = request.form.getlist('price')
        for item, qty, price in zip(items, qtys, prices): 
            transactions.append({'item': item, 'qty': int(qty), 'price': float(price)})
            # Update total amount
            total += int(qty) * float(price)

        # Render the receipt template, passing the transactions and total to the HTML
        return render_template('receipt.html', transactions=transactions, total=total)

    # If the request is a GET (user opens the page), show the input form
    return render_template('form.html')

# Start the application only if this file is run (not imported as a module)
if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode for better error messages and live reload

