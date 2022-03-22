class Clients():
    def __init__(self, fname:str, lname:str):
        self.fname = fname
        self.lname = lname
        self.length = 0
        self.type = ""
        self.last_appt = ""
        self.last_payment = 0.00

    def set_length(self, length):
        self.length = length
        # update length in database

    def set_type(self, type):
        self.type = type
        # update type in database

    def set_last_appt(self, last_appt):
        self.last_appt = last_appt
        # update last_appt in database

    def set_last_payment(self, last_payment):
        self.last_payment = last_payment
        # update last_payment in database

    def view_all_info(self):
        c.execute("SELECT * WHERE (fname=:fname AND lname = lname)", {'fname': self.fname, 'lname': self.lname})