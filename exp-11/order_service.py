from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ HOME ROUTE (ADD HERE)
@app.route('/')
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running"
    })

# In-memory orders
orders = {
    101: {"status": "Pending"},
    102: {"status": "Shipped"}
}

# API
@app.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json()

    if not data or "status" not in data:
        return jsonify({"error": "Status is required"}), 400

    orders[order_id]["status"] = data["status"]

    return jsonify({
        "message": "Order updated successfully",
        "order_id": order_id,
        "new_status": orders[order_id]["status"]
    })

if __name__ == '__main__':
    app.run(port=5001, debug=True)