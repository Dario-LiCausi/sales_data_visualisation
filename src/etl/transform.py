import datetime
from extract import ETL, Extract

class Transform(ETL):
    def __init__(self):
        super().__init__()
        self.extractor = Extract()

    # split text file data into a dictionary
    def split_lines(self):
        # getting data from file
        extractor = Extract(self.file)
        raw_data = extractor.read_txt()
        if not raw_data:
            return []
        
        # split dataset into lines 
        transactions = raw_data.splitlines()

        # split every single transaction into a list of tokens
        single_transact = []
        for line in transactions:
            if line:
                single_transact.append(line.split(","))

        # create transaction dictionary per line
        sales = []
        for i in single_transact:
            if len(i) >= 10:
                t = {
                    'trans_ID': i[0],
                    'customer_name': i[1],
                    'product': i[2],
                    'category': i[3],
                    'quantity': i[4],
                    'unit_price': i[5],
                    'branch': i[6],
                    'payment_type': i[7],
                    'card_number': i[8],
                    'timestamp': i[9]
                }
                sales.append(t)
        return sales
        
    # remove costumer sensible data like name and card number
    def remove_pii(self):
        sales = self.split_lines()
        for trans in sales:
            trans.pop('customer_name', None)
            trans.pop('card_number', None) 
        return sales

    # normalise time stamp and create splitted data and time keys    
    def split_datetime(self):
        sales = self.remove_pii()

        time_formats = (
            "%Y-%m-%d %H:%M",
            "%y-%m-%d %H:%M",
            "%d-%m-%Y %H:%M",
            "%d-%m-%y %H:%M",
            "%Y-%b-%d %H:%M",
            "%y-%b-%d %H:%M",
            "%d-%b-%Y %H:%M",
            "%d-%b-%y %H:%M",
            "%Y/%m/%d %H:%M",
            "%y/%m/%d %H:%M",
            "%d/%m/%Y %H:%M",
            "%d/%m/%y %H:%M",
            "%Y/%b/%Y %H:%M",
            "%y/%b/%Y %H:%M",
            "%d/%b/%Y %H:%M",
            "%d/%b/%y %H:%M",
        )

        # remove header
        sales = [
            t for t in sales
            if str(t.get("timestamp") or "").strip().lower() != "timestamp"
        ]

        for t in sales:
            timestamp = str(t.get("timestamp") or "").strip()

            parsed = None
            for format in time_formats:
                try:
                    parsed = datetime.datetime.strptime(timestamp, format)
                    break
                except ValueError:
                    pass
            if parsed is None:
                raise ValueError (f"Timestamp not valid: {timestamp!r}")
                
            date = parsed.strftime("%d/%m/%Y")
            time = parsed.strftime("%H:%M")

            t["date"] = date
            t["time"] = time
            t.pop("timestamp")
        # for t in sales:
        #     print(t)
        return sales

# test
# if __name__ == "__main__":
#     transformer = Transform()
#     result = transformer.split_datetime()
