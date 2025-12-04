import pandas as pd
import os

class DataManager:
    REQUIRED_COLUMNS = ['Student', 'Math', 'Physics', 'English']

    def __init__(self, filename='students.csv'):
        self.filename = filename
        self.df = None

    # --- 1. LOAD OR CREATE CSV ---
    def load_data(self):
        """Load CSV; auto-create sample data if the file doesn't exist or is invalid."""
        if os.path.exists(self.filename):
            self.df = pd.read_csv(self.filename)

            # Validate columns
            if not set(self.REQUIRED_COLUMNS).issubset(self.df.columns):
                print("⚠️ CSV file is missing required columns. Rebuilding sample data...")
                self._create_sample_data()
        else:
            print("⚠️ File not found. Creating sample data...")
            self._create_sample_data()

        print(f"✅ Loaded data from {self.filename}")
        return self.df

    def _create_sample_data(self):
        """Create default sample dataset"""
        data = {
            'Student': ['Alice', 'Bob', 'Carol', 'David', 'Emma'],
            'Math': [85, 70, 95, 60, 88],
            'Physics': [78, 65, 88, 72, 91],
            'English': [92, 75, 90, 68, 84]
        }
        self.df = pd.DataFrame(data)
        self.save_data()

    def save_data(self):
        """Save DataFrame back to CSV"""
        if self.df is None:
            print("❌ No data to save.")
            return
        self.df.to_csv(self.filename, index=False)
        print(f"💾 Data saved to {self.filename}")

    # --- 2. CALCULATE AVG + GRADE ---
    def process_data(self):
        """Compute average score and classify grade"""
        if self.df is None:
            raise ValueError("Data not loaded.")

        subjects = ['Math', 'Physics', 'English']
        self.df['Average'] = self.df[subjects].mean(axis=1).round(2)

        self.df['Grade'] = self.df['Average'].apply(self._classify_grade)
        return self.df

    @staticmethod
    def _classify_grade(score):
        """Return grade based on score"""
        if score >= 90: return 'A'
        if score >= 80: return 'B'
        if score >= 70: return 'C'
        if score >= 50: return 'D'
        return 'F'

    # --- 3. STATS ---
    def get_stats(self):
        """Return min/max of each subject"""
        if self.df is None:
            raise ValueError("Data not loaded.")

        return {
            col: {'Max': self.df[col].max(), 'Min': self.df[col].min()}
            for col in ['Math', 'Physics', 'English']
        }


# --- TEST RUN ---
if __name__ == "__main__":
    manager = DataManager()

    print("--- LOAD DATA ---")
    manager.load_data()

    print("\n--- PROCESS DATA ---")
    processed = manager.process_data()
    print(processed)

    manager.save_data()
