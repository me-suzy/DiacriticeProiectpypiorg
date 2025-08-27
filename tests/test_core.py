from diacritice_rom import add_diacritics

def test_basic():
    text = "Romania este o tara frumoasa"
    result = add_diacritics(text)
    assert result == "România este o țară frumoasă"
