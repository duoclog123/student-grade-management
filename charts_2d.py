import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. DATA PREPARATION ---
data = {
    "Student": ["Alice", "Bob", "Carol", "David", "Emma"],
    "Math": [85, 70, 95, 60, 88],
    "Physics": [78, 65, 88, 72, 91],
    "English": [92, 75, 90, 68, 84]
}
df = pd.DataFrame(data)

# Calculate average score
df["Average"] = (df["Math"] + df["Physics"] + df["English"]) / 3

# Grading function (for the pie chart)
def classify(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

df["Grade"] = df["Average"].apply(classify)
grade_counts = df["Grade"].value_counts()

# --- 2. PLOTTING (COMBINE 2 CHARTS) ---

# Create a figure with 1 row, 2 columns (Side-by-side)
# figsize=(14, 6): Width 14, Height 6
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Set white background style (to match requirements)
sns.set_style("white")

# === CHART 1: PIE CHART (Grade Distribution) 
# Plot on the first axis: ax[0]
ax[0].pie(
    grade_counts, 
    labels=grade_counts.index, 
    autopct="%1.1f%%", 
    startangle=90,
    colors=['blue','green','orange'] # Add specific colors
)
ax[0].set_title("Grade Distribution (Pie Chart)", fontsize=14, fontweight='bold')
ax[0].axis('equal') # Ensure the pie is drawn as a perfect circle

# === CHART 2: HISTOGRAM (Average Scores) ===
# Plot on the second axis: ax[1]
sns.histplot(
    data=df, 
    x='Average', 
    kde=True, 
    bins=5, 
    ax=ax[1], # Important: specify the right axis (ax[1])
    color='skyblue',
    edgecolor='black'
)
ax[1].set_title('Histogram of Average Scores', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Score', fontsize=12)
ax[1].set_ylabel('Count', fontsize=12)

# Adjust layout automatically to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()