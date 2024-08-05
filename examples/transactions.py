#!/usr/bin/env -S rye run python

# To run this example locally
#   1. Install Rye and setup a Python virtual environment: ./scripts/bootstrap
#   2. Run the example: LITHIC_API_KEY=<your_api_key> rye run python examples/transactions.py

import asyncio

from lithic import AsyncLithic
from lithic.types import Card

client = AsyncLithic(environment="sandbox")


# Sleep function to add delays to simulate more realistic interactions with the sandbox API
async def sleep(ms: int) -> None:
    print(f"Waiting {ms}ms")
    await asyncio.sleep(ms / 1000)


async def simulate_auth_declined(card: Card) -> None:
    print("Simulate a transaction declined...")

    auth_response = await client.transactions.simulate_authorization(
        pan=card.pan or "unknown", amount=999999999999, descriptor="coffee shop"
    )

    await sleep(5000)

    transaction = await client.transactions.retrieve(auth_response.token or "unknown")
    assert transaction.result == "DECLINED", "Authorization was not declined"

    print("Done")


async def simulate_auth_clearing(card: Card) -> None:
    print("Simulate a transaction clearing...")

    auth_response = await client.transactions.simulate_authorization(
        pan=card.pan or "unknown", amount=50, descriptor="coffee shop"
    )

    await sleep(5000)

    await client.transactions.simulate_clearing(
        token=auth_response.token or "unknown",
    )

    await sleep(5000)

    transaction = await client.transactions.retrieve(auth_response.token or "unknown")
    assert transaction.status == "SETTLED", "Transaction was not settled"

    print("Done")


async def simulate_paginated_transaction(card: Card) -> None:
    print("Simulate a paginated transaction...")

    first_page = await client.transactions.list(
        card_token=card.token,
        account_token=card.account_token,
    )

    count_items_in_first_page = len(first_page.data)
    if count_items_in_first_page > 1:
        second_page = await client.transactions.list(
            card_token=card.token,
            account_token=card.account_token,
            starting_after=first_page.data[0].token,
        )

        assert first_page.data[1].token == second_page.data[0].token, "Tokens do not match"

    print("Done")


async def main() -> None:
    card = await client.cards.create(type="VIRTUAL")
    print(f"Created new card with token '{card.token}'")

    await sleep(2000)

    await simulate_auth_declined(card)
    await simulate_auth_clearing(card)
    await simulate_paginated_transaction(card)


if __name__ == "__main__":
    asyncio.run(main())
