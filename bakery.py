import streamlit as st
import pandas as pd
import altair as alt 

@st.cache_data
def load_data():
    df = pd.read_csv("Datasets/modified.csv")
    return df.head(1000)

st.title("Demo App")

st.subheader("Learn the basic structure")

st.write("Bakery Sales Data")
df = load_data()
st.write(df)
articles = df.article.unique()
articles_selection = st.multiselect("Choose Product", [article for article in articles])
articles_selected = df[df['article'].isin(articles_selection)]
st.write(articles_selected.head())
# plotting

# line chart
st.write("""### Sales over Time """)
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(articles_selected['datetime']


# mine (using altair)
# chart = alt.Chart(df).mark_line().encode(x='datetime', y='sales')
# st.write(chart)