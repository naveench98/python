from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def receipt():
    transactions = []
    total = 0
    if request.method == 'POST':
        items = request.form.getlist('item')
        qtys = request.form.getlist('qty')
        prices = request.form.getlist('price')
        for item, qty, price in zip(items, qtys, prices):
            transactions.append({'item': item, 'qty': int(qty), 'price': float(price)})
            total += int(qty) * float(price)
        return render_template('receipt.html', transactions=transactions, total=total)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
