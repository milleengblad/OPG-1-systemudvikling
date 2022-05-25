class Secretary:
    """KLasse med information om Underviseren"""
    def __init__(self, titel, firstname, surname, cpr_number, address, phone_nr, mail, IDnr, university):
        self.titel = titel
        self.firstname = firstname
        self.surname = surname
        self.cpr_number = cpr_number
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

    def get_cpr_number(self): return self.cpr_number
    def set_cpr_number(self, new_cpr_number): self.cpr_number = new_cpr_number

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


