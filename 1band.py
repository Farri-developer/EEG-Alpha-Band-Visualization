import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------
# Step 1: Dataset load karo
# -----------------------------
file_path = "eeg_7ch_bands_labels.csv"   # apna dataset ka naam
data = pd.read_csv(file_path)

st.title("EEG Alpha Band Visualization")

# -----------------------------
# Step 2: Alpha columns nikalo (Ch1_Alpha ... Ch7_Alpha)
# -----------------------------
alpha_cols = [col for col in data.columns if "Alpha" in col]

st.subheader("Alpha Columns (7 Channels)")
st.write(alpha_cols)

# -----------------------------
# Step 3: Har sample ke liye 7 channels ka Alpha average nikalo
# -----------------------------
alpha_avg = data[alpha_cols].mean(axis=1)

# Calculation dikhana
st.subheader("Alpha Band Calculation (per sample)")
st.write("Alpha Average = (Ch1_Alpha + Ch2_Alpha + ... + Ch7_Alpha) / 7")

# Show first 10 calculations as example
calc_example = data[alpha_cols].head(10)
calc_example["Alpha_Avg"] = alpha_avg.head(10)
st.write(calc_example)

# -----------------------------
# Step 4: Graph plot karo
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(alpha_avg, label="Alpha Average", color="blue")
ax.set_title("EEG Alpha Band Power (Average of 7 Channels)")
ax.set_xlabel("Sample Index")
ax.set_ylabel("Power")
ax.legend()
ax.grid(True)

# Save figure as PNG
fig.savefig("alpha_band_plot.png")   # same folder me save hoga
st.success("✅ Graph saved as alpha_band_plot.png")

# Show graph in Streamlit
st.pyplot(fig)
