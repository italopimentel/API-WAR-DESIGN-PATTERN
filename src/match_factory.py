from match import Match
class MatchFactory:

    @staticmethod
    def createMatch(match_id, match_name, number_of_player_to_start):
        return Match(match_id=match_id, number_of_players_to_start=number_of_player_to_start, match_name=match_name)