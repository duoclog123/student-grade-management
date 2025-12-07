# File chính chạy chương trình và hiển thị GUI
import tkinter as tk
from tkinter import ttk, messagebox

# ======================================================
# 1. MAIN WINDOW (CỬA SỔ CHÍNH)
# ======================================================
root = tk.Tk()
root.title("Student Grade Management")
root.geometry("900x650") # Tăng chiều cao một chút cho thoải mái


# ======================================================
# 2. INPUT FRAME (KHUNG NHẬP LIỆU)
# ======================================================
input_frame = ttk.LabelFrame(root, text="Add Student")
input_frame.pack(fill="x", padx=10, pady=10)

# Hàm hỗ trợ tạo Label + Entry cho gọn code
def create_entry(label_text, row, column):
    ttk.Label(input_frame, text=label_text).grid(row=row, column=column, padx=5, pady=5, sticky="e")
    entry = ttk.Entry(input_frame)
    entry.grid(row=row, column=column + 1, padx=5, pady=5, sticky="w")
    return entry

# Tạo các ô nhập liệu
entry_name = create_entry("Name:", 0, 0)
entry_math = create_entry("Math:", 0, 2)
entry_physics = create_entry("Physics:", 1, 0)
entry_english = create_entry("English:", 1, 2)


# ======================================================
# 3. CALLBACKS (CÁC HÀM XỬ LÝ - CHỜ TEAM KHÁC GHÉP VÀO)
# ======================================================
def add_student():
    messagebox.showinfo("TODO", "Chức năng add_student() chưa được cài đặt.")

def load_file():
    messagebox.showinfo("TODO", "Chức năng load_file() chưa được cài đặt.")

def save_file():
    messagebox.showinfo("TODO", "Chức năng save_file() chưa được cài đặt.")

def show_histogram():
    messagebox.showinfo("TODO", "Chức năng show_histogram() chưa được cài đặt.")

def show_pie():
    messagebox.showinfo("TODO", "Chức năng show_pie() chưa được cài đặt.")

def show_3d():
    messagebox.showinfo("TODO", "Chức năng show_3d() chưa được cài đặt.")


# ======================================================
# 4. BUTTONS (CÁC NÚT BẤM TÁC VỤ)
# ======================================================
# Tạo một frame con để chứa nút bấm cho căn giữa đẹp hơn (Optional)
btn_frame = ttk.Frame(input_frame)
btn_frame.grid(row=2, column=0, columnspan=4, pady=10)

ttk.Button(btn_frame, text="Add Student", command=add_student).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Load File", command=load_file).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Save File", command=save_file).pack(side="left", padx=5)


# ======================================================
# 5. TABLE (BẢNG HIỂN THỊ CÓ THANH CUỘN)
# ======================================================
table_frame = ttk.LabelFrame(root, text="Student List")
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("name", "math", "physics", "english", "avg", "grade")

# --- Thêm Scrollbar ---
scrollbar = ttk.Scrollbar(table_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# --- Tạo Treeview kết nối Scrollbar ---
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10, yscrollcommand=scrollbar.set)
scrollbar.config(command=tree.yview) # Khi kéo thanh cuộn thì bảng chạy theo

# Định dạng cột
for col in columns:
    tree.heading(col, text=col.capitalize())
    tree.column(col, width=100, anchor="center")

tree.pack(side="left", fill="both", expand=True)


# ======================================================
# 6. STATISTICS PANEL (KHUNG THỐNG KÊ)
# ======================================================
stats_frame = ttk.LabelFrame(root, text="Statistics")
stats_frame.pack(fill="x", padx=10, pady=5)

# Dùng frame con để chia cột thống kê cho đẹp
left_stats = ttk.Frame(stats_frame)
left_stats.pack(side="left", padx=20, pady=5)
right_stats = ttk.Frame(stats_frame)
right_stats.pack(side="right", padx=20, pady=5)

label_avg = ttk.Label(left_stats, text="Class Average: ---", font=("Arial", 10, "bold"))
label_avg.pack(anchor="w")

label_grade_dist = ttk.Label(left_stats, text="Grade Distribution: ---")
label_grade_dist.pack(anchor="w")

label_highest = ttk.Label(right_stats, text="Highest Score: ---", foreground="green")
label_highest.pack(anchor="w")

label_lowest = ttk.Label(right_stats, text="Lowest Score: ---", foreground="red")
label_lowest.pack(anchor="w")


# ======================================================
# 7. VISUALIZATION BUTTONS (NÚT VẼ BIỂU ĐỒ)
# ======================================================
viz_frame = ttk.Frame(root)
viz_frame.pack(fill="x", padx=10, pady=10)

# Căn giữa các nút vẽ biểu đồ
viz_center_frame = ttk.Frame(viz_frame)
viz_center_frame.pack(anchor="center")

ttk.Button(viz_center_frame, text="Show Histogram", command=show_histogram).pack(side="left", padx=10)
ttk.Button(viz_center_frame, text="Show Pie Chart", command=show_pie).pack(side="left", padx=10)
ttk.Button(viz_center_frame, text="Show 3D Scatter", command=show_3d).pack(side="left", padx=10)


# ======================================================
# 8. RUN APP
# ======================================================
if __name__ == "__main__":
    root.mainloop()