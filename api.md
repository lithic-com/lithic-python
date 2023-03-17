# Shared Types

```python
from lithic.types import Address, ShippingAddress
```

# Top Level

Types:

```python
from lithic.types import APIStatus
```

Methods:

- <code title="get /status">client..<a href="./src/lithic/_client.py">api_status</a>() -> <a href="./src/lithic/types/api_status.py">APIStatus</a></code>

# Accounts

Types:

```python
from lithic.types import Account
```

Methods:

- <code title="get /accounts/{account_token}">client.accounts.<a href="./src/lithic/resources/accounts.py">retrieve</a>(account_token) -> <a href="./src/lithic/types/account.py">Account</a></code>
- <code title="patch /accounts/{account_token}">client.accounts.<a href="./src/lithic/resources/accounts.py">update</a>(account_token, \*\*<a href="src/lithic/types/account_update_params.py">params</a>) -> <a href="./src/lithic/types/account.py">Account</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/lithic/resources/accounts.py">list</a>(\*\*<a href="src/lithic/types/account_list_params.py">params</a>) -> <a href="./src/lithic/types/account.py">SyncPage[Account]</a></code>

# AccountHolders

Types:

```python
from lithic.types import (
    AccountHolder,
    AccountHolderDocument,
    AccountHolderUpdateResponse,
    AccountHolderListDocumentsResponse,
    AccountHolderCreateWebhookResponse,
)
```

Methods:

- <code title="post /account_holders">client.account_holders.<a href="./src/lithic/resources/account_holders.py">create</a>(\*\*<a href="src/lithic/types/account_holder_create_params.py">params</a>) -> <a href="./src/lithic/types/account_holder.py">AccountHolder</a></code>
- <code title="get /account_holders/{account_holder_token}">client.account_holders.<a href="./src/lithic/resources/account_holders.py">retrieve</a>(account_holder_token) -> <a href="./src/lithic/types/account_holder.py">AccountHolder</a></code>
- <code title="patch /account_holders/{account_holder_token}">client.account_holders.<a href="./src/lithic/resources/account_holders.py">update</a>(account_holder_token, \*\*<a href="src/lithic/types/account_holder_update_params.py">params</a>) -> <a href="./src/lithic/types/account_holder_update_response.py">AccountHolderUpdateResponse</a></code>
- <code title="post /webhooks/account_holders">client.account_holders.<a href="./src/lithic/resources/account_holders.py">create_webhook</a>(\*\*<a href="src/lithic/types/account_holder_create_webhook_params.py">params</a>) -> <a href="./src/lithic/types/account_holder_create_webhook_response.py">AccountHolderCreateWebhookResponse</a></code>
- <code title="get /account_holders/{account_holder_token}/documents">client.account_holders.<a href="./src/lithic/resources/account_holders.py">list_documents</a>(account_holder_token) -> <a href="./src/lithic/types/account_holder_list_documents_response.py">AccountHolderListDocumentsResponse</a></code>
- <code title="post /account_holders/{account_holder_token}/resubmit">client.account_holders.<a href="./src/lithic/resources/account_holders.py">resubmit</a>(account_holder_token, \*\*<a href="src/lithic/types/account_holder_resubmit_params.py">params</a>) -> <a href="./src/lithic/types/account_holder.py">AccountHolder</a></code>
- <code title="get /account_holders/{account_holder_token}/documents/{document_token}">client.account_holders.<a href="./src/lithic/resources/account_holders.py">retrieve_document</a>(document_token, account_holder_token) -> <a href="./src/lithic/types/account_holder_document.py">AccountHolderDocument</a></code>
- <code title="post /account_holders/{account_holder_token}/documents">client.account_holders.<a href="./src/lithic/resources/account_holders.py">upload_document</a>(account_holder_token, \*\*<a href="src/lithic/types/account_holder_upload_document_params.py">params</a>) -> <a href="./src/lithic/types/account_holder_document.py">AccountHolderDocument</a></code>

# AuthRules

Types:

```python
from lithic.types import (
    AuthRule,
    AuthRuleCreateResponse,
    AuthRuleRetrieveResponse,
    AuthRuleUpdateResponse,
    AuthRuleApplyResponse,
    AuthRuleRemoveResponse,
)
```

Methods:

