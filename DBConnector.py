from DBFileConverter import DBFileConverter
from DBClass import DBClass
import numpy as np

class DBConnector:
    def __init__(self):
        self.db = DBClass()
        self.file = DBFileConverter(self.db)

    def create(self, db_name, dim_names):
        self.db.name = db_name
        self.db.dim_names = dim_names

        ndtuple = []

        for i in range(len(dim_names)):
            ndtuple.append(1)

        ndtuple = tuple(ndtuple)
        print(ndtuple)
        array = np.ndarray(ndtuple)
        array.fill(0)
        self.db.db = array.tolist()
        print(vars(self.db))
        self.file.create_file()

    def read(self):
        pass

    def update(self):
        self.file.update_file()

    """setter functions"""

    def overwrite_cell(self, position, value):
        db_copy = self.db.db.copy()
        print(db_copy)
        db_progress = db_copy
        for dim in range(len(position)-1):
            db_progress = db_progress[position[dim]]
            print(db_progress)

        db_progress[0] = value
        self.db.db = db_copy.copy()

    def append(self):
        pass

    """getter functions"""

    def get_cell(self, position):
        pass

    def get_exerpt(self, dim_ranges):
        pass

    def get_db_with_cut_dim(self, dim, position_in_dim):
        pass

if __name__ == "__main__":
    db_con = DBConnector()
    db_con.create("test", ["hi", "hello", "tach"])
