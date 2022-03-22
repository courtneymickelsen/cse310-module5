class Clients():
    def __init__(self, fname:str, lname:str):
        self.fname = fname
        self.lname = lname
        self.length = 0
        self.type = "Unknown"
        self.last_appt = "00-00-0000"
        self.last_payment = 0.00