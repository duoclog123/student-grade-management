# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 17:28:04 2025

@author: PC
"""

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt

# --- IMPORT MEMBER MODULES ---
from data_manager import DataManager  # Member 2: Data Logic
import charts_3d                    # Member 4: 3D Charts
# Note: Member 3's logic is integrated directly or imported if available

# ======================================================
# 1. INITIALIZE BACKEND (THE BRAIN)
# ======================================================
manager = DataManager()  # Initialize the logic engine

# ======================================================
# 2. MAIN WINDOW SETUP (GUI)
# ======================================================
root = tk.Tk()
root.title("Student Grade Management System (Elite Edition)")
root.geometry("1050x720")

# Apply a style for better look
style = ttk.Style()
style.theme_use('clam') # Options: 'clam', 'alt', 'default', 'classic'

# ======================================================
# 3. HELPER FUNCTIONS & LOGIC
# ======================================================

def refresh_table():
    """Clear the table and reload data from the DataFrame"""
    # Clear existing rows
    for item in tree.get_children():
        tree.delete(item)
    
    # Insert new data
    if manager.df is not None:
        for _, row in manager.df.iterrows():
            tree.insert("", tk.END, values=list(row))
        update_stats() # Auto-update statistics

def update_stats():
    """Update the statistics dashboard at the bottom"""
    if manager.df is not None and not manager.df.empty:
        stats = manager.get_stats()
        avg_score = manager.df['Average'].mean()
        
        # Update Labels
        label_avg.config(text=f"Class Average: {avg_score:.2f}")
        label_highest.config(text=f"Highest Math: {stats['Math']['Max']}")
        label_lowest.config(text=f"Lowest English: {stats['English']['Min']}")
        
        # Grade Distribution
        dist = manager.df['Grade'].value_counts().to_dict()
        label_grade_dist.config(text=f"Grade Dist: {dist}")
    else:
        # Reset labels if no data
        label_avg.config(text="Class Average: ---")
        label_highest.config(text="Highest Math: ---")
        label_lowest.config(text="Lowest English: ---")

def add_student():
    """Get input -> Validate -> Add to Data -> Refresh UI"""
    try:
        # 1. Get input
        name = entry_name.get().strip()
        math_val = entry_math.get()
        phy_val = entry_physics.get()
        eng_val = entry_english.get()

        # 2. Validation
        if not name:
            messagebox.showwarning("Input Error", "Student Name cannot be empty!")
            return
        
        # Convert to float and validate range
        math = float(math_val)
        phy = float(phy_val)
        eng = float(eng_val)

        if not (0 <= math <= 100 and 0 <= phy <= 100 and 0 <= eng <= 100):
            messagebox.showerror("Input Error", "Scores must be between 0 and 100.")
            return

        # 3. Add to DataFrame
        new_row = pd.DataFrame({'Student': [name], 'Math': [math], 'Physics': [phy], 'English': [eng]})
        
        if manager.df is None:
            manager.df = new_row
        else:
            manager.df = pd.concat([manager.df, new_row], ignore_index=True)
            
        # 4. Recalculate Logic (Member 2's function)
        manager.process_data()
        
        # 5. Refresh UI
        refresh_table()
        messagebox.showinfo("Success", f"Student '{name}' added successfully!")
        
        # Clear inputs
        entry_name.delete(0, tk.END)
        entry_math.delete(0, tk.END)
        entry_physics.delete(0, tk.END)
        entry_english.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Input Error", "Math, Physics, and English must be valid numbers!")

def load_file():
    """Trigger Backend to load CSV"""
    manager.load_data()     # Load
    manager.process_data()  # Calculate
    refresh_table()         # Display
    messagebox.showinfo("System", "Data loaded successfully from CSV file!")

def save_file():
    """Trigger Backend to save CSV"""
    manager.save_data()
    messagebox.showinfo("System", "Data saved to CSV successfully!")

# --- CHART FUNCTIONS ---
def check_data_ready():
    if manager.df is None or manager.df.empty:
        messagebox.showwarning("Warning", "No data to visualize! Please Load Data first.")
        return False
    return True

def show_histogram():
    if not check_data_ready(): return
    plt.figure(figsize=(8, 5))
    # Member 3 Logic (2D)
    plt.hist(manager.df['Average'], bins=5, color='#3498db', edgecolor='black', alpha=0.7)
    plt.title('Distribution of Average Scores')
    plt.xlabel('Average Score')
    plt.ylabel('Number of Students')
    plt.grid(axis='y', alpha=0.5)
    plt.show()

def show_pie():
    if not check_data_ready(): return
    # Member 3 Logic (2D)
    grade_counts = manager.df['Grade'].value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=140, 
            colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'], shadow=True)
    plt.title('Class Grade Distribution')
    plt.show()

def show_3d():
    if not check_data_ready(): return
    try:
        # Member 4 Logic (3D)
        charts_3d.plot_3d_scatter(manager.df)
    except Exception as e:
        messagebox.showerror("Error", f"Could not plot 3D chart: {e}")

# ======================================================
# 4. GUI LAYOUT & WIDGETS
# ======================================================

# --- SECTION A: INPUT ---
input_frame = ttk.LabelFrame(root, text=" 📝 Student Data Entry ")
input_frame.pack(fill="x", padx=15, pady=10)

def create_entry_field(parent, label_text, r, c):
    ttk.Label(parent, text=label_text, font=("Arial", 10)).grid(row=r, column=c, padx=10, pady=10, sticky="e")
    entry = ttk.Entry(parent, width=20)
    entry.grid(row=r, column=c+1, padx=10, pady=10, sticky="w")
    return entry

entry_name = create_entry_field(input_frame, "Full Name:", 0, 0)
entry_math = create_entry_field(input_frame, "Math Score:", 0, 2)
entry_physics = create_entry_field(input_frame, "Physics Score:", 1, 0)
entry_english = create_entry_field(input_frame, "English Score:", 1, 2)

# Action Buttons Frame
action_frame = ttk.Frame(input_frame)
action_frame.grid(row=2, column=0, columnspan=4, pady=10)

ttk.Button(action_frame, text="📂 Load CSV", command=load_file).pack(side="left", padx=10)
ttk.Button(action_frame, text="➕ Add Student", command=add_student).pack(side="left", padx=10)
ttk.Button(action_frame, text="💾 Save to CSV", command=save_file).pack(side="left", padx=10)


# --- SECTION B: DATA TABLE ---
table_frame = ttk.LabelFrame(root, text=" 📋 Class Record ")
table_frame.pack(fill="both", expand=True, padx=15, pady=5)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

cols = ("Student", "Math", "Physics", "English", "Average", "Grade")
tree = ttk.Treeview(table_frame, columns=cols, show="headings", height=8, yscrollcommand=scrollbar.set)
scrollbar.config(command=tree.yview)

# Configure Columns
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")

tree.pack(side="left", fill="both", expand=True)


# --- SECTION C: DASHBOARD & VISUALIZATION ---
bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill="x", padx=15, pady=15)

# Left: Statistics
stats_frame = ttk.LabelFrame(bottom_frame, text=" 📊 Statistics Dashboard ")
stats_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

label_avg = ttk.Label(stats_frame, text="Class Average: ---", font=("Segoe UI", 11, "bold"), foreground="#2980b9")
label_avg.pack(anchor="w", padx=15, pady=2)

label_highest = ttk.Label(stats_frame, text="Highest Math: ---", foreground="#27ae60")
label_highest.pack(anchor="w", padx=15, pady=2)

label_lowest = ttk.Label(stats_frame, text="Lowest English: ---", foreground="#c0392b")
label_lowest.pack(anchor="w", padx=15, pady=2)

label_grade_dist = ttk.Label(stats_frame, text="Grade Dist: ---", font=("Segoe UI", 9, "italic"))
label_grade_dist.pack(anchor="w", padx=15, pady=5)

# Right: Visualization Buttons
viz_frame = ttk.LabelFrame(bottom_frame, text=" 📈 Data Visualization ")
viz_frame.pack(side="right", fill="both", expand=True)

btn_p1 = ttk.Button(viz_frame, text="Show Histogram (2D)", command=show_histogram)
btn_p1.pack(fill="x", padx=20, pady=5)

btn_p2 = ttk.Button(viz_frame, text="Show Pie Chart (2D)", command=show_pie)
btn_p2.pack(fill="x", padx=20, pady=5)

btn_p3 = ttk.Button(viz_frame, text="Show 3D Scatter Plot", command=show_3d)
btn_p3.pack(fill="x", padx=20, pady=5)

# ======================================================
# 5. RUN APPLICATION
# ======================================================
if __name__ == "__main__":
    root.mainloop()