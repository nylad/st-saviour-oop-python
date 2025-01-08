from song import Song

def test_songs():
    humble = Song('HUMBLE', 'Kendrick Lamar')
    assert humble.play() == 'HUMBLE by Kendrick Lamar plays'

    jolene = Song('Jolene', 'Dolly Parton')
    assert jolene.play() == 'Jolene by Dolly Parton plays'

def test_country():
    pass

def test_rap():
    pass
    