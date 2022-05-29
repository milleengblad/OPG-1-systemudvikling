
from Klasser.Teacher import Teacher

def test_get_age():
    und=Teacher('Lector', 'Jakob', 'Nielsen', '190590-9999', 'Borgmestervangen_1', '11111111', 'jakob.nielsen@gmail.com', '1', 'Systemdevelopment')
    assert und.get_age() == 32

