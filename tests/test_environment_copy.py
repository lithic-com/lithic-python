from typing_extensions import Literal

import httpx
import pytest

from lithic import Lithic, AsyncLithic

Environment = Literal["production", "sandbox"]


@pytest.mark.parametrize("initial,target", [("production", "sandbox"), ("sandbox", "production")])
@pytest.mark.parametrize("method", ["copy", "with_options"])
def test_sync_environment_override(
    initial: Environment, target: Environment, method: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("LITHIC_BASE_URL", raising=False)
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"data": []})

    with Lithic(
        api_key="test-key", environment=initial, http_client=httpx.Client(transport=httpx.MockTransport(respond))
    ) as client:
        original_url = client.base_url
        switched = client.copy(environment=target) if method == "copy" else client.with_options(environment=target)
        switched.cards.list()
        assert client.base_url == original_url

    expected_host = "api.lithic.com" if target == "production" else "sandbox.lithic.com"
    assert requests[0].url.host == expected_host


@pytest.mark.parametrize("initial,target", [("production", "sandbox"), ("sandbox", "production")])
@pytest.mark.parametrize("method", ["copy", "with_options"])
async def test_async_environment_override(
    initial: Environment, target: Environment, method: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("LITHIC_BASE_URL", raising=False)
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"data": []})

    async with AsyncLithic(
        api_key="test-key", environment=initial, http_client=httpx.AsyncClient(transport=httpx.MockTransport(respond))
    ) as client:
        original_url = client.base_url
        switched = client.copy(environment=target) if method == "copy" else client.with_options(environment=target)
        await switched.cards.list()
        assert client.base_url == original_url

    expected_host = "api.lithic.com" if target == "production" else "sandbox.lithic.com"
    assert requests[0].url.host == expected_host


@pytest.mark.parametrize("override", [False, True])
def test_sync_custom_url_is_preserved(override: bool) -> None:
    with Lithic(api_key="test-key", base_url="https://original.example/v1") as client:
        copied = (
            client.copy(environment="sandbox", base_url="https://override.example/v1") if override else client.copy()
        )
        assert copied.base_url.host == ("override.example" if override else "original.example")


@pytest.mark.parametrize("override", [False, True])
async def test_async_custom_url_is_preserved(override: bool) -> None:
    async with AsyncLithic(api_key="test-key", base_url="https://original.example/v1") as client:
        copied = (
            client.copy(environment="sandbox", base_url="https://override.example/v1") if override else client.copy()
        )
        assert copied.base_url.host == ("override.example" if override else "original.example")
