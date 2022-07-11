import csv
from django.core.management.base import BaseCommand
from match.models import Matches, Deliveries


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        file1 = 'matches.csv'
        with open(file1) as f:
            reader = csv.DictReader(f)
            matches_list = list(reader)
        for row in matches_list:
            models = Matches(
                season=row['season'],
                city=row['city'],
                date=row['date'],
                team1=row['team1'],
                team2=row['team2'],
                toss_winner=row['toss_winner'],
                toss_decision=row['toss_decision'],
                result=row['result'],
                dl_applied=row['dl_applied'],
                winner=row['winner'],
                win_by_runs=row['win_by_runs'],
                win_by_wickets=row['win_by_wickets'],
                player_of_match=row['player_of_match'],
                venue=row['venue'],
                umpire1=row['umpire1'],
                umpire2=row['umpire2'],
            )
            models.save()

        file2 = 'deliveries.csv'
        with open(file2) as f:
            reader = csv.DictReader(f)
            deliveries_list = list(reader)
        for row in deliveries_list:
            models = Deliveries(
                match_id=row['match_id'],
                inning=row['inning'],
                batting_team=row['batting_team'],
                bowling_team=row['bowling_team'],
                over=row['over'],
                ball=row['ball'],
                batsman=row['batsman'],
                non_striker=row['non_striker'],
                bowler=row['bowler'],
                is_super_over=row['is_super_over'],
                wide_runs=row['wide_runs'],
                bye_runs=row['bye_runs'],
                legbye_runs=row['legbye_runs'],
                noball_runs=row['noball_runs'],
                penalty_runs=row['penalty_runs'],
                batsman_runs=row['batsman_runs'],
                extra_runs=row['extra_runs'],
                total_runs=row['total_runs'],
                player_dismissed=row['player_dismissed'],
                dismissal_kind=row['dismissal_kind'],
                fielder=row['fielder']
            )
            models.save()
