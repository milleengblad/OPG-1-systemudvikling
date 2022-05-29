# vi bruger datetime pa UNI-test
from datetime import date
from stdnum.dk import cpr


class Teacher:
    """Class for the teacher"""
    def __init__(self, titel, firstname, surname, cpr:cpr, address, phone_nr, mail, IDnr, course):
        self.titel = titel
        self.firstname = firstname
        self.surname = surname
        self.cpr = cpr
        self.address = address
        self.phone_nr = phone_nr
        self.mail = mail
        self.IDnr = IDnr
        self.course = course

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

    def get_course(self): return self.course
    def set_course(self, new_course): self.course = new_course

#vi bruger get_age pga. UNITtest
    def get_age(self):
        """metode at returnere data fra i dags dato og med cpr.nr"""
        cpr_compact = cpr.compact(self.cpr)
        date_today = date.today()
        birth_date = cpr.get_birth_date(cpr_compact)
        age_date = date_today - birth_date
        return int(age_date.days / 365.2425)
