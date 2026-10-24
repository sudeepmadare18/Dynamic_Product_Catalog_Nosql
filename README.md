# 🛒 E-Commerce: Schema-Agnostic Dynamic Product Catalog

A NoSQL-based e-commerce product catalog built using **MongoDB**, **PyMongo**, and **Streamlit**.

This project demonstrates how MongoDB can store products with different attributes in a single collection without requiring a fixed database schema. It is designed as an academic NoSQL database project.

---

## 📌 Project Overview

In an e-commerce platform, different products require different details:

- A **mobile** may have RAM, storage, and camera information.
- A **laptop** may have processor, RAM, and storage details.
- Clothing may have size, color, and fabric.
- Footwear may have size, color, and material.

In a traditional SQL database, this would require multiple tables or frequent schema changes. In this project, MongoDB stores every product as a flexible JSON-like document inside one collection.

Common product details remain consistent, while category-specific details are stored inside an embedded `attributes` object.

---

## ✨ Features

- Add new products with dynamic attributes
- View all products in an interactive Streamlit interface
- Search products by name, brand, or category
- Update product stock
- Delete products
- Store category-specific attributes without changing the database schema
- MongoDB Atlas cloud database integration
- Simple and clean Streamlit user interface

---

## 🧠 Why MongoDB?

MongoDB is a NoSQL document database. Instead of storing data in rows and columns, it stores data as documents in BSON/JSON-like format.

This project is **schema-agnostic** because each product document can contain different fields.

### Example: Mobile Product

```json
{
  "name": "iPhone 15",
  "category": "Mobile",
  "brand": "Apple",
  "price": 79999,
  "stock": 25,
  "attributes": {
    "ram": "8GB",
    "storage": "128GB",
    "camera": "48MP"
  },
  "tags": ["electronics", "smartphone"]
}
```

### Example: Clothing Product

```json
{
  "name": "Cotton T-Shirt",
  "category": "Clothing",
  "brand": "Levis",
  "price": 999,
  "stock": 100,
  "attributes": {
    "size": "M",
    "color": "Black",
    "fabric": "Cotton"
  },
  "tags": ["fashion", "tshirt"]
}
```

Both products are stored in the same `products` collection, even though they have different attributes.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| MongoDB Atlas | Cloud NoSQL database |
| PyMongo | Python driver for MongoDB |
| Streamlit | Web application interface |
| Pandas | Data handling and tabular display |

---

## 📂 Project Structure

```text
dynamic_product_catalog/
├── app.py                  # Streamlit web application
├── db.py                   # MongoDB connection logic
├── seed_data.py            # Inserts sample product data
├── requirements.txt        # Required Python libraries
├── README.md               # Project documentation
└── .streamlit/
    └── secrets.example.toml  # Example configuration file
```

> Note: The real `secrets.toml` file is not uploaded to GitHub for security reasons.

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone [https://github.com/sudeepmadare1/dynamic-product-catalog.git](https://github.com/sudeepmadare1/dynamic-product-catalog.git)
cd dynamic-product-catalog
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create MongoDB Atlas database

1. Create a free account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Create a free M0 cluster.
3. Create a database user with read and write access.
4. Add your IP address in the Network Access list.
5. Copy the cluster host name.

### 4. Create secrets file

Create a folder named `.streamlit` and inside it create a file named `secrets.toml`.

Add the following details:

```toml
[mongo]
username = "your_mongodb_username"
password = "your_mongodb_password"
host = "your_cluster_host.mongodb.net"
db_name = "ecommerce_db"
collection_name = "products"
```

> Do not share or upload the real `secrets.toml` file to GitHub.

### 5. Insert sample data

```bash
python seed_data.py
```

### 6. Run the application

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

## 🚀 How to Use

### View Products

Open the **View Products** page to see all products stored in MongoDB.

### Add Product

1. Open **Add Product**.
2. Enter product name, category, brand, price, stock, and tags.
3. Add only the attributes required for that product.
4. Click **Add Product**.

Example: A Smart TV can have attributes such as screen size, resolution, and warranty.

### Search Products

Search products using:

- Product name
- Brand name
- Category

### Update Stock

Select a product and enter the new stock quantity.

### Delete Product

Select a product and delete it from MongoDB.

---

## 🗄️ Database Design

### Database Name

```text
ecommerce_db
```

### Collection Name

```text
products
```

### Common Fields

| Field | Description |
|---|---|
| `name` | Product name |
| `category` | Product category |
| `brand` | Product brand |
| `price` | Product price |
| `stock` | Available quantity |
| `attributes` | Category-specific details |
| `tags` | Product tags |

### Schema-Agnostic Design

The `attributes` field is flexible. Each product can store different keys and values.

| Product Type | Example Attributes |
|---|---|
| Mobile | RAM, storage, camera |
| Laptop | Processor, RAM, storage |
| Clothing | Size, color, fabric |
| Footwear | Size, color, material |
| Television | Screen size, resolution, warranty |

---

## 🔐 Security

- MongoDB credentials are stored in `.streamlit/secrets.toml`.
- The real secrets file is excluded using `.gitignore`.
- A sample configuration file, `secrets.example.toml`, is provided for reference.
- Never upload real database passwords to GitHub.

---

## 🎓 Learning Outcomes

Through this project, the following NoSQL concepts are demonstrated:

- MongoDB document database concepts
- Schema-agnostic data modeling
- Embedded documents
- CRUD operations using PyMongo
- MongoDB Atlas cloud deployment
- Streamlit-based database application development
- Secure handling of database credentials

---

## 👨‍💻 Author

**Sudeep Madare**  
NoSQL Database Project  
E-Commerce: Schema-Agnostic Dynamic Product Catalog
