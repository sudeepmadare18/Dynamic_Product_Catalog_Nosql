import streamlit as st
import pandas as pd

from db import get_collection

st.set_page_config(
    page_title="Dynamic Product Catalog",
    page_icon="🛒",
    layout="wide"
)

collection = get_collection()

st.title("🛒 E-Commerce Dynamic Product Catalog")
st.caption("MongoDB schema-agnostic product catalog built with PyMongo and Streamlit")

menu = st.sidebar.radio(
    "Navigation",
    [
        "View Products",
        "Add Product",
        "Search Products",
        "Update Stock",
        "Delete Product"
    ]
)

if menu == "View Products":

    st.subheader("All Products")

    products = list(collection.find())

    if not products:
        st.warning("No products found. Run seed_data.py first.")
    else:
        for product in products:
            with st.expander(f"{product['name']} — ₹{product['price']}"):
                st.write(f"**Category:** {product['category']}")
                st.write(f"**Brand:** {product['brand']}")
                st.write(f"**Stock:** {product['stock']}")

                st.write("**Category-specific attributes:**")

                for key, value in product.get("attributes", {}).items():
                    st.write(f"- {key}: {value}")

                st.write("**Tags:**")
                st.write(", ".join(product.get("tags", [])))

elif menu == "Add Product":

    st.subheader("Add New Product")

    name = st.text_input("Product Name")
    category = st.text_input("Category")
    brand = st.text_input("Brand")
    price = st.number_input("Price", min_value=0)
    stock = st.number_input("Stock", min_value=0)
    tags = st.text_input("Tags (comma separated)")

    st.markdown("### Dynamic Attributes")
    st.info("Add only the attributes required for this product category.")

    attribute_count = st.number_input(
        "Number of attributes",
        min_value=0,
        max_value=10,
        value=2
    )

    attributes = {}

    for i in range(int(attribute_count)):
        col1, col2 = st.columns(2)

        with col1:
            attr_name = st.text_input(
                f"Attribute {i + 1} name",
                key=f"attr_name_{i}"
            )

        with col2:
            attr_value = st.text_input(
                f"Attribute {i + 1} value",
                key=f"attr_value_{i}"
            )

        if attr_name and attr_value:
            attributes[attr_name] = attr_value

    if st.button("Add Product"):
        if name and category and brand:
            product = {
                "name": name,
                "category": category,
                "brand": brand,
                "price": float(price),
                "stock": int(stock),
                "attributes": attributes,
                "tags": [
                    tag.strip()
                    for tag in tags.split(",")
                    if tag.strip()
                ]
            }

            collection.insert_one(product)
            st.success(f"Product '{name}' added successfully!")
        else:
            st.error("Please enter product name, category, and brand.")

elif menu == "Search Products":

    st.subheader("Search Products")

    search_text = st.text_input("Search by product name or brand")
    category_filter = st.text_input("Filter by category")

    query = {}

    if search_text:
        query["$or"] = [
            {"name": {"$regex": search_text, "$options": "i"}},
            {"brand": {"$regex": search_text, "$options": "i"}}
        ]

    if category_filter:
        query["category"] = {"$regex": category_filter, "$options": "i"}

    products = list(collection.find(query))

    if products:
        df = pd.DataFrame(products)

        if "_id" in df.columns:
            df = df.drop(columns=["_id"])

        if "attributes" in df.columns:
            df["attributes"] = df["attributes"].astype(str)

        if "tags" in df.columns:
            df["tags"] = df["tags"].apply(
                lambda x: ", ".join(x) if isinstance(x, list) else x
            )

        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No matching products found.")

elif menu == "Update Stock":

    st.subheader("Update Product Stock")

    products = list(collection.find({}, {"name": 1}))
    product_names = [p["name"] for p in products]

    selected_product = st.selectbox("Select product", product_names)
    new_stock = st.number_input("New stock quantity", min_value=0)

    if st.button("Update Stock"):
        collection.update_one(
            {"name": selected_product},
            {"$set": {"stock": int(new_stock)}}
        )

        st.success(f"Stock updated for {selected_product}")

elif menu == "Delete Product":

    st.subheader("Delete Product")

    products = list(collection.find({}, {"name": 1}))
    product_names = [p["name"] for p in products]

    selected_product = st.selectbox("Select product", product_names)

    if st.button("Delete Product"):
        collection.delete_one({"name": selected_product})
        st.success(f"Product '{selected_product}' deleted successfully!")
