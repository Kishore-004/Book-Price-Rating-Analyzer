import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Book Price & Rating Analyzer", layout="centered")

# Load dataset
df = pd.read_csv("Books_to_Scrape_Data.csv")

st.title("📚 Book Price & Rating Analyzer")
st.markdown("Data scraped from [Books to Scrape](https://books.toscrape.com/)")

# Sidebar Filters
rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
df["RatingNum"] = df["Rating"].map(rating_map)

st.sidebar.header("Filter Options")
min_price, max_price = st.sidebar.slider("Price Range (£)", float(df["Price (£)"].min()), float(df["Price (£)"].max()), (float(df["Price (£)"].min()), float(df["Price (£)"].max())))
selected_rating = st.sidebar.multiselect("Select Rating", options=sorted(df["RatingNum"].unique()), default=sorted(df["RatingNum"].unique()))

# Apply filters
filtered = df[(df["Price (£)"] >= min_price) & (df["Price (£)"] <= max_price) & (df["RatingNum"].isin(selected_rating))]

st.subheader("📊 Filtered Dataset")
st.dataframe(filtered)

# Charts
st.subheader("Average Price by Rating")
avg_price = filtered.groupby("RatingNum")["Price (£)"].mean()
fig, ax = plt.subplots(figsize=(6,4))
avg_price.plot(kind="bar", color="skyblue", edgecolor="black", ax=ax)
ax.set_xlabel("Rating (Stars)")
ax.set_ylabel("Average Price (£)")
st.pyplot(fig)

st.subheader("Price Distribution")
fig2, ax2 = plt.subplots(figsize=(6,4))
ax2.hist(filtered["Price (£)"], bins=10, edgecolor='black')
ax2.set_xlabel("Price (£)")
ax2.set_ylabel("Count")
st.pyplot(fig2)

st.markdown("✅ _Developed with Python, BeautifulSoup, Pandas, and Streamlit._")
