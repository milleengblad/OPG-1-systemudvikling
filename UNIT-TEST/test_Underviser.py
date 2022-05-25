
from Klasser.Teacher import Underviser

def test_get_age():
    und=Underviser('Lektor', 'Jakob', 'Nielsen', '190590-9999',
'Mand', 'Borgmestervangen_1', '11111111', 'jakob.nielsen@gmail.com')
    assert und.get_age() == 32

