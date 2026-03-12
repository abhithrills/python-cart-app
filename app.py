from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# Sample products
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 2000}
]

@app.route('/')
def home():
    return render_template("store.html", products=products)

@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    session.modified = True

    return redirect('/')

@app.route('/cart')
def cart():
    cart_items = []
    total = 0

    if "cart" in session:
        for id in session["cart"]:
            for product in products:
                if product["id"] == id:
                    cart_items.append(product)
                    total += product["price"]

    return render_template("cart.html", cart_items=cart_items, total=total)

if __name__ == '__main__':
   app.run(debug=True)
