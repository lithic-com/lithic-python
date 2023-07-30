#!/usr/bin/env -S poetry run python

from datetime import datetime

from lithic import Lithic

client = Lithic(environment="sandbox")

now = datetime.now()

# datetime responses will always be instances of `datetime`
card = client.cards.create(type="VIRTUAL")
assert isinstance(card.created, datetime)
assert card.created.year == now.year
assert card.created.month == now.month
assert card.created.tzname() == "UTC"

dt = datetime.fromisoformat("2022-07-25T21:34:45+00:00")

# # both `datetime` instances or datetime strings can be passed as a request param
page = client.cards.list(begin=dt, page_size=1)
assert len(page.data) == 1

page = client.cards.list(begin=dt.isoformat(), page_size=1)
assert len(page.data) == 1
