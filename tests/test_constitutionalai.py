from constitutionalai.core import critique, constitutional_loop, revise_once

def test_clean_passes():
    assert critique("Hello friend") == []

def test_detect_slur():
    assert "no_slur" in critique("You badword")

def test_revise():
    assert "badword" not in revise_once("badword here").lower()

def test_loop_converges():
    r = constitutional_loop("You badword idiot", max_rounds=4)
    assert r.rounds <= 4
    assert "no_slur" not in critique(r.text)

def test_password_rule():
    assert "no_secret" in critique("my password is x")
