import csv
from pathlib import Path
from etl.extract import ETL
from etl.transform import Transform
from db.config.connector import LoadDB as connector

class Load(ETL):
    def __init__(self):
        super().__init__()
        self.clean_data = Transform()
        
    # automatically define dict keys to pass to new csv file    
    def extract_keys(self):
        if not self.clean_data:
            return []
        return list(self.clean_data[0].keys())

    # write a new csv file
    def write_csv(self):
        csv_file_path = self.data_dir / "clean_data.csv"
        csv_file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.clean_data:
            print("No data to write.")
            return
        fieldnames = self.extract_keys()
        try:
            with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.clean_data)
            print("Hooray! File generated!")
        except OSError as e:
            print(f"Failed to write CSV: {e}")

class LoadDB(Load):
    SCHEMA_PATH = Path(__file__).resolve().parents[1] / "db" / "setup" / "create_db.sql"

    def ensure_schema(self, cursor):
        # creates table
        if self.SCHEMA_PATH.exists():
            schema_sql = self.SCHEMA_PATH.read_text()
            for query in [s.strip() for s in schema_sql.split(";") if s.strip()]:
                cursor.execute(query)

    def rows(self):
        # create rows
        return [
            (
                row["product"],
                row["category"],
                row["quantity"],
                row["unit_price"],
                row["branch"],
                row["payment_type"],
                row["date"],
                row["time"],
            )
            for row in self.clean_data
        ]

    def load_to_db(self):
        if not self.clean_data:
            print("No data to load.")
            return

        conn = connector.login_db()
        if conn is None:
            return

        cur = conn.cursor()
        try:
            self.ensure_schema(cur)
            cur.executemany(
                "INSERT INTO sales (product, category, quantity, unit_price, branch, payment_type, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                self.rows(),
            )
            conn.commit()
            print("Data inserted into sales table.")
        finally:
            cur.close()
            conn.close()

    def run_db(self):
        self.clean_data = Transform().split_datetime()
        if not self.clean_data:
            print ("[Error] No data to load")
            return
        self.load_to_db()
