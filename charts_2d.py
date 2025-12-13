import matplotlib.pyplot as plt
from tkinter import messagebox

def plot_histogram(df):
    """
    Plots a Histogram of Average scores using pure Matplotlib.
    """
    if df is None or df.empty:
        messagebox.showwarning("Warning", "No data available to plot Histogram.")
        return

    try:
        plt.figure(figsize=(8, 6))
        
        # Draw Histogram
        counts, bins, patches = plt.hist(df['Average'], bins=10, color='#87CEEB', edgecolor='black', alpha=0.7)
        
        # Add mean line
        mean_val = df['Average'].mean()
        plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=1.5, label=f'Mean: {mean_val:.2f}')
        
        plt.title('Distribution of Student Average Scores', fontsize=14)
        plt.xlabel('Average Score', fontsize=12)
        plt.ylabel('Frequency (Students)', fontsize=12)
        plt.legend()
        plt.grid(axis='y', alpha=0.5)
        
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Could not plot Histogram: {e}")

def plot_pie_chart(df):
    """
    Plots a Pie Chart of Grade distribution using pure Matplotlib.
    """
    if df is None or df.empty:
        messagebox.showwarning("Warning", "No data available to plot Pie Chart.")
        return

    try:
        grade_counts = df['Grade'].value_counts()
        
        # Standardize order
        order = ['A', 'B', 'C', 'D', 'F']
        grade_counts = grade_counts.reindex(order, fill_value=0)
        grade_counts = grade_counts[grade_counts > 0] # Remove zero counts

        if grade_counts.empty:
            messagebox.showwarning("Warning", "No valid grades to plot.")
            return

        plt.figure(figsize=(7, 7))
        
        # Colors similar to Seaborn pastel
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
        explode = [0.05] * len(grade_counts)

        plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', 
                startangle=140, colors=colors[:len(grade_counts)], explode=explode, shadow=True)
        
        plt.title('Student Grade Distribution', fontsize=14)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Could not plot Pie Chart: {e}")
