from match_factory import MatchFactory

match_test = MatchFactory.createMatch(match_id=0, match_name="Partida 0", number_of_player_to_start=2)

def test_get_match_id():
    assert match_test.get_id() == 0

def test_get_match_name():
    assert match_test.get_name() == "Partida 0"

def test_number_of_players():
    assert match_test.get_number_of_players() == 0