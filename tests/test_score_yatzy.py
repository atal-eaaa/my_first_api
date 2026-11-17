from yatzy import score_yatzy

def test_yatzy():
    scores = score_yatzy([4, 4, 4, 4, 4])
    assert scores["yatzy"] == 50


def test_full_house():
    scores = score_yatzy([2, 2, 3, 3, 3])
    assert scores["full_house"] == 13


