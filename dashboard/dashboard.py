
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from Google Drive
DATA_PATH = "/content/drive/My Drive/MC03 Proyek Analisis Data Python/dashboard/main_data.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

# Load data
df = load_data()

# Streamlit App
st.title("📊 Bike Sharing Dashboard")
st.sidebar.header("Filter Data")

# Sidebar filters
season = st.sidebar.selectbox("Pilih Musim:", df['season_day'].unique())
weather = st.sidebar.selectbox("Pilih Kondisi Cuaca:", df['weathersit_day'].unique())

df_filtered = df[(df['season_day'] == season) & (df['weathersit_day'] == weather)]

st.write("### Statistik Data")
st.write(df_filtered.describe())

# Visualization 1: Penyewaan Berdasarkan Musim
st.write("### Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.boxplot(x='season_day', y='cnt_day', data=df, ax=ax)
st.pyplot(fig)

# Visualization 2: Penyewaan Berdasarkan Cuaca
st.write("### Penyewaan Sepeda Berdasarkan Cuaca")
fig, ax = plt.subplots()
sns.boxplot(x='weathersit_day', y='cnt_day', data=df, ax=ax)
st.pyplot(fig)

# Visualization 3: Penyewaan per Jam
st.write("### Pola Penyewaan Sepeda Berdasarkan Jam")
df['hr'] = pd.to_numeric(df['hr'], errors='coerce')  # Pastikan 'hr' numerik
df_grouped = df.groupby('hr').mean(numeric_only=True).reset_index()  # Gunakan numeric_only=True

fig, ax = plt.subplots()
sns.lineplot(x='hr', y='cnt_hour', data=df_grouped, ax=ax)
plt.xlabel("Jam")
plt.ylabel("Rata-rata Penyewaan")
st.pyplot(fig)
