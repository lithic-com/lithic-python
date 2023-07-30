#!/usr/bin/env -S poetry run python

#
# Run with: LITHIC_API_KEY=<your_api_key> poetry run python examples/upload_evidence.py
#

from lithic import Lithic, file_from_path

client = Lithic(environment="sandbox")

transactions_page = client.transactions.list()
assert len(transactions_page.data) > 0, "No transactions found"

transaction = transactions_page.data[0]
assert transaction.token, "Transaction must have a token"

disputes_page = client.disputes.list()
dispute = disputes_page.data[0]
if not dispute:
    dispute = client.disputes.create(
        amount=42,
        reason="ATM_CASH_MISDISPENSE",
        transaction_token=transaction.token,
    )

print(dispute)
assert dispute, "Could not find or create a dispute"

my_file = file_from_path("hello_world.txt")

upload = client.disputes.upload_evidence(dispute.token, my_file)
print(upload)

print("Done!")
