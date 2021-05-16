from Testing.greeting.lib.greeting import Making_Recommendations
import pytest
from lib.greeting import PersonalityGrouper
from lib.greeting import AnimaltoJob
from lib.greeting import RankingApplications, Making_Recommendations


class Test_Recomendations:

    def Recomendations(self):
        result = Making_Recommendations(
            {'Django', 'Python', 'Java'}, 'Dublin', 'owl',)
        expected = ""
        assert result == expected
