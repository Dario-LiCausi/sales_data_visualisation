from extract import ETL
from transform import Transform


class Load(ETL):
    def __init__(self):
        super().__init__()
        self.transformer = Transform()
        

    def test_print(self):
        transformer = Transform()
        sales = transformer.split_datetime()
        for t in sales:
            print(t)

#test
if __name__ == "__main__":
    loader = Load()
    result = loader.test_print()