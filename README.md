# Lithic Python API Library

> **Migration Guide**
>
> We've made some major improvements to how you pass arguments to methods which will require migrating your existing code.
>
> If you want to migrate to the new patterns incrementally you can do so by installing `v0.5.0`. This release contains both
> the new and old patterns with a backwards compatibility layer.
>
> You can find a guide to migrating in [this document](#migration-guide).

[![PyPI version](https://img.shields.io/pypi/v/lithic.svg)](https://pypi.org/project/lithic/)

The Lithic Python library provides convenient access to the Lithic REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Documentation

The API documentation can be found [here](https://docs.lithic.com).

## Installation

```sh
pip install lithic
```

## Usage

```python
from lithic import Lithic

lithic = Lithic(
    # defaults to os.environ.get("LITHIC_API_KEY")
    api_key="my api key",
    # defaults to "production".
    environment="sandbox",
)

card = lithic.cards.create(
    type="SINGLE_USE",
)
print(card.token)
```

While you can provide an `api_key` keyword argument, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
and adding `LITHIC_API_KEY="my api key"` to your `.env` file so that your API Key is not stored in source control.

## Async Usage

Simply import `AsyncLithic` instead of `Lithic` and use `await` with each API call:

```python
from lithic import AsyncLithic

lithic = AsyncLithic(
    # defaults to os.environ.get("LITHIC_API_KEY")
    api_key="my api key",
    # defaults to "production".
    environment="sandbox",
)


async def main():
    card = await lithic.cards.create(
        type="SINGLE_USE",
    )
    print(card.token)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using Types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), while responses are [Pydantic](https://pydantic-docs.helpmanual.io/) models. This helps provide autocomplete and documentation within your editor.

If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Lithic API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import lithic

lithic = Lithic()

all_cards = []
# Automatically fetches more pages as needed.
for card in lithic.cards.list():
    # Do something with card here
    all_cards.append(card)
print(all_cards)
```

Or, asynchronously:

```python
import asyncio
import lithic

lithic = AsyncLithic()


async def main() -> None:
    all_cards = []
    # Iterate through items across all pages, issuing requests as needed.
    async for card in lithic.cards.list():
        all_cards.append(card)
    print(all_cards)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await lithic.cards.list()
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await lithic.cards.list()

print(f"page number: {first_page.page}")  # => "page number: 1"
for card in first_page.data:
    print(card.created)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```py
from lithic import Lithic

lithic = Lithic()

lithic.cards.create(
    foo={
        "bar": True
    },
)
```

## Handling errors

When the library is unable to connect to the API (e.g., due to network connection problems or a timeout), a subclass of `lithic.APIConnectionError` is raised.

When the API returns a non-success status code (i.e., 4xx or 5xx
response), a subclass of `lithic.APIStatusError` will be raised, containing `status_code` and `response` properties.

All errors inherit from `lithic.APIError`.

```python
from lithic import Lithic

lithic = Lithic()

try:
    lithic.cards.create(
        type="an_incorrect_type",
    )
except lithic.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except lithic.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except lithic.APIStatusError as e:
    print("Another non-200-range status code was received")
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
lithic = Lithic(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
lithic.with_options(max_retries=5).cards.list(
    page_size=10,
)
```

### Timeouts

Requests time out after 60 seconds by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
from lithic import Lithic

# Configure the default for all requests:
lithic = Lithic(
    # default is 60s
    timeout=20.0,
)

# More granular control:
lithic = Lithic(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
lithic.with_options(timeout=5 * 1000).cards.list(
    page_size=10,
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Advanced: Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
from lithic import Lithic

lithic = Lithic(
    # Use a custom base URL
    base_url="http://my.test.server.example.com:8083",
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

# Migration guide

This section outlines the features that were deprecated in `v0.5.0`, and subsequently removed in `v0.6.0` and how to migrate your code.

## Breaking changes

### TypedDict → keyword arguments

The way you pass arguments to methods has been changed from a single `TypedDict` to individual arguments. For example, this snippet:

```python
card = await client.cards.create({"type": "VIRTUAL"})
```

Now becomes:

```python
card = await client.cards.create(type="VIRTUAL")
```

#### Migrating

The easiest way to make your code compatible with this change is to add `**{`, for example:

```diff
- card = await client.cards.create({'type': 'VIRTUAL'})
+ card = await client.cards.create(**{'type': 'VIRTUAL'})
```

However, it is highly recommended to completely switch to explicit keyword arguments:

```diff
- card = await client.cards.create({'type': 'VIRTUAL'})
+ card = await client.cards.create(type='VIRTUAL')
```

### Named path arguments

All but the last path parameter must now be passed as named arguments instead of positional arguments, for example, for a method that calls the endpoint `/account_holders/{account_holder_token}/documents/{document_token}` you would've been able to call the method like this:

```python
card = await client.account_holders.retrieve(
    "account_holder_token", "my_document_token"
)
```

But now you must call the method like this:

```python
card = await client.account_holders.retrieve(
    "my_document_token", account_holder_token="account_holder_token"
)
```

If you have type checking enabled in your IDE it will tell you which parts of your code need to be updated.

### Request options

You used to be able to set request options on a per-method basis, now you can only set them on the client. There are two methods that you can use to make this easy, `with_options` and `copy`.

If you need to make multiple requests with changed options, you can use `.copy()` to get a new client object with those options. This can be useful if you need to set a custom header for multiple requests, for example:

```python
copied = client.copy(default_headers={"X-My-Header": "Foo"})
card = await copied.cards.create(type="VIRTUAL")
await copied.cards.provision(card.token, digital_wallet="GOOGLE_PAY")
```

If you just need to override one of the client options for one request, you can use `.with_options()`, for example:

```python
await client.with_options(timeout=None).cards.create(type="VIRTUAL")
```

It should be noted that the `.with_options()` method is simply an alias to `.copy()`, you can use them interchangeably.

You can pass nearly every argument that is supported by the Client `__init__` method to the `.copy()` method, except for `proxies` and `transport`.

```python
copied = client.copy(
    api_key="...",
    environment="sandbox",
    timeout=httpx.Timeout(read=10),
    max_retries=5,
    default_headers={
        "X-My-Header": "value",
    },
    default_query={
        "my_default_param": "value",
    },
)
```

## New features

### Pass custom headers

If you need to add additional headers to a request you can easily do so with the `extra_headers` argument:

```python
card = await client.cards.create(
    type="VIRTUAL",
    extra_headers={
        "X-Foo": "my header",
    },
)
```

### Pass custom JSON properties

You can add additional properties to the JSON request body that are not included directly in the method definition through the `extra_body` argument. This can be useful when there are in new properties in the API that are in beta and aren't in the SDK yet.

```python
card = await client.cards.create(
    type="VIRTUAL",
    extra_body={
        "special_prop": "foo",
    },
)
# sends this to the API:
# {"type": "VIRTUAL", "special_prop": "foo"}
```

### Pass custom query parameters

You can add additional query parameters that aren't specified in the method definition through the `extra_query` argument. This can be useful when there are any new/beta query parameters that are not yet in the SDK.

```python
card = await client.cards.create(
    type="VIRTUAL",
    extra_query={
        "special_param": "bar",
    },
)
# makes the request to this URL:
# https://api.lithic.com/v1/cards?special_param=bar
```

## Status

This package is in beta. Its internals and interfaces are not stable and subject to change without a major semver bump;
please reach out if you rely on any undocumented behavior.

We are keen for your feedback; please email us at [sdk-feedback@lithic.com](mailto:sdk-feedback@lithic.com) or open an issue with questions,
bugs, or suggestions.

## Requirements

Python 3.7 or higher.