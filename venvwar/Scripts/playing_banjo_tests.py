from playing_banjo import are_you_playing_banjo


def test_cases():
    assert are_you_playing_banjo("martin"), "martin does not playing banjo"
    assert are_you_playing_banjo("Rikke"), "Rikke plays banjo"
    assert are_you_playing_banjo("bravo"), "bravo does not playing banjo"
    assert are_you_playing_banjo("rolf"), "rolf plays banjo"
