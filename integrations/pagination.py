#!/usr/bin/env -S rye run python integrations/pagination.py

from __future__ import annotations

import json

from lithic import Lithic

client = Lithic(environment="sandbox")


def main() -> None:
    page = client.transactions.list()
    assert len(page.data) > 0, "No transactions found"

    if not page.has_more or not page.has_next_page():
        raise RuntimeError(f"Expected multiple pages to be present, only got {len(page.data)} items")

    tokens: dict[str, int] = {}

    for transaction in page:
        tokens[transaction.token] = tokens.get(transaction.token, 0) + 1

    duplicates = {token: count for token, count in tokens.items() if count > 1}
    if duplicates:
        print(json.dumps(duplicates, indent=2))  # noqa: T201
        raise RuntimeError(f"Found {len(duplicates)} duplicate entries!")

    print("Success!")  # noqa: T201


main()
