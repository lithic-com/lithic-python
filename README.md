# Lithic Python API Library

The Lithic Python library provides convenient access to the Lithic REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Installation

```sh
pip install lithic
```

## Usage

```python
from lithic import Lithic

client = Lithic(
    api_key="my api key", # defaults to os.environ.get("LITHIC_API_KEY")
    environment="sandbox" # defaults to "production"
)

card = client.cards.create({
    "type": "SINGLE_USE"
})

print(card.token)
```

While you can provide an `api_key` keyword argument, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
and adding `LITHIC_API_KEY="my api key"` to your `.env` file so that your API keys are not stored in source control.

## Async Usage

Simply import `AsyncLithic` instead of `Lithic` and use `await` with each API call:

```python
from lithic import AsyncLithic
import asyncio # or the async environment of your choice

client = AsyncLithic(
    api_key="my api key", # defaults to os.environ.get("LITHIC_API_KEY")
    environment="sandbox" # defaults to "production"
)

async def main():
    card = await client.cards.create({
        "type": "SINGLE_USE"
    })

    print(card.token)

asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients are otherwise identical.

## Using Types

Request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), while responses are [Pydantic](https://pydantic-docs.helpmanual.io/) models. This helps provide autocomplete and documentation within your editor.

If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Lithic API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import lithic
from typing import List

client = lithic.Lithic()

all_cards = []
# Iterate through items across all pages, issuing requests as needed.
for card in client.cards.list():
    all_cards.append(card)
```

Or, asynchronously:

```python
import lithic
from typing import List

client = lithic.AsyncLithic()

async def get_all_cards() -> List[lithic.types.Card]:
    cards = []
    # Iterate through items across all pages, issuing requests as needed.
    async for card in client.cards.list():
        cards.append(card)
    return cards
```

Alternatively, you can use the `.has_next_page()`, `.next_page_params()`,
or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await client.cards.list({"page_size": 2})
if first_page.has_next_page():
    print("will fetch next page, with params", first_page.next_page_params())
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await client.cards.list()

print(f"page number: {first_page.page}") # => "page number: 1"
for card in first_page.data:
    print(card.token)

# Remove `await` for non-async usage.
```

## Handling errors

When the library is unable to connect to the API (e.g., due to network connection problems or a timeout), a subclass of `lithic.APIConnectionError` is raised.

When the API returns a non-success status code (i.e., 4xx or 5xx
response), a subclass of `lithic.APIStatusError` will be raised, containing `status_code` and `response` properties.

All errors inherit from `lithic.APIError`.

```python
import lithic

client = lithic.Lithic()

try:
    client.cards.create()

except lithic.APIConnectionError as e:
    print('The server could not be reached')
    print(e.__cause__) # an underlying Exception, likely raised within httpx.

except lithic.RateLimitError as e:
    print('A 429 status code was received; we should back off a bit.')

except lithic.APIStatusError as e:
    print('Another non-200-range status code was received')
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 409 Conflict, 429 Rate Limit,
and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from lithic import Lithic

# Configure the default for all requests:
client = Lithic(max_retries=0)

# Override per-request:
client.cards.list({"page_size": 10}, max_retries=5)
```

### Timeouts

Requests time out after 60 seconds by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
# Configure the default for all requests:
client = Lithic(
  timeout=20.0 # default is 60s.
)

# More granular control:
client = Lithic(
  timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0)
)

# Override per-request:
client.cards.list({"page_size": 10}, timeout=5.0)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Advanced: Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
import lithic

client = lithic.Lithic(
    base_url="http://my.test.server.example.com:8083", # Use a custom base URL
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0")
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

## Status

This package is in beta. Its internals and interfaces are not stable and subject to change without a major semver bump;
please reach out if you rely on any undocumented behavior.

We are keen for your feedback; please email us at [sdk-feedback@lithic.com](mailto:sdk-feedback@lithic.com) or open an issue with questions,
bugs, or suggestions.

## Requirements

Python 3.7 or higher.
