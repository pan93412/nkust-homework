from advanced import TwoATwoB


class TestTwoATwoB:
    def test_verify(self):
        instance = TwoATwoB()
        assert instance.verify(instance.our_answer) == "1111"

        instance.our_answer = ["red", "yellow", "blue", "yellow"]
        assert instance.verify(["red", "yellow", "blue", "yellow"]) == "1111"
        assert instance.verify(["red", "yellow", "blue", "green"]) == "1113"
        assert instance.verify(["red", "yellow", "green", "blue"]) == "1132"
        assert instance.verify(["red", "green", "blue", "yellow"]) == "1311"
        assert instance.verify(["green", "red", "blue", "yellow"]) == "3211"
        assert instance.verify(["green", "red", "yellow", "blue"]) == "3222"
        assert instance.verify(["green"] * 4) == "3333"
        assert instance.verify(["red"] * 4) == "1222"
        assert instance.verify(["yellow"] * 4) == "2121"

