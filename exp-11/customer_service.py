from flask import Flask, jsonify

app = Flask(__name__)

# In-memory data
customers = {
    1: {"name": "John"},
    2: {"name": "Alice"}
}

orders = {
    1: [{"order_id": 101, "status": "Pending"}],
    2: [{"order_id": 102, "status": "Shipped"}]
}

# Home route (fixes Not Found error)
@app.route('/')
def home():
    return jsonify({
        "service": "Customer Service",
        "status": "running"
    })

# API: Get customer orders
@app.route('/customer/<int:customer_id>/orders', methods=['GET'])
def get_orders(customer_id):
    if customer_id in orders:
        return jsonify({
            "customer_id": customer_id,
            "orders": orders[customer_id]
        })
    return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)