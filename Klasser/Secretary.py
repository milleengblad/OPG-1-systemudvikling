from stdnum.dk import cpr

class Secretary:
    """Class for secretary"""
    def __init__(self, titel, firstname, surname, cpr:cpr, address, phone_nr, mail, IDnr, university):
        self.titel = titel
        self.firstname = firstname
        self.surname = surname
        self.cpr = cpr
        self.address = address
        self.phone_nr = phone_nr
        self.mail = mail
        self.IDnr = IDnr
        self.university = university

        # getters og setters
    def get_titel(self): return self.titel
    def set_titel(self, new_titel): self.titel = new_titel

    def get_firstname(self): return self.firstname
    def set_firstname(self, new_firstname): self.firstname = new_firstname

    def get_surname(self): return self.surname
    def set_surname(self, new_surname): self.surname = new_surname

    def get_cpr(self): return self.cpr
    def set_cpr(self, new_cpr): self.cpr = new_cpr

    def get_address(self): return self.address
    def set_address(self, new_address): self.address = new_address

    def get_phone_nr(self): return self.phone_nr
    def set_phone_nr(self, new_phone_nr): self.phone_nr = new_phone_nr

    def get_mail(self): return self.mail
    def set_mail(self, new_mail): self.mail = new_mail

    def get_IDnr(self): return self.IDnr
    def set_IDnr(self, new_IDnr): self.IDnr = new_IDnr

    def get_university(self): return self.university
    def set_university(self, new_university): self.university = new_university


