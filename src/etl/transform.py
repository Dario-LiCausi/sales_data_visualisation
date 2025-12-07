from .extract import ETL, Extract

class Transform(ETL):
    def __init__(self):
        super().__init__()
        self.extractor = Extract()

    def split_lines(self):
        # getting data from file
        extractor = Extract(self.file)
        raw_data = extractor.read_txt()
        if not raw_data:
            return []
        
        # split dataset into lines \n
        transactions = raw_data.splitlines()

        # split every single transaction into a list of tokens
        single_transact = []
        for line in transactions:
            if line:
                single_transact.append(line.split(" "))

        # create transaction dictionary per line
        sales = []
        for i in single_transact:
            if len(i) >= 8:
                t = {
                    'customer_name': i[0],
                    'product': i[1],
                    'category': i[2],
                    'quantity': i[3],
                    'unit_price': i[4],
                    'branch': i[5],
                    'payment_type': i[6],
                    'card_number': i[7],
                    'timestamp': i[8]
                }
                sales.append(t)
        return sales

    def remove_pii(self):
        sales = self.split_lines()
        for trans in sales:
            trans.pop('customer_name', None)
            trans.pop('t_ID', None) 
        for trans in sales:
            print(trans)
        return sales


# test
if __name__ == "__main__":
    transformer = Transform()
    result = transformer.remove_pii()