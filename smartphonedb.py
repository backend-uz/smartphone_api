from tinydb import TinyDB, Query

class SmartphoneDB:
    def __init__(self) -> None:
        self.db = TinyDB('db.json', indent=4, separators=(',', ':'))

    def brands(self):
        return list(self.db.tables())
    
    def add(self, brand, phone):
        self.db.table(brand).insert(phone)
    
    def getPhone(self,brand,idx):
        table = self.db.table(brand)
        return table.get(doc_id=idx)
    
    def get_phone_list(self,brand):
        table = self.db.table(brand)
        return table.all()
    
    def delete_smartphone(self):
        pass