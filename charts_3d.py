# Module xu ly bieu do 3D (Scatter Plot)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_scatter(df):
    """
    Plot 3D Scatter chart comparing Math - Physics - English scores.
    Input: df containing columns ['Student', 'Math', 'Physics', 'English']
    """

    # 1. Validate Input Data [cite: 24]
    required_cols = {'Student', 'Math', 'Physics', 'English'}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"DataFrame must contain columns: {required_cols}")

    # 2. Setup 3D Plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # 3. Get Data
    x, y, z = df['Math'], df['Physics'], df['English']

    # 4. Draw Scatter [cite: 23, 41]
    ax.scatter(x, y, z, s=60, c='red', marker='o')

    # 5. Set Labels & Title
    ax.set_xlabel('Math Score')
    ax.set_ylabel('Physics Score')
    ax.set_zlabel('English Score')
    ax.set_title('3D Student Performance Analysis')

    # 6. Annotate Student Names
    for x_val, y_val, z_val, name in zip(x, y, z, df['Student']):
        ax.text(x_val, y_val, z_val, name, fontsize=9)

    plt.tight_layout()
    plt.show()

# --- TEST BLOCK ---
if __name__ == "__main__":
    import pandas as pd
    df_test = pd.DataFrame({
        'Student': ["Alice", "Bob", "Carol", "David", "Emma"],
        'Math': [85, 70, 95, 60, 88],
        'Physics': [78, 65, 88, 72, 91],
        'English': [92, 75, 90, 68, 84]
    })

    print("Testing 3D Chart...")
    plot_3d_scatter(df_test)