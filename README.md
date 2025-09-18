import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------
# Step 1: Load the dataset
# -----------------------------
st.title("EEG Bands Visualization (Average Across 7 Channels)")

file_path = "eeg_7ch_bands_labels.csv"  # Path to your dataset
try:
    data = pd.read_csv(file_path)
    st.success(f"Dataset loaded successfully! Shape: {data.shape}")
except FileNotFoundError:
    st.error(f"File not found: {file_path}")
    st.stop()  # Stop Streamlit if file is missing

# -----------------------------
# Step 2: Define EEG bands
# -----------------------------
bands = ["Delta", "Theta", "Alpha", "Beta", "Gamma"]

# -----------------------------
# Step 3: Compute average across 7 channels for each band
# -----------------------------
avg_bands = {}
st.subheader("Band-wise Column Selection & Average Calculation")

for band in bands:
    # Select columns corresponding to this band
    band_cols = [col for col in data.columns if band.lower() in col.lower()]
    
    if not band_cols:
        st.warning(f"No columns found for {band}")
        continue
    
    # Calculate average for this band
    avg_bands[band] = data[band_cols].mean(axis=1)

    # Show the columns
    st.write(f"**{band} Columns:**", band_cols)

    # Show first 10 rows with average
    example_df = data[band_cols].head(10).copy()
    example_df[f"{band}_Avg"] = avg_bands[band].head(10)
    st.write(example_df)

# -----------------------------
# Step 4: Plot the graph
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

for band in avg_bands:  # Only iterate valid bands
    ax.plot(avg_bands[band], label=band)

ax.set_title("EEG Band Power Across Samples (Average of 7 Channels)")
ax.set_xlabel("Sample Index")
ax.set_ylabel("Power")
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# -----------------------------
# Step 5: Save the graph
# -----------------------------
plt.savefig("eeg_bands_plot.png", bbox_inches='tight')
st.success("✅ Graph saved as eeg_bands_plot.png in project folder")