- <code title="post /auth_rules">client.auth_rules.<a href="./src/lithic/resources/auth_rules.py">create</a>(\*\*<a href="src/lithic/types/auth_rule_create_params.py">params</a>) -> <a href="./src/lithic/types/auth_rule_create_response.py">AuthRuleCreateResponse</a></code>
- <code title="get /auth_rules/{auth_rule_token}">client.auth_rules.<a href="./src/lithic/resources/auth_rules.py">retrieve</a>(auth_rule_token) -> <a href="./src/lithic/types/auth_rule_retrieve_response.py">AuthRuleRetrieveResponse</a></code>
- <code title="put /auth_rules/{auth_rule_token}">client.auth_rules.<a href="./src/lithic/resources/auth_rules.py">update</a>(auth_rule_token, \*\*<a href="src/lithic/types/auth_rule_update_params.py">params</a>) -> <a href="./src/lithic/types/auth_rule_update_response.py">AuthRuleUpdateResponse</a></code>
- <code title="get /auth_rules">client.auth_rules.<a href="./src/lithic/resources/auth_rules.py">list</a>(\*\*<a href="src/lithic/types/auth_rule_list_params.py">params</a>) -> <a href="./src/lithic/types/auth_rule.py">SyncPage[AuthRule]</a></code>
- <code title="post /auth_rules/{auth_rule_token}/apply">client.auth_rules.<a href="./src/lithic/resources/auth_rules.py">apply</a>(auth_rule_token, \*\*<a href="src/lithic/types/auth_rule_apply_params.py">params</a>) -> <a href="./src/lithic/types/auth_rule_apply_response.py">AuthRuleApplyResponse</a></code>
- <code title="delete /auth_rules/remove">client.auth_rules.<a href="./src/lithic/resources/auth_rules.py">remove</a>(\*\*<a href="src/lithic/types/auth_rule_remove_params.py">params</a>) -> <a href="./src/lithic/types/auth_rule_remove_response.py">AuthRuleRemoveResponse</a></code>

# AuthStreamEnrollmentResource

Types:

```python
from lithic.types import AuthStreamEnrollment
```

Methods:

- <code title="get /auth_stream">client.auth_stream_enrollment.<a href="./src/lithic/resources/auth_stream_enrollment.py">retrieve</a>() -> <a href="./src/lithic/types/auth_stream_enrollment.py">AuthStreamEnrollment</a></code>
- <code title="delete /auth_stream">client.auth_stream_enrollment.<a href="./src/lithic/resources/auth_stream_enrollment.py">disenroll</a>() -> None</code>
- <code title="post /auth_stream">client.auth_stream_enrollment.<a href="./src/lithic/resources/auth_stream_enrollment.py">enroll</a>(\*\*<a href="src/lithic/types/auth_stream_enrollment_enroll_params.py">params</a>) -> None</code>

# Cards

Types:

```python
from lithic.types import (
    Card,
    EmbedRequestParams,
    SpendLimitDuration,
    CardProvisionResponse,
    CardEmbedResponse,
)
```

Methods:

- <code title="post /cards">client.cards.<a href="./src/lithic/resources/cards.py">create</a>(\*\*<a href="src/lithic/types/card_create_params.py">params</a>) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code title="get /cards/{card_token}">client.cards.<a href="./src/lithic/resources/cards.py">retrieve</a>(card_token) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code title="patch /cards/{card_token}">client.cards.<a href="./src/lithic/resources/cards.py">update</a>(card_token, \*\*<a href="src/lithic/types/card_update_params.py">params</a>) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code title="get /cards">client.cards.<a href="./src/lithic/resources/cards.py">list</a>(\*\*<a href="src/lithic/types/card_list_params.py">params</a>) -> <a href="./src/lithic/types/card.py">SyncPage[Card]</a></code>
- <code title="get /embed/card">client.cards.<a href="./src/lithic/resources/cards.py">embed</a>(\*\*<a href="src/lithic/types/card_embed_params.py">params</a>) -> str</code>
- <code title="post /cards/{card_token}/provision">client.cards.<a href="./src/lithic/resources/cards.py">provision</a>(card_token, \*\*<a href="src/lithic/types/card_provision_params.py">params</a>) -> <a href="./src/lithic/types/card_provision_response.py">CardProvisionResponse</a></code>
- <code title="post /cards/{card_token}/reissue">client.cards.<a href="./src/lithic/resources/cards.py">reissue</a>(card_token, \*\*<a href="src/lithic/types/card_reissue_params.py">params</a>) -> <a href="./src/lithic/types/card.py">Card</a></code>

Custom Methods:

- `get_embed_html`
- `get_embed_url`

# Disputes

