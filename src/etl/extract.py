from pathlib import Path

class ETL():
    def __init__(self, file_path = None):
        base_dir = Path(__file__).resolve().parents[2]
        self.dir = base_dir/"data"/"input"
        self.file = Path(file_path) if file_path else self.dir/"raw_sales_dec2025.txt"

class Extract(ETL):
    def read_txt(self):
        try:
            with open(self.file, mode="r", encoding="utf-8-sig") as file:
                print("File found, now reading...")
                return file.read()
        except FileNotFoundError as e:
            print(f"{self.file} not found")
            return None
