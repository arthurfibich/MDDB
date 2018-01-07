from DBClass import DBClass


class DBFileConverter:
    def __init__(self, db_class: DBClass):
        self.file = None
        self.db = db_class

    def get_from_file(self):
        pass

    def update_file(self):
        self.create_file()
        self.file.write(str(self.db.db))

    def create_file(self):
        fname = "".join((self.db.name, ".mddb"))
        self.file = open(fname, 'w+')
        print('success')