Types:

```python
from lithic.types import Dispute, DisputeEvidence, DisputeInitiateEvidenceUploadResponse
```

Methods:

- <code title="post /disputes">client.disputes.<a href="./src/lithic/resources/disputes.py">create</a>(\*\*<a href="src/lithic/types/dispute_create_params.py">params</a>) -> <a href="./src/lithic/types/dispute.py">Dispute</a></code>
- <code title="get /disputes/{dispute_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">retrieve</a>(dispute_token) -> <a href="./src/lithic/types/dispute.py">Dispute</a></code>
- <code title="patch /disputes/{dispute_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">update</a>(dispute_token, \*\*<a href="src/lithic/types/dispute_update_params.py">params</a>) -> <a href="./src/lithic/types/dispute.py">Dispute</a></code>
- <code title="get /disputes">client.disputes.<a href="./src/lithic/resources/disputes.py">list</a>(\*\*<a href="src/lithic/types/dispute_list_params.py">params</a>) -> <a href="./src/lithic/types/dispute.py">SyncCursorPage[Dispute]</a></code>
- <code title="delete /disputes/{dispute_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">delete</a>(dispute_token) -> <a href="./src/lithic/types/dispute.py">Dispute</a></code>
- <code title="delete /disputes/{dispute_token}/evidences/{evidence_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">delete_evidence</a>(evidence_token, dispute_token) -> <a href="./src/lithic/types/dispute_evidence.py">DisputeEvidence</a></code>
- <code title="post /disputes/{dispute_token}/evidences">client.disputes.<a href="./src/lithic/resources/disputes.py">initiate_evidence_upload</a>(dispute_token) -> <a href="./src/lithic/types/dispute_initiate_evidence_upload_response.py">DisputeInitiateEvidenceUploadResponse</a></code>
- <code title="get /disputes/{dispute_token}/evidences">client.disputes.<a href="./src/lithic/resources/disputes.py">list_evidences</a>(dispute_token, \*\*<a href="src/lithic/types/dispute_list_evidences_params.py">params</a>) -> <a href="./src/lithic/types/dispute_evidence.py">SyncCursorPage[DisputeEvidence]</a></code>
- <code title="get /disputes/{dispute_token}/evidences/{evidence_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">retrieve_evidence</a>(evidence_token, dispute_token) -> <a href="./src/lithic/types/dispute_evidence.py">DisputeEvidence</a></code>

Custom Methods:

- `upload_evidence`

# Events

Types:

```python
from lithic.types import Event, EventSubscription
```

Methods:

- <code title="get /events/{event_token}">client.events.<a href="./src/lithic/resources/events/events.py">retrieve</a>(event_token) -> <a href="./src/lithic/types/event.py">Event</a></code>
- <code title="get /events">client.events.<a href="./src/lithic/resources/events/events.py">list</a>(\*\*<a href="src/lithic/types/event_list_params.py">params</a>) -> <a href="./src/lithic/types/event.py">SyncCursorPage[Event]</a></code>

Custom Methods:

- `resend`

## Subscriptions

Types:

```python
from lithic.types.events import SubscriptionRetrieveSecretResponse
```

Methods:

- <code title="post /event_subscriptions">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">create</a>(\*\*<a href="src/lithic/types/events/subscription_create_params.py">params</a>) -> <a href="./src/lithic/types/event_subscription.py">EventSubscription</a></code>
- <code title="get /event_subscriptions/{event_subscription_token}">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">retrieve</a>(event_subscription_token) -> <a href="./src/lithic/types/event_subscription.py">EventSubscription</a></code>
- <code title="patch /event_subscriptions/{event_subscription_token}">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">update</a>(event_subscription_token, \*\*<a href="src/lithic/types/events/subscription_update_params.py">params</a>) -> <a href="./src/lithic/types/event_subscription.py">EventSubscription</a></code>
- <code title="get /event_subscriptions">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">list</a>(\*\*<a href="src/lithic/types/events/subscription_list_params.py">params</a>) -> <a href="./src/lithic/types/event_subscription.py">SyncCursorPage[EventSubscription]</a></code>
- <code title="delete /event_subscriptions/{event_subscription_token}">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">delete</a>(event_subscription_token) -> None</code>
- <code title="post /event_subscriptions/{event_subscription_token}/recover">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">recover</a>(event_subscription_token) -> None</code>
- <code title="post /event_subscriptions/{event_subscription_token}/replay_missing">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">replay_missing</a>(event_subscription_token) -> None</code>
- <code title="get /event_subscriptions/{event_subscription_token}/secret">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">retrieve_secret</a>(event_subscription_token) -> <a href="./src/lithic/types/events/subscription_retrieve_secret_response.py">SubscriptionRetrieveSecretResponse</a></code>
- <code title="post /event_subscriptions/{event_subscription_token}/secret/rotate">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">rotate_secret</a>(event_subscription_token) -> None</code>

