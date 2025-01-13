from song import Song
from rap import Rap
from country import Country

def test_songs():
    humble = Rap('HUMBLE', 'Kendrick Lamar', [])
    assert humble.play() == 'HUMBLE by Kendrick Lamar plays with special guests: []'

    jolene = Country('Jolene', 'Dolly Parton', 60)
    assert jolene.play() == 'Jolene by Dolly Parton plays at speed: 60'

    assert isinstance(humble, Rap)
    assert isinstance(humble, Song)

    assert isinstance(jolene, Country)
    assert isinstance(jolene, Song)
    