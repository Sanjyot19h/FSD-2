

* Microservices architecture divides a system into **small independent services**
* Each service runs separately (different ports) and performs a **specific task**
* Learned how to build APIs using **Flask framework**
* Understood HTTP methods:

  * **GET** → Fetch data
  * **PUT** → Update data
 
---
 

* Created two Flask-based microservices:

  * **Customer Service (Port 5000)**

    * Fetches customer details and their orders

  * **Order Service (Port 5001)**

    * Fetches order details
    * Updates order status

* Stored data in **Python dictionaries (in-memory)**

* Implemented API routes:

  * `GET /customers/<id>/orders`
  * `GET /orders/<id>`
  * `PUT /orders/<id>`

* Tested APIs using Postman:

  * Sent **GET requests** to fetch data
  * Sent **PUT request** to update order status

* Verified updated data using GET request again

---
 