# FundingSources

Types:

```python
from lithic.types import FundingSource
```

Methods:

- <code title="post /funding_sources">client.funding_sources.<a href="./src/lithic/resources/funding_sources.py">create</a>(\*\*<a href="src/lithic/types/funding_source_create_params.py">params</a>) -> <a href="./src/lithic/types/funding_source.py">FundingSource</a></code>
- <code title="patch /funding_sources/{funding_source_token}">client.funding_sources.<a href="./src/lithic/resources/funding_sources.py">update</a>(funding_source_token, \*\*<a href="src/lithic/types/funding_source_update_params.py">params</a>) -> <a href="./src/lithic/types/funding_source.py">FundingSource</a></code>
- <code title="get /funding_sources">client.funding_sources.<a href="./src/lithic/resources/funding_sources.py">list</a>(\*\*<a href="src/lithic/types/funding_source_list_params.py">params</a>) -> <a href="./src/lithic/types/funding_source.py">SyncPage[FundingSource]</a></code>
- <code title="post /funding_sources/{funding_source_token}/verify">client.funding_sources.<a href="./src/lithic/resources/funding_sources.py">verify</a>(funding_source_token, \*\*<a href="src/lithic/types/funding_source_verify_params.py">params</a>) -> <a href="./src/lithic/types/funding_source.py">FundingSource</a></code>

# Transactions

Types:

```python
from lithic.types import (
    Transaction,
    TransactionSimulateAuthorizationResponse,
    TransactionSimulateClearingResponse,
    TransactionSimulateReturnResponse,
    TransactionSimulateReturnReversalResponse,
    TransactionSimulateVoidResponse,
    TransactionSimulateCreditAuthorizationResponse,
)
```

Methods:

- <code title="get /transactions/{transaction_token}">client.transactions.<a href="./src/lithic/resources/transactions.py">retrieve</a>(transaction_token) -> <a href="./src/lithic/types/transaction.py">Transaction</a></code>
- <code title="get /transactions">client.transactions.<a href="./src/lithic/resources/transactions.py">list</a>(\*\*<a href="src/lithic/types/transaction_list_params.py">params</a>) -> <a href="./src/lithic/types/transaction.py">SyncPage[Transaction]</a></code>
- <code title="post /simulate/authorize">client.transactions.<a href="./src/lithic/resources/transactions.py">simulate_authorization</a>(\*\*<a href="src/lithic/types/transaction_simulate_authorization_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_authorization_response.py">TransactionSimulateAuthorizationResponse</a></code>
- <code title="post /simulate/clearing">client.transactions.<a href="./src/lithic/resources/transactions.py">simulate_clearing</a>(\*\*<a href="src/lithic/types/transaction_simulate_clearing_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_clearing_response.py">TransactionSimulateClearingResponse</a></code>
- <code title="post /simulate/credit_authorization_advice">client.transactions.<a href="./src/lithic/resources/transactions.py">simulate_credit_authorization</a>(\*\*<a href="src/lithic/types/transaction_simulate_credit_authorization_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_credit_authorization_response.py">TransactionSimulateCreditAuthorizationResponse</a></code>
- <code title="post /simulate/return">client.transactions.<a href="./src/lithic/resources/transactions.py">simulate_return</a>(\*\*<a href="src/lithic/types/transaction_simulate_return_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_return_response.py">TransactionSimulateReturnResponse</a></code>
- <code title="post /simulate/return_reversal">client.transactions.<a href="./src/lithic/resources/transactions.py">simulate_return_reversal</a>(\*\*<a href="src/lithic/types/transaction_simulate_return_reversal_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_return_reversal_response.py">TransactionSimulateReturnReversalResponse</a></code>
- <code title="post /simulate/void">client.transactions.<a href="./src/lithic/resources/transactions.py">simulate_void</a>(\*\*<a href="src/lithic/types/transaction_simulate_void_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_void_response.py">TransactionSimulateVoidResponse</a></code>

# Webhooks

Custom Methods:

- `unwrap`
- `verify_signature`