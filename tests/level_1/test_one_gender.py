from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize("программировал", "программировала", "male") == "программировал"
    assert genderalize("тестировал", "тестировала", "female") == "тестировала"
    assert (
        genderalize(verb_female="смотрела", gender="female", verb_male="смотрел")
        == "смотрела"
    )
