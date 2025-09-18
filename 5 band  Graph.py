import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------
# Step 1: Dataset load karo
# -----------------------------
file_path = "eeg_7ch_bands_labels.csv"  # apna dataset ka naam
data = pd.read_csv(file_path)

st.title("EEG Bands Visualization (Average Across 7 Channels)")

# -----------------------------
# Step 2: Bands define karo
# -----------------------------
bands = ["Delta", "Theta", "Alpha", "Beta", "Gamma"]

# -----------------------------
# Step 3: Har band ka average across 7 channels
# -----------------------------
avg_bands = {}
st.subheader("Band-wise Column Selection & Average Calculation")

for band in bands:
    band_cols = [col for col in data.columns if band in col]  # band wali sari columns
    avg_bands[band] = data[band_cols].mean(axis=1)  # har sample ka average

    # Show columns list
    st.write(f"**{band} Columns:**", band_cols)

    # Example calculation (pehle 10 rows)
    calc_example = data[band_cols].head(10)
    calc_example[f"{band}_Avg"] = avg_bands[band].head(10)
    st.write(calc_example)

# -----------------------------
# Step 4: Graph plot karo
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

for band in bands:
    ax.plot(avg_bands[band], label=band)

ax.set_title("EEG Band Power Across Samples (Average of 7 Channels)")
ax.set_xlabel("Sample Index")
ax.set_ylabel("Power")
ax.legend()
ax.grid(True)

# Show graph in Streamlit
st.pyplot(fig)

# -----------------------------
# Step 5: Graph save karo
# -----------------------------
plt.savefig("eeg_bands_plot.png")  # same folder me save hoga
st.success("✅ Graph saved as eeg_bands_plot.png")
