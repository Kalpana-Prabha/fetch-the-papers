def test_is_non_academic():
    assert is_non_academic("Pfizer Inc") == True
    assert is_non_academic("University of Oxford") == False
