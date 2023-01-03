from unittest.mock import Mock, call
from advanced import DictApproach, ListApproach, ApproachDistributor
import pytest


class TestDictApproach:
    fake_input: Mock

    @pytest.fixture(autouse=True)
    def fixture(self):
        self.fake_input = Mock(side_effect=[
            "金 4",
            "銀 5",
            "銅 9",
            "優 7"
        ])
        yield

    def test_input(self):
        dict_approach = DictApproach()
        dict_approach.input(self.fake_input)

        assert self.fake_input.call_args_list == [call(""), call(""), call(""), call("")]
        assert dict_approach.award_table == {
            "金": 4,
            "銀": 5,
            "銅": 9,
            "優": 7
        }

    def test_str(self):
        dict_approach = DictApproach()
        dict_approach.input(self.fake_input)

        assert str(dict_approach) == (
            "金牌得到 4 面\n"
            "銀牌得到 5 面\n"
            "銅牌得到 9 面\n"
            "優牌得到 7 面"
        )

class TestListApproach:
    fake_input: Mock

    @pytest.fixture(autouse=True)
    def fixture(self):
        self.fake_input = Mock(side_effect=[
            "金 4",
            "銀 5",
            "銅 9",
            "優 7"
        ])
        yield

    def test_input(self):
        list_approach = ListApproach()
        list_approach.input(self.fake_input)

        assert self.fake_input.call_args_list == [call(""), call(""), call(""), call("")]
        assert list_approach.award_amount == [4, 5, 9, 7]

    def test_str(self):
        list_apporach = ListApproach()
        list_apporach.input(self.fake_input)

        assert str(list_apporach) == (
            "金牌得到 4 面\n"
            "銀牌得到 5 面\n"
            "銅牌得到 9 面\n"
            "優牌得到 7 面"
        )

class TestApproachDistributor:
    def test_register(self):
        distributor = ApproachDistributor()
        distributor.register("1", DictApproach)
        distributor.register("2", ListApproach)

        assert distributor.approach_map == {
            "1": DictApproach,
            "2": ListApproach
        }

    def test_call(self):
        distributor = ApproachDistributor()
        distributor.register("1", DictApproach)
        distributor.register("2", ListApproach)

        assert distributor("1") == DictApproach
        assert distributor("2") == ListApproach

    def test_call_outside(self):
        distributor = ApproachDistributor()
        approach_name = "1"

        with pytest.raises(ValueError, match = "找不到做法"):
            distributor(approach_name)
