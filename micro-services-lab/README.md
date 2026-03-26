 
 ## What I Understood

* Microservices architecture divides a system into **small independent services**
* Each service runs separately (different ports) and performs a **specific task**
* Learned how to build APIs using **Flask framework**
* Understood HTTP methods:

  * **GET** → Fetch data
  * **PUT** → Update data
* Learned about **in-memory data storage** using Python dictionaries
* No database is used → data is **temporary**
* Data is **lost when server restarts**
* Understood how APIs communicate through **URLs (routes)**
* Learned how to test APIs using **Postman**
* Importance of correct **routes, methods, and ports**

---

##  What I Did

* Created two Flask-based microservices:

  * **Customer Service (Port 5000)**

    * Fetches customer details and their orders

  * **Order Service (Port 5001)**

    * Fetches order details
    * Updates order status
 
* Implemented API routes:

  * `GET /customers/<id>/orders`
  * `GET /orders/<id>`
  * `PUT /orders/<id>`

* Tested APIs using Postman:

  * Sent **GET requests** to fetch data
  * Sent **PUT request** to update order status
 
---
  