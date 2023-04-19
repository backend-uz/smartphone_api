from tinydb import TinyDB, Query

class CartDB:
    def __init__(self) -> None:
        self.db = TinyDB('cartdb.json', indent=4)
        
    def get_all(self, tablename):
        return list(self.db.table(tablename).all())

    def add_card(self, tablename, phone):
        self.table = self.db.table(tablename)
        self.db.table(tablename).insert(phone)

    def remove_cart(self, tablename, idx):
        self.db.table(tablename).remove(doc_ids = [idx])

# db = CartDB()
# data = {"name":"phone"}
# print(db.get_all('testing'))