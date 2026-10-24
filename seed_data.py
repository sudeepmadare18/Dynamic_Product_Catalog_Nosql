from db import get_collection

collection = get_collection()

products = [
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
    },
    {
        "name": "Dell Inspiron 15",
        "category": "Laptop",
        "brand": "Dell",
        "price": 55000,
        "stock": 15,
        "attributes": {
            "processor": "Intel i5",
            "ram": "16GB",
            "storage": "512GB SSD"
        },
        "tags": ["electronics", "computer"]
    },
    {
        "name": "Nike Running Shoes",
        "category": "Footwear",
        "brand": "Nike",
        "price": 4999,
        "stock": 40,
        "attributes": {
            "size": "9",
            "color": "Black",
            "material": "Synthetic"
        },
        "tags": ["fashion", "shoes"]
    },
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
]

collection.delete_many({})
collection.insert_many(products)

print("Sample products inserted successfully")
