# E-Commerce: Schema-Agnostic Dynamic Product Catalog

A NoSQL project built using MongoDB, PyMongo, and Streamlit.

## Features
- Add products with dynamic category-specific attributes
- View all products
- Search products by name, brand, and category
- Update product stock
- Delete products
- Schema-agnostic MongoDB document design

## Technologies
- Python
- MongoDB Atlas
- PyMongo
- Streamlit
- Pandas

## How to Run
1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create `.streamlit/secrets.toml` and add MongoDB credentials.

3. Insert sample data:

```bash
python seed_data.py
```

4. Run the app:

```bash
streamlit run app.py
```
