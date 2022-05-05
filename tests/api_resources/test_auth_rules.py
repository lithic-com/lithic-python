# File generated from our OpenAPI spec by Stainless.
import os
import pytest
from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage

from lithic.types.auth_rule import *
from lithic.types.auth_rule_create_response import *
from lithic.types.auth_rule_retrieve_response import *
from lithic.types.auth_rule_update_response import *
from lithic.types.auth_rule_list_response import *
from lithic.types.auth_rule_apply_response import *
from lithic.types.auth_rule_remove_response import *


base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAuthRules:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.auth_rules.create({})
        assert isinstance(resource, AuthRuleCreateResponse)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.auth_rules.create(
            {
                "allowed_mcc": ["rjjhdroasarbgcntnxs", "jyumqxaforweooehnwtk", "iv"],
                "blocked_mcc": ["ejnjkugfqyawtjniwd", "vahduuhmnl", "iwhxzjlwwpquwiwdyq"],
                "allowed_countries": ["fuutlpvsasabbn", "utgrmylvksdpnql", "rqomalausascyo"],
                "blocked_countries": ["mmdqylufjjtcrroepm", "zva", "dehtyzxzeuzltdogydw"],
                "avs_type": "ZIP_ONLY",
                "card_tokens": ["koroqjiaermegnjoyr", "hrkiozjrj", "ecfy"],
                "account_tokens": ["ycqxalf", "umwglljxhzdpdqy", "vxekfhrstqvmevzwfs"],
                "program_level": True,
            }
        )
        assert isinstance(resource, AuthRuleCreateResponse)

    def test_method_retrieve(self) -> None:
        resource = self.client.auth_rules.retrieve(
            "499f7af9-b8dc-4711-83fc-7c5955c862cb",
        )
        assert isinstance(resource, AuthRuleRetrieveResponse)

    def test_method_update(self) -> None:
        resource = self.client.auth_rules.update("73d41570-764d-4f2e-a7c1-836477d51c77", {})
        assert isinstance(resource, AuthRuleUpdateResponse)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.auth_rules.update(
            "73d41570-764d-4f2e-a7c1-836477d51c77",
            {
                "allowed_mcc": ["wqzcftpnwpyohxs", "aiwrb", "tdzjnrfqprqfryew"],
                "blocked_mcc": ["sqlbnrofgaoovvswdc", "rgsihuz", "hbblngsogtiyoixwtefo"],
                "allowed_countries": ["knvtz", "bnapltinrxqy", "xftignkdhhrjiutgc"],
                "blocked_countries": ["uvpwvplcqzor", "qtjoneuxafnqaylfzfiw", "vdjzgodizevcxunbc"],
                "avs_type": "ZIP_ONLY",
            },
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    def test_method_list(self) -> None:
        resource = self.client.auth_rules.list()
        assert isinstance(resource, AuthRuleListResponse)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.auth_rules.list({"page": 6, "page_size": 53})
        assert isinstance(resource, AuthRuleListResponse)

    def test_method_apply(self) -> None:
        resource = self.client.auth_rules.apply("95cebf0d-f216-4f31-b3aa-7955178f5968", {})
        assert isinstance(resource, AuthRuleApplyResponse)

    def test_method_apply_with_optional_params(self) -> None:
        resource = self.client.auth_rules.apply(
            "95cebf0d-f216-4f31-b3aa-7955178f5968",
            {
                "card_tokens": ["wksona", "wvxfoggjz", "jcsarilxfkztblmo"],
                "account_tokens": ["jhdv", "jlckfqwjzlgtrucy", "akzxeixyjnhjpqa"],
                "program_level": False,
            },
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    def test_method_remove(self) -> None:
        resource = self.client.auth_rules.remove({})
        assert isinstance(resource, AuthRuleRemoveResponse)

    def test_method_remove_with_optional_params(self) -> None:
        resource = self.client.auth_rules.remove(
            {
                "card_tokens": ["fafsyomqtqmkpkpwzyrg", "sahfy", "lktvguwck"],
                "account_tokens": ["nnwpwkoqpwurhzmskvh", "", "rericuvvpqcx"],
                "program_level": True,
            }
        )
        assert isinstance(resource, AuthRuleRemoveResponse)


class TestAsyncAuthRules:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.auth_rules.create({})
        assert isinstance(resource, AuthRuleCreateResponse)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.create(
            {
                "allowed_mcc": ["", "fgxapjxqii", "hjt"],
                "blocked_mcc": ["tpskcznaowt", "xwjdlitz", "poqjxfcewcxcp"],
                "allowed_countries": ["xjrbexyfugwfdzccr", "pykrewmgerdswln", "issxztangmileatnwk"],
                "blocked_countries": ["ejdklebjz", "jijs", "x"],
                "avs_type": "ZIP_ONLY",
                "card_tokens": ["gavaciqv", "lxavevtqtztfjrjlusk", "snpyjlci"],
                "account_tokens": ["fx", "lnzvjqgwjcilqlaw", "jkxlnmglgmviqlmk"],
                "program_level": True,
            }
        )
        assert isinstance(resource, AuthRuleCreateResponse)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.auth_rules.retrieve(
            "82983a8f-9004-4803-86cd-8597a0646aa5",
        )
        assert isinstance(resource, AuthRuleRetrieveResponse)

    async def test_method_update(self) -> None:
        resource = await self.client.auth_rules.update("53b4fff1-5740-4885-adae-4bbb56014d18", {})
        assert isinstance(resource, AuthRuleUpdateResponse)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.update(
            "53b4fff1-5740-4885-adae-4bbb56014d18",
            {
                "allowed_mcc": ["qhrqomaafi", "mlos", "uq"],
                "blocked_mcc": ["ikemukbbyhsjmfapkw", "vwoqskmlmwqju", "w"],
                "allowed_countries": ["vzkjuflbk", "zic", "lrybsylghdan"],
                "blocked_countries": ["rdhirkhixswr", "m", "osw"],
                "avs_type": "ZIP_ONLY",
            },
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    async def test_method_list(self) -> None:
        resource = await self.client.auth_rules.list()
        assert isinstance(resource, AuthRuleListResponse)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.list({"page": 0, "page_size": 749})
        assert isinstance(resource, AuthRuleListResponse)

    async def test_method_apply(self) -> None:
        resource = await self.client.auth_rules.apply("d354b706-3415-4236-a74e-fa0b81746f28", {})
        assert isinstance(resource, AuthRuleApplyResponse)

    async def test_method_apply_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.apply(
            "d354b706-3415-4236-a74e-fa0b81746f28",
            {
                "card_tokens": ["", "zauclcrahxlgwzot", "gwzvwbekew"],
                "account_tokens": ["ncspzbffyyrmko", "hvlfdt", "kbxbqrlbvn"],
                "program_level": False,
            },
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    async def test_method_remove(self) -> None:
        resource = await self.client.auth_rules.remove({})
        assert isinstance(resource, AuthRuleRemoveResponse)

    async def test_method_remove_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.remove(
            {
                "card_tokens": ["qepov", "flldwd", "cpbsohtkuiyyezd"],
                "account_tokens": ["mtwxteoneskbsujebi", "rsdsqehitklk", "cckdnasaoakvynpmzr"],
                "program_level": True,
            }
        )
        assert isinstance(resource, AuthRuleRemoveResponse)
