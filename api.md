# Shared Types

```python
from lithic.types import (
    AccountFinancialAccountType,
    Address,
    Carrier,
    Currency,
    Document,
    InstanceFinancialAccountType,
    ShippingAddress,
)
```

# Lithic

Types:

```python
from lithic.types import APIStatus
```

Methods:

- <code title="get /v1/status">client.<a href="./src/lithic/_client.py">api_status</a>() -> <a href="./src/lithic/types/api_status.py">APIStatus</a></code>

# Accounts

Types:

```python
from lithic.types import Account, AccountSpendLimits
```

Methods:

- <code title="get /v1/accounts/{account_token}">client.accounts.<a href="./src/lithic/resources/accounts.py">retrieve</a>(account_token) -> <a href="./src/lithic/types/account.py">Account</a></code>
- <code title="patch /v1/accounts/{account_token}">client.accounts.<a href="./src/lithic/resources/accounts.py">update</a>(account_token, \*\*<a href="src/lithic/types/account_update_params.py">params</a>) -> <a href="./src/lithic/types/account.py">Account</a></code>
- <code title="get /v1/accounts">client.accounts.<a href="./src/lithic/resources/accounts.py">list</a>(\*\*<a href="src/lithic/types/account_list_params.py">params</a>) -> <a href="./src/lithic/types/account.py">SyncCursorPage[Account]</a></code>
- <code title="get /v1/accounts/{account_token}/spend_limits">client.accounts.<a href="./src/lithic/resources/accounts.py">retrieve_spend_limits</a>(account_token) -> <a href="./src/lithic/types/account_spend_limits.py">AccountSpendLimits</a></code>

# AccountHolders

Types:

```python
from lithic.types import (
    AccountHolder,
    AddressUpdate,
    KYB,
    KYBBusinessEntity,
    KYC,
    KYCExempt,
    RequiredDocument,
    AccountHolderCreateResponse,
    AccountHolderUpdateResponse,
    AccountHolderListDocumentsResponse,
    AccountHolderSimulateEnrollmentReviewResponse,
)
```

Methods:

- <code title="post /v1/account_holders">client.account_holders.<a href="./src/lithic/resources/account_holders.py">create</a>(\*\*<a href="src/lithic/types/account_holder_create_params.py">params</a>) -> <a href="./src/lithic/types/account_holder_create_response.py">AccountHolderCreateResponse</a></code>
- <code title="get /v1/account_holders/{account_holder_token}">client.account_holders.<a href="./src/lithic/resources/account_holders.py">retrieve</a>(account_holder_token) -> <a href="./src/lithic/types/account_holder.py">AccountHolder</a></code>
- <code title="patch /v1/account_holders/{account_holder_token}">client.account_holders.<a href="./src/lithic/resources/account_holders.py">update</a>(account_holder_token, \*\*<a href="src/lithic/types/account_holder_update_params.py">params</a>) -> <a href="./src/lithic/types/account_holder_update_response.py">AccountHolderUpdateResponse</a></code>
- <code title="get /v1/account_holders">client.account_holders.<a href="./src/lithic/resources/account_holders.py">list</a>(\*\*<a href="src/lithic/types/account_holder_list_params.py">params</a>) -> <a href="./src/lithic/types/account_holder.py">SyncSinglePage[AccountHolder]</a></code>
- <code title="get /v1/account_holders/{account_holder_token}/documents">client.account_holders.<a href="./src/lithic/resources/account_holders.py">list_documents</a>(account_holder_token) -> <a href="./src/lithic/types/account_holder_list_documents_response.py">AccountHolderListDocumentsResponse</a></code>
- <code title="get /v1/account_holders/{account_holder_token}/documents/{document_token}">client.account_holders.<a href="./src/lithic/resources/account_holders.py">retrieve_document</a>(document_token, \*, account_holder_token) -> <a href="./src/lithic/types/shared/document.py">Document</a></code>
- <code title="post /v1/simulate/account_holders/enrollment_document_review">client.account_holders.<a href="./src/lithic/resources/account_holders.py">simulate_enrollment_document_review</a>(\*\*<a href="src/lithic/types/account_holder_simulate_enrollment_document_review_params.py">params</a>) -> <a href="./src/lithic/types/shared/document.py">Document</a></code>
- <code title="post /v1/simulate/account_holders/enrollment_review">client.account_holders.<a href="./src/lithic/resources/account_holders.py">simulate_enrollment_review</a>(\*\*<a href="src/lithic/types/account_holder_simulate_enrollment_review_params.py">params</a>) -> <a href="./src/lithic/types/account_holder_simulate_enrollment_review_response.py">AccountHolderSimulateEnrollmentReviewResponse</a></code>
- <code title="post /v1/account_holders/{account_holder_token}/documents">client.account_holders.<a href="./src/lithic/resources/account_holders.py">upload_document</a>(account_holder_token, \*\*<a href="src/lithic/types/account_holder_upload_document_params.py">params</a>) -> <a href="./src/lithic/types/shared/document.py">Document</a></code>

# AuthRules

## V2

Types:

```python
from lithic.types.auth_rules import (
    AuthRule,
    AuthRuleCondition,
    ConditionalAttribute,
    ConditionalBlockParameters,
    VelocityLimitParams,
    VelocityLimitParamsPeriodWindow,
    V2CreateResponse,
    V2RetrieveResponse,
    V2UpdateResponse,
    V2ListResponse,
    V2ApplyResponse,
    V2DraftResponse,
    V2PromoteResponse,
    V2ReportResponse,
)
```

Methods:

- <code title="post /v2/auth_rules">client.auth_rules.v2.<a href="./src/lithic/resources/auth_rules/v2/v2.py">create</a>(\*\*<a href="src/lithic/types/auth_rules/v2_create_params.py">params</a>) -> <a href="./src/lithic/types/auth_rules/v2_create_response.py">V2CreateResponse</a></code>
- <code title="get /v2/auth_rules/{auth_rule_token}">client.auth_rules.v2.<a href="./src/lithic/resources/auth_rules/v2/v2.py">retrieve</a>(auth_rule_token) -> <a href="./src/lithic/types/auth_rules/v2_retrieve_response.py">V2RetrieveResponse</a></code>
- <code title="patch /v2/auth_rules/{auth_rule_token}">client.auth_rules.v2.<a href="./src/lithic/resources/auth_rules/v2/v2.py">update</a>(auth_rule_token, \*\*<a href="src/lithic/types/auth_rules/v2_update_params.py">params</a>) -> <a href="./src/lithic/types/auth_rules/v2_update_response.py">V2UpdateResponse</a></code>
- <code title="get /v2/auth_rules">client.auth_rules.v2.<a href="./src/lithic/resources/auth_rules/v2/v2.py">list</a>(\*\*<a href="src/lithic/types/auth_rules/v2_list_params.py">params</a>) -> <a href="./src/lithic/types/auth_rules/v2_list_response.py">SyncCursorPage[V2ListResponse]</a></code>
- <code title="delete /v2/auth_rules/{auth_rule_token}">client.auth_rules.v2.<a href="./src/lithic/resources/auth_rules/v2/v2.py">delete</a>(auth_rule_token) -> None</code>
- <code title="post /v2/auth_rules/{auth_rule_token}/apply">client.auth_rules.v2.<a href="./src/lithic/resources/auth_rules/v2/v2.py">apply</a>(auth_rule_token, \*\*<a href="src/lithic/types/auth_rules/v2_apply_params.py">params</a>) -> <a href="./src/lithic/types/auth_rules/v2_apply_response.py">V2ApplyResponse</a></code>
- <code title="post /v2/auth_rules/{auth_rule_token}/draft">client.auth_rules.v2.<a href="./src/lithic/resources/auth_rules/v2/v2.py">draft</a>(auth_rule_token, \*\*<a href="src/lithic/types/auth_rules/v2_draft_params.py">params</a>) -> <a href="./src/lithic/types/auth_rules/v2_draft_response.py">V2DraftResponse</a></code>
- <code title="post /v2/auth_rules/{auth_rule_token}/promote">client.auth_rules.v2.<a href="./src/lithic/resources/auth_rules/v2/v2.py">promote</a>(auth_rule_token) -> <a href="./src/lithic/types/auth_rules/v2_promote_response.py">V2PromoteResponse</a></code>
- <code title="post /v2/auth_rules/{auth_rule_token}/report">client.auth_rules.v2.<a href="./src/lithic/resources/auth_rules/v2/v2.py">report</a>(auth_rule_token) -> <a href="./src/lithic/types/auth_rules/v2_report_response.py">V2ReportResponse</a></code>

### Backtests

Types:

```python
from lithic.types.auth_rules.v2 import BacktestResults, BacktestCreateResponse
```

Methods:

- <code title="post /v2/auth_rules/{auth_rule_token}/backtests">client.auth_rules.v2.backtests.<a href="./src/lithic/resources/auth_rules/v2/backtests.py">create</a>(auth_rule_token, \*\*<a href="src/lithic/types/auth_rules/v2/backtest_create_params.py">params</a>) -> <a href="./src/lithic/types/auth_rules/v2/backtest_create_response.py">BacktestCreateResponse</a></code>
- <code title="get /v2/auth_rules/{auth_rule_token}/backtests/{auth_rule_backtest_token}">client.auth_rules.v2.backtests.<a href="./src/lithic/resources/auth_rules/v2/backtests.py">retrieve</a>(auth_rule_backtest_token, \*, auth_rule_token) -> <a href="./src/lithic/types/auth_rules/v2/backtest_results.py">BacktestResults</a></code>

# AuthStreamEnrollment

Types:

```python
from lithic.types import AuthStreamSecret
```

Methods:

- <code title="get /v1/auth_stream/secret">client.auth_stream_enrollment.<a href="./src/lithic/resources/auth_stream_enrollment.py">retrieve_secret</a>() -> <a href="./src/lithic/types/auth_stream_secret.py">AuthStreamSecret</a></code>
- <code title="post /v1/auth_stream/secret/rotate">client.auth_stream_enrollment.<a href="./src/lithic/resources/auth_stream_enrollment.py">rotate_secret</a>() -> None</code>

# TokenizationDecisioning

Types:

```python
from lithic.types import TokenizationSecret, TokenizationDecisioningRotateSecretResponse
```

Methods:

- <code title="get /v1/tokenization_decisioning/secret">client.tokenization_decisioning.<a href="./src/lithic/resources/tokenization_decisioning.py">retrieve_secret</a>() -> <a href="./src/lithic/types/tokenization_secret.py">TokenizationSecret</a></code>
- <code title="post /v1/tokenization_decisioning/secret/rotate">client.tokenization_decisioning.<a href="./src/lithic/resources/tokenization_decisioning.py">rotate_secret</a>() -> <a href="./src/lithic/types/tokenization_decisioning_rotate_secret_response.py">TokenizationDecisioningRotateSecretResponse</a></code>

# Tokenizations

Types:

```python
from lithic.types import (
    Tokenization,
    TokenizationRetrieveResponse,
    TokenizationSimulateResponse,
    TokenizationUpdateDigitalCardArtResponse,
)
```

Methods:

- <code title="get /v1/tokenizations/{tokenization_token}">client.tokenizations.<a href="./src/lithic/resources/tokenizations.py">retrieve</a>(tokenization_token) -> <a href="./src/lithic/types/tokenization_retrieve_response.py">TokenizationRetrieveResponse</a></code>
- <code title="get /v1/tokenizations">client.tokenizations.<a href="./src/lithic/resources/tokenizations.py">list</a>(\*\*<a href="src/lithic/types/tokenization_list_params.py">params</a>) -> <a href="./src/lithic/types/tokenization.py">SyncCursorPage[Tokenization]</a></code>
- <code title="post /v1/tokenizations/{tokenization_token}/activate">client.tokenizations.<a href="./src/lithic/resources/tokenizations.py">activate</a>(tokenization_token) -> None</code>
- <code title="post /v1/tokenizations/{tokenization_token}/deactivate">client.tokenizations.<a href="./src/lithic/resources/tokenizations.py">deactivate</a>(tokenization_token) -> None</code>
- <code title="post /v1/tokenizations/{tokenization_token}/pause">client.tokenizations.<a href="./src/lithic/resources/tokenizations.py">pause</a>(tokenization_token) -> None</code>
- <code title="post /v1/tokenizations/{tokenization_token}/resend_activation_code">client.tokenizations.<a href="./src/lithic/resources/tokenizations.py">resend_activation_code</a>(tokenization_token, \*\*<a href="src/lithic/types/tokenization_resend_activation_code_params.py">params</a>) -> None</code>
- <code title="post /v1/simulate/tokenizations">client.tokenizations.<a href="./src/lithic/resources/tokenizations.py">simulate</a>(\*\*<a href="src/lithic/types/tokenization_simulate_params.py">params</a>) -> <a href="./src/lithic/types/tokenization_simulate_response.py">TokenizationSimulateResponse</a></code>
- <code title="post /v1/tokenizations/{tokenization_token}/unpause">client.tokenizations.<a href="./src/lithic/resources/tokenizations.py">unpause</a>(tokenization_token) -> None</code>
- <code title="post /v1/tokenizations/{tokenization_token}/update_digital_card_art">client.tokenizations.<a href="./src/lithic/resources/tokenizations.py">update_digital_card_art</a>(tokenization_token, \*\*<a href="src/lithic/types/tokenization_update_digital_card_art_params.py">params</a>) -> <a href="./src/lithic/types/tokenization_update_digital_card_art_response.py">TokenizationUpdateDigitalCardArtResponse</a></code>

# Cards

Types:

```python
from lithic.types import (
    Card,
    CardSpendLimits,
    SpendLimitDuration,
    CardEmbedResponse,
    CardProvisionResponse,
)
```

Methods:

- <code title="post /v1/cards">client.cards.<a href="./src/lithic/resources/cards/cards.py">create</a>(\*\*<a href="src/lithic/types/card_create_params.py">params</a>) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code title="get /v1/cards/{card_token}">client.cards.<a href="./src/lithic/resources/cards/cards.py">retrieve</a>(card_token) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code title="patch /v1/cards/{card_token}">client.cards.<a href="./src/lithic/resources/cards/cards.py">update</a>(card_token, \*\*<a href="src/lithic/types/card_update_params.py">params</a>) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code title="get /v1/cards">client.cards.<a href="./src/lithic/resources/cards/cards.py">list</a>(\*\*<a href="src/lithic/types/card_list_params.py">params</a>) -> <a href="./src/lithic/types/card.py">SyncCursorPage[Card]</a></code>
- <code title="post /v1/cards/{card_token}/convert_physical">client.cards.<a href="./src/lithic/resources/cards/cards.py">convert_physical</a>(card_token, \*\*<a href="src/lithic/types/card_convert_physical_params.py">params</a>) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code title="get /v1/embed/card">client.cards.<a href="./src/lithic/resources/cards/cards.py">embed</a>(\*\*<a href="src/lithic/types/card_embed_params.py">params</a>) -> str</code>
- <code title="post /v1/cards/{card_token}/provision">client.cards.<a href="./src/lithic/resources/cards/cards.py">provision</a>(card_token, \*\*<a href="src/lithic/types/card_provision_params.py">params</a>) -> <a href="./src/lithic/types/card_provision_response.py">CardProvisionResponse</a></code>
- <code title="post /v1/cards/{card_token}/reissue">client.cards.<a href="./src/lithic/resources/cards/cards.py">reissue</a>(card_token, \*\*<a href="src/lithic/types/card_reissue_params.py">params</a>) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code title="post /v1/cards/{card_token}/renew">client.cards.<a href="./src/lithic/resources/cards/cards.py">renew</a>(card_token, \*\*<a href="src/lithic/types/card_renew_params.py">params</a>) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code title="get /v1/cards/{card_token}/spend_limits">client.cards.<a href="./src/lithic/resources/cards/cards.py">retrieve_spend_limits</a>(card_token) -> <a href="./src/lithic/types/card_spend_limits.py">CardSpendLimits</a></code>
- <code title="post /v1/cards/search_by_pan">client.cards.<a href="./src/lithic/resources/cards/cards.py">search_by_pan</a>(\*\*<a href="src/lithic/types/card_search_by_pan_params.py">params</a>) -> <a href="./src/lithic/types/card.py">Card</a></code>
- <code>client.cards.<a href="./src/lithic/resources/cards/cards.py">get_embed_html</a>(\*args) -> str</code>
- <code>client.cards.<a href="./src/lithic/resources/cards/cards.py">get_embed_url</a>(\*args) -> URL</code>

## AggregateBalances

Types:

```python
from lithic.types.cards import AggregateBalanceListResponse
```

Methods:

- <code title="get /v1/cards/aggregate_balances">client.cards.aggregate_balances.<a href="./src/lithic/resources/cards/aggregate_balances.py">list</a>(\*\*<a href="src/lithic/types/cards/aggregate_balance_list_params.py">params</a>) -> <a href="./src/lithic/types/cards/aggregate_balance_list_response.py">SyncSinglePage[AggregateBalanceListResponse]</a></code>

## Balances

Types:

```python
from lithic.types.cards import BalanceListResponse
```

Methods:

- <code title="get /v1/cards/{card_token}/balances">client.cards.balances.<a href="./src/lithic/resources/cards/balances.py">list</a>(card_token, \*\*<a href="src/lithic/types/cards/balance_list_params.py">params</a>) -> <a href="./src/lithic/types/cards/balance_list_response.py">SyncSinglePage[BalanceListResponse]</a></code>

## FinancialTransactions

Methods:

- <code title="get /v1/cards/{card_token}/financial_transactions/{financial_transaction_token}">client.cards.financial_transactions.<a href="./src/lithic/resources/cards/financial_transactions.py">retrieve</a>(financial_transaction_token, \*, card_token) -> <a href="./src/lithic/types/financial_transaction.py">FinancialTransaction</a></code>
- <code title="get /v1/cards/{card_token}/financial_transactions">client.cards.financial_transactions.<a href="./src/lithic/resources/cards/financial_transactions.py">list</a>(card_token, \*\*<a href="src/lithic/types/cards/financial_transaction_list_params.py">params</a>) -> <a href="./src/lithic/types/financial_transaction.py">SyncSinglePage[FinancialTransaction]</a></code>

# Balances

Types:

```python
from lithic.types import Balance
```

Methods:

- <code title="get /v1/balances">client.balances.<a href="./src/lithic/resources/balances.py">list</a>(\*\*<a href="src/lithic/types/balance_list_params.py">params</a>) -> <a href="./src/lithic/types/balance.py">SyncSinglePage[Balance]</a></code>

# AggregateBalances

Types:

```python
from lithic.types import AggregateBalance
```

Methods:

- <code title="get /v1/aggregate_balances">client.aggregate_balances.<a href="./src/lithic/resources/aggregate_balances.py">list</a>(\*\*<a href="src/lithic/types/aggregate_balance_list_params.py">params</a>) -> <a href="./src/lithic/types/aggregate_balance.py">SyncSinglePage[AggregateBalance]</a></code>

# Disputes

Types:

```python
from lithic.types import Dispute, DisputeEvidence
```

Methods:

- <code title="post /v1/disputes">client.disputes.<a href="./src/lithic/resources/disputes.py">create</a>(\*\*<a href="src/lithic/types/dispute_create_params.py">params</a>) -> <a href="./src/lithic/types/dispute.py">Dispute</a></code>
- <code title="get /v1/disputes/{dispute_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">retrieve</a>(dispute_token) -> <a href="./src/lithic/types/dispute.py">Dispute</a></code>
- <code title="patch /v1/disputes/{dispute_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">update</a>(dispute_token, \*\*<a href="src/lithic/types/dispute_update_params.py">params</a>) -> <a href="./src/lithic/types/dispute.py">Dispute</a></code>
- <code title="get /v1/disputes">client.disputes.<a href="./src/lithic/resources/disputes.py">list</a>(\*\*<a href="src/lithic/types/dispute_list_params.py">params</a>) -> <a href="./src/lithic/types/dispute.py">SyncCursorPage[Dispute]</a></code>
- <code title="delete /v1/disputes/{dispute_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">delete</a>(dispute_token) -> <a href="./src/lithic/types/dispute.py">Dispute</a></code>
- <code title="delete /v1/disputes/{dispute_token}/evidences/{evidence_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">delete_evidence</a>(evidence_token, \*, dispute_token) -> <a href="./src/lithic/types/dispute_evidence.py">DisputeEvidence</a></code>
- <code title="post /v1/disputes/{dispute_token}/evidences">client.disputes.<a href="./src/lithic/resources/disputes.py">initiate_evidence_upload</a>(dispute_token, \*\*<a href="src/lithic/types/dispute_initiate_evidence_upload_params.py">params</a>) -> <a href="./src/lithic/types/dispute_evidence.py">DisputeEvidence</a></code>
- <code title="get /v1/disputes/{dispute_token}/evidences">client.disputes.<a href="./src/lithic/resources/disputes.py">list_evidences</a>(dispute_token, \*\*<a href="src/lithic/types/dispute_list_evidences_params.py">params</a>) -> <a href="./src/lithic/types/dispute_evidence.py">SyncCursorPage[DisputeEvidence]</a></code>
- <code title="get /v1/disputes/{dispute_token}/evidences/{evidence_token}">client.disputes.<a href="./src/lithic/resources/disputes.py">retrieve_evidence</a>(evidence_token, \*, dispute_token) -> <a href="./src/lithic/types/dispute_evidence.py">DisputeEvidence</a></code>
- <code>client.disputes.<a href="./src/lithic/resources/disputes.py">upload_evidence</a>(\*args) -> None</code>

# Events

Types:

```python
from lithic.types import Event, EventSubscription, MessageAttempt
```

Methods:

- <code title="get /v1/events/{event_token}">client.events.<a href="./src/lithic/resources/events/events.py">retrieve</a>(event_token) -> <a href="./src/lithic/types/event.py">Event</a></code>
- <code title="get /v1/events">client.events.<a href="./src/lithic/resources/events/events.py">list</a>(\*\*<a href="src/lithic/types/event_list_params.py">params</a>) -> <a href="./src/lithic/types/event.py">SyncCursorPage[Event]</a></code>
- <code title="get /v1/events/{event_token}/attempts">client.events.<a href="./src/lithic/resources/events/events.py">list_attempts</a>(event_token, \*\*<a href="src/lithic/types/event_list_attempts_params.py">params</a>) -> <a href="./src/lithic/types/message_attempt.py">SyncCursorPage[MessageAttempt]</a></code>
- <code>client.events.<a href="./src/lithic/resources/events/events.py">resend</a>(\*args) -> None</code>

## Subscriptions

Types:

```python
from lithic.types.events import SubscriptionRetrieveSecretResponse
```

Methods:

- <code title="post /v1/event_subscriptions">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">create</a>(\*\*<a href="src/lithic/types/events/subscription_create_params.py">params</a>) -> <a href="./src/lithic/types/event_subscription.py">EventSubscription</a></code>
- <code title="get /v1/event_subscriptions/{event_subscription_token}">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">retrieve</a>(event_subscription_token) -> <a href="./src/lithic/types/event_subscription.py">EventSubscription</a></code>
- <code title="patch /v1/event_subscriptions/{event_subscription_token}">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">update</a>(event_subscription_token, \*\*<a href="src/lithic/types/events/subscription_update_params.py">params</a>) -> <a href="./src/lithic/types/event_subscription.py">EventSubscription</a></code>
- <code title="get /v1/event_subscriptions">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">list</a>(\*\*<a href="src/lithic/types/events/subscription_list_params.py">params</a>) -> <a href="./src/lithic/types/event_subscription.py">SyncCursorPage[EventSubscription]</a></code>
- <code title="delete /v1/event_subscriptions/{event_subscription_token}">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">delete</a>(event_subscription_token) -> None</code>
- <code title="get /v1/event_subscriptions/{event_subscription_token}/attempts">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">list_attempts</a>(event_subscription_token, \*\*<a href="src/lithic/types/events/subscription_list_attempts_params.py">params</a>) -> <a href="./src/lithic/types/message_attempt.py">SyncCursorPage[MessageAttempt]</a></code>
- <code title="post /v1/event_subscriptions/{event_subscription_token}/recover">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">recover</a>(event_subscription_token, \*\*<a href="src/lithic/types/events/subscription_recover_params.py">params</a>) -> None</code>
- <code title="post /v1/event_subscriptions/{event_subscription_token}/replay_missing">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">replay_missing</a>(event_subscription_token, \*\*<a href="src/lithic/types/events/subscription_replay_missing_params.py">params</a>) -> None</code>
- <code title="get /v1/event_subscriptions/{event_subscription_token}/secret">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">retrieve_secret</a>(event_subscription_token) -> <a href="./src/lithic/types/events/subscription_retrieve_secret_response.py">SubscriptionRetrieveSecretResponse</a></code>
- <code title="post /v1/event_subscriptions/{event_subscription_token}/secret/rotate">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">rotate_secret</a>(event_subscription_token) -> None</code>
- <code title="post /v1/simulate/event_subscriptions/{event_subscription_token}/send_example">client.events.subscriptions.<a href="./src/lithic/resources/events/subscriptions.py">send_simulated_example</a>(event_subscription_token, \*\*<a href="src/lithic/types/events/subscription_send_simulated_example_params.py">params</a>) -> None</code>

# FinancialAccounts

Types:

```python
from lithic.types import FinancialAccount, FinancialTransaction
```

Methods:

- <code title="post /v1/financial_accounts">client.financial_accounts.<a href="./src/lithic/resources/financial_accounts/financial_accounts.py">create</a>(\*\*<a href="src/lithic/types/financial_account_create_params.py">params</a>) -> <a href="./src/lithic/types/financial_account.py">FinancialAccount</a></code>
- <code title="get /v1/financial_accounts/{financial_account_token}">client.financial_accounts.<a href="./src/lithic/resources/financial_accounts/financial_accounts.py">retrieve</a>(financial_account_token) -> <a href="./src/lithic/types/financial_account.py">FinancialAccount</a></code>
- <code title="patch /v1/financial_accounts/{financial_account_token}">client.financial_accounts.<a href="./src/lithic/resources/financial_accounts/financial_accounts.py">update</a>(financial_account_token, \*\*<a href="src/lithic/types/financial_account_update_params.py">params</a>) -> <a href="./src/lithic/types/financial_account.py">FinancialAccount</a></code>
- <code title="get /v1/financial_accounts">client.financial_accounts.<a href="./src/lithic/resources/financial_accounts/financial_accounts.py">list</a>(\*\*<a href="src/lithic/types/financial_account_list_params.py">params</a>) -> <a href="./src/lithic/types/financial_account.py">SyncSinglePage[FinancialAccount]</a></code>
- <code title="post /v1/financial_accounts/{financial_account_token}/charge_off">client.financial_accounts.<a href="./src/lithic/resources/financial_accounts/financial_accounts.py">charge_off</a>(financial_account_token, \*\*<a href="src/lithic/types/financial_account_charge_off_params.py">params</a>) -> <a href="./src/lithic/types/financial_accounts/financial_account_credit_config.py">FinancialAccountCreditConfig</a></code>

## Balances

Types:

```python
from lithic.types.financial_accounts import BalanceListResponse
```

Methods:

- <code title="get /v1/financial_accounts/{financial_account_token}/balances">client.financial_accounts.balances.<a href="./src/lithic/resources/financial_accounts/balances.py">list</a>(financial_account_token, \*\*<a href="src/lithic/types/financial_accounts/balance_list_params.py">params</a>) -> <a href="./src/lithic/types/financial_accounts/balance_list_response.py">SyncSinglePage[BalanceListResponse]</a></code>

## FinancialTransactions

Methods:

- <code title="get /v1/financial_accounts/{financial_account_token}/financial_transactions/{financial_transaction_token}">client.financial_accounts.financial_transactions.<a href="./src/lithic/resources/financial_accounts/financial_transactions.py">retrieve</a>(financial_transaction_token, \*, financial_account_token) -> <a href="./src/lithic/types/financial_transaction.py">FinancialTransaction</a></code>
- <code title="get /v1/financial_accounts/{financial_account_token}/financial_transactions">client.financial_accounts.financial_transactions.<a href="./src/lithic/resources/financial_accounts/financial_transactions.py">list</a>(financial_account_token, \*\*<a href="src/lithic/types/financial_accounts/financial_transaction_list_params.py">params</a>) -> <a href="./src/lithic/types/financial_transaction.py">SyncSinglePage[FinancialTransaction]</a></code>

## CreditConfiguration

Types:

```python
from lithic.types.financial_accounts import FinancialAccountCreditConfig
```

Methods:

- <code title="get /v1/financial_accounts/{financial_account_token}/credit_configuration">client.financial_accounts.credit_configuration.<a href="./src/lithic/resources/financial_accounts/credit_configuration.py">retrieve</a>(financial_account_token) -> <a href="./src/lithic/types/financial_accounts/financial_account_credit_config.py">FinancialAccountCreditConfig</a></code>
- <code title="patch /v1/financial_accounts/{financial_account_token}/credit_configuration">client.financial_accounts.credit_configuration.<a href="./src/lithic/resources/financial_accounts/credit_configuration.py">update</a>(financial_account_token, \*\*<a href="src/lithic/types/financial_accounts/credit_configuration_update_params.py">params</a>) -> <a href="./src/lithic/types/financial_accounts/financial_account_credit_config.py">FinancialAccountCreditConfig</a></code>

## Statements

Types:

```python
from lithic.types.financial_accounts import Statement, Statements
```

Methods:

- <code title="get /v1/financial_accounts/{financial_account_token}/statements/{statement_token}">client.financial_accounts.statements.<a href="./src/lithic/resources/financial_accounts/statements/statements.py">retrieve</a>(statement_token, \*, financial_account_token) -> <a href="./src/lithic/types/financial_accounts/statement.py">Statement</a></code>
- <code title="get /v1/financial_accounts/{financial_account_token}/statements">client.financial_accounts.statements.<a href="./src/lithic/resources/financial_accounts/statements/statements.py">list</a>(financial_account_token, \*\*<a href="src/lithic/types/financial_accounts/statement_list_params.py">params</a>) -> <a href="./src/lithic/types/financial_accounts/statement.py">SyncCursorPage[Statement]</a></code>

### LineItems

Types:

```python
from lithic.types.financial_accounts.statements import StatementLineItems
```

Methods:

- <code title="get /v1/financial_accounts/{financial_account_token}/statements/{statement_token}/line_items">client.financial_accounts.statements.line_items.<a href="./src/lithic/resources/financial_accounts/statements/line_items.py">list</a>(statement_token, \*, financial_account_token, \*\*<a href="src/lithic/types/financial_accounts/statements/line_item_list_params.py">params</a>) -> SyncCursorPage[Data]</code>

## LoanTapes

Types:

```python
from lithic.types.financial_accounts import LoanTape
```

Methods:

- <code title="get /v1/financial_accounts/{financial_account_token}/loan_tapes/{loan_tape_token}">client.financial_accounts.loan_tapes.<a href="./src/lithic/resources/financial_accounts/loan_tapes.py">retrieve</a>(loan_tape_token, \*, financial_account_token) -> <a href="./src/lithic/types/financial_accounts/loan_tape.py">LoanTape</a></code>
- <code title="get /v1/financial_accounts/{financial_account_token}/loan_tapes">client.financial_accounts.loan_tapes.<a href="./src/lithic/resources/financial_accounts/loan_tapes.py">list</a>(financial_account_token, \*\*<a href="src/lithic/types/financial_accounts/loan_tape_list_params.py">params</a>) -> <a href="./src/lithic/types/financial_accounts/loan_tape.py">SyncCursorPage[LoanTape]</a></code>

# Transactions

Types:

```python
from lithic.types import (
    Transaction,
    TransactionSimulateAuthorizationResponse,
    TransactionSimulateAuthorizationAdviceResponse,
    TransactionSimulateClearingResponse,
    TransactionSimulateCreditAuthorizationResponse,
    TransactionSimulateReturnResponse,
    TransactionSimulateReturnReversalResponse,
    TransactionSimulateVoidResponse,
)
```

Methods:

- <code title="get /v1/transactions/{transaction_token}">client.transactions.<a href="./src/lithic/resources/transactions/transactions.py">retrieve</a>(transaction_token) -> <a href="./src/lithic/types/transaction.py">Transaction</a></code>
- <code title="get /v1/transactions">client.transactions.<a href="./src/lithic/resources/transactions/transactions.py">list</a>(\*\*<a href="src/lithic/types/transaction_list_params.py">params</a>) -> <a href="./src/lithic/types/transaction.py">SyncCursorPage[Transaction]</a></code>
- <code title="post /v1/simulate/authorize">client.transactions.<a href="./src/lithic/resources/transactions/transactions.py">simulate_authorization</a>(\*\*<a href="src/lithic/types/transaction_simulate_authorization_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_authorization_response.py">TransactionSimulateAuthorizationResponse</a></code>
- <code title="post /v1/simulate/authorization_advice">client.transactions.<a href="./src/lithic/resources/transactions/transactions.py">simulate_authorization_advice</a>(\*\*<a href="src/lithic/types/transaction_simulate_authorization_advice_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_authorization_advice_response.py">TransactionSimulateAuthorizationAdviceResponse</a></code>
- <code title="post /v1/simulate/clearing">client.transactions.<a href="./src/lithic/resources/transactions/transactions.py">simulate_clearing</a>(\*\*<a href="src/lithic/types/transaction_simulate_clearing_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_clearing_response.py">TransactionSimulateClearingResponse</a></code>
- <code title="post /v1/simulate/credit_authorization_advice">client.transactions.<a href="./src/lithic/resources/transactions/transactions.py">simulate_credit_authorization</a>(\*\*<a href="src/lithic/types/transaction_simulate_credit_authorization_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_credit_authorization_response.py">TransactionSimulateCreditAuthorizationResponse</a></code>
- <code title="post /v1/simulate/return">client.transactions.<a href="./src/lithic/resources/transactions/transactions.py">simulate_return</a>(\*\*<a href="src/lithic/types/transaction_simulate_return_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_return_response.py">TransactionSimulateReturnResponse</a></code>
- <code title="post /v1/simulate/return_reversal">client.transactions.<a href="./src/lithic/resources/transactions/transactions.py">simulate_return_reversal</a>(\*\*<a href="src/lithic/types/transaction_simulate_return_reversal_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_return_reversal_response.py">TransactionSimulateReturnReversalResponse</a></code>
- <code title="post /v1/simulate/void">client.transactions.<a href="./src/lithic/resources/transactions/transactions.py">simulate_void</a>(\*\*<a href="src/lithic/types/transaction_simulate_void_params.py">params</a>) -> <a href="./src/lithic/types/transaction_simulate_void_response.py">TransactionSimulateVoidResponse</a></code>

## EnhancedCommercialData

Types:

```python
from lithic.types.transactions import EnhancedCommercialDataRetrieveResponse
```

Methods:

- <code title="get /v1/transactions/{transaction_token}/enhanced_commercial_data">client.transactions.enhanced_commercial_data.<a href="./src/lithic/resources/transactions/enhanced_commercial_data.py">retrieve</a>(transaction_token) -> <a href="./src/lithic/types/transactions/enhanced_commercial_data_retrieve_response.py">EnhancedCommercialDataRetrieveResponse</a></code>

## Events

### EnhancedCommercialData

Types:

```python
from lithic.types.transactions.events import EnhancedData
```

Methods:

- <code title="get /v1/transactions/events/{event_token}/enhanced_commercial_data">client.transactions.events.enhanced_commercial_data.<a href="./src/lithic/resources/transactions/events/enhanced_commercial_data.py">retrieve</a>(event_token) -> <a href="./src/lithic/types/transactions/events/enhanced_data.py">EnhancedData</a></code>

# ResponderEndpoints

Types:

```python
from lithic.types import ResponderEndpointStatus, ResponderEndpointCreateResponse
```

Methods:

- <code title="post /v1/responder_endpoints">client.responder_endpoints.<a href="./src/lithic/resources/responder_endpoints.py">create</a>(\*\*<a href="src/lithic/types/responder_endpoint_create_params.py">params</a>) -> <a href="./src/lithic/types/responder_endpoint_create_response.py">ResponderEndpointCreateResponse</a></code>
- <code title="delete /v1/responder_endpoints">client.responder_endpoints.<a href="./src/lithic/resources/responder_endpoints.py">delete</a>(\*\*<a href="src/lithic/types/responder_endpoint_delete_params.py">params</a>) -> None</code>
- <code title="get /v1/responder_endpoints">client.responder_endpoints.<a href="./src/lithic/resources/responder_endpoints.py">check_status</a>(\*\*<a href="src/lithic/types/responder_endpoint_check_status_params.py">params</a>) -> <a href="./src/lithic/types/responder_endpoint_status.py">ResponderEndpointStatus</a></code>

# Webhooks

Methods:

- <code>client.webhooks.<a href="./src/lithic/resources/webhooks.py">unwrap</a>(\*args) -> object</code>
- <code>client.webhooks.<a href="./src/lithic/resources/webhooks.py">verify_signature</a>(\*args) -> None</code>

# ExternalBankAccounts

Types:

```python
from lithic.types import (
    ExternalBankAccountAddress,
    OwnerType,
    VerificationMethod,
    ExternalBankAccountCreateResponse,
    ExternalBankAccountRetrieveResponse,
    ExternalBankAccountUpdateResponse,
    ExternalBankAccountListResponse,
    ExternalBankAccountRetryMicroDepositsResponse,
    ExternalBankAccountRetryPrenoteResponse,
)
```

Methods:

- <code title="post /v1/external_bank_accounts">client.external_bank_accounts.<a href="./src/lithic/resources/external_bank_accounts/external_bank_accounts.py">create</a>(\*\*<a href="src/lithic/types/external_bank_account_create_params.py">params</a>) -> <a href="./src/lithic/types/external_bank_account_create_response.py">ExternalBankAccountCreateResponse</a></code>
- <code title="get /v1/external_bank_accounts/{external_bank_account_token}">client.external_bank_accounts.<a href="./src/lithic/resources/external_bank_accounts/external_bank_accounts.py">retrieve</a>(external_bank_account_token) -> <a href="./src/lithic/types/external_bank_account_retrieve_response.py">ExternalBankAccountRetrieveResponse</a></code>
- <code title="patch /v1/external_bank_accounts/{external_bank_account_token}">client.external_bank_accounts.<a href="./src/lithic/resources/external_bank_accounts/external_bank_accounts.py">update</a>(external_bank_account_token, \*\*<a href="src/lithic/types/external_bank_account_update_params.py">params</a>) -> <a href="./src/lithic/types/external_bank_account_update_response.py">ExternalBankAccountUpdateResponse</a></code>
- <code title="get /v1/external_bank_accounts">client.external_bank_accounts.<a href="./src/lithic/resources/external_bank_accounts/external_bank_accounts.py">list</a>(\*\*<a href="src/lithic/types/external_bank_account_list_params.py">params</a>) -> <a href="./src/lithic/types/external_bank_account_list_response.py">SyncCursorPage[ExternalBankAccountListResponse]</a></code>
- <code title="post /v1/external_bank_accounts/{external_bank_account_token}/retry_micro_deposits">client.external_bank_accounts.<a href="./src/lithic/resources/external_bank_accounts/external_bank_accounts.py">retry_micro_deposits</a>(external_bank_account_token, \*\*<a href="src/lithic/types/external_bank_account_retry_micro_deposits_params.py">params</a>) -> <a href="./src/lithic/types/external_bank_account_retry_micro_deposits_response.py">ExternalBankAccountRetryMicroDepositsResponse</a></code>
- <code title="post /v1/external_bank_accounts/{external_bank_account_token}/retry_prenote">client.external_bank_accounts.<a href="./src/lithic/resources/external_bank_accounts/external_bank_accounts.py">retry_prenote</a>(external_bank_account_token, \*\*<a href="src/lithic/types/external_bank_account_retry_prenote_params.py">params</a>) -> <a href="./src/lithic/types/external_bank_account_retry_prenote_response.py">ExternalBankAccountRetryPrenoteResponse</a></code>

## MicroDeposits

Types:

```python
from lithic.types.external_bank_accounts import MicroDepositCreateResponse
```

Methods:

- <code title="post /v1/external_bank_accounts/{external_bank_account_token}/micro_deposits">client.external_bank_accounts.micro_deposits.<a href="./src/lithic/resources/external_bank_accounts/micro_deposits.py">create</a>(external_bank_account_token, \*\*<a href="src/lithic/types/external_bank_accounts/micro_deposit_create_params.py">params</a>) -> <a href="./src/lithic/types/external_bank_accounts/micro_deposit_create_response.py">MicroDepositCreateResponse</a></code>

# Payments

Types:

```python
from lithic.types import (
    Payment,
    PaymentCreateResponse,
    PaymentRetryResponse,
    PaymentSimulateActionResponse,
    PaymentSimulateReceiptResponse,
    PaymentSimulateReleaseResponse,
    PaymentSimulateReturnResponse,
)
```

Methods:

- <code title="post /v1/payments">client.payments.<a href="./src/lithic/resources/payments.py">create</a>(\*\*<a href="src/lithic/types/payment_create_params.py">params</a>) -> <a href="./src/lithic/types/payment_create_response.py">PaymentCreateResponse</a></code>
- <code title="get /v1/payments/{payment_token}">client.payments.<a href="./src/lithic/resources/payments.py">retrieve</a>(payment_token) -> <a href="./src/lithic/types/payment.py">Payment</a></code>
- <code title="get /v1/payments">client.payments.<a href="./src/lithic/resources/payments.py">list</a>(\*\*<a href="src/lithic/types/payment_list_params.py">params</a>) -> <a href="./src/lithic/types/payment.py">SyncCursorPage[Payment]</a></code>
- <code title="post /v1/payments/{payment_token}/retry">client.payments.<a href="./src/lithic/resources/payments.py">retry</a>(payment_token) -> <a href="./src/lithic/types/payment_retry_response.py">PaymentRetryResponse</a></code>
- <code title="post /v1/simulate/payments/{payment_token}/action">client.payments.<a href="./src/lithic/resources/payments.py">simulate_action</a>(payment_token, \*\*<a href="src/lithic/types/payment_simulate_action_params.py">params</a>) -> <a href="./src/lithic/types/payment_simulate_action_response.py">PaymentSimulateActionResponse</a></code>
- <code title="post /v1/simulate/payments/receipt">client.payments.<a href="./src/lithic/resources/payments.py">simulate_receipt</a>(\*\*<a href="src/lithic/types/payment_simulate_receipt_params.py">params</a>) -> <a href="./src/lithic/types/payment_simulate_receipt_response.py">PaymentSimulateReceiptResponse</a></code>
- <code title="post /v1/simulate/payments/release">client.payments.<a href="./src/lithic/resources/payments.py">simulate_release</a>(\*\*<a href="src/lithic/types/payment_simulate_release_params.py">params</a>) -> <a href="./src/lithic/types/payment_simulate_release_response.py">PaymentSimulateReleaseResponse</a></code>
- <code title="post /v1/simulate/payments/return">client.payments.<a href="./src/lithic/resources/payments.py">simulate_return</a>(\*\*<a href="src/lithic/types/payment_simulate_return_params.py">params</a>) -> <a href="./src/lithic/types/payment_simulate_return_response.py">PaymentSimulateReturnResponse</a></code>

# ThreeDS

## Authentication

Types:

```python
from lithic.types.three_ds import AuthenticationRetrieveResponse, AuthenticationSimulateResponse
```

Methods:

- <code title="get /v1/three_ds_authentication/{three_ds_authentication_token}">client.three_ds.authentication.<a href="./src/lithic/resources/three_ds/authentication.py">retrieve</a>(three_ds_authentication_token) -> <a href="./src/lithic/types/three_ds/authentication_retrieve_response.py">AuthenticationRetrieveResponse</a></code>
- <code title="post /v1/three_ds_authentication/simulate">client.three_ds.authentication.<a href="./src/lithic/resources/three_ds/authentication.py">simulate</a>(\*\*<a href="src/lithic/types/three_ds/authentication_simulate_params.py">params</a>) -> <a href="./src/lithic/types/three_ds/authentication_simulate_response.py">AuthenticationSimulateResponse</a></code>
- <code title="post /v1/three_ds_decisioning/simulate/enter_otp">client.three_ds.authentication.<a href="./src/lithic/resources/three_ds/authentication.py">simulate_otp_entry</a>(\*\*<a href="src/lithic/types/three_ds/authentication_simulate_otp_entry_params.py">params</a>) -> None</code>

## Decisioning

Types:

```python
from lithic.types.three_ds import (
    ChallengeResponse,
    ChallengeResult,
    DecisioningRetrieveSecretResponse,
)
```

Methods:

- <code title="post /v1/three_ds_decisioning/challenge_response">client.three_ds.decisioning.<a href="./src/lithic/resources/three_ds/decisioning.py">challenge_response</a>(\*\*<a href="src/lithic/types/three_ds/decisioning_challenge_response_params.py">params</a>) -> None</code>
- <code title="get /v1/three_ds_decisioning/secret">client.three_ds.decisioning.<a href="./src/lithic/resources/three_ds/decisioning.py">retrieve_secret</a>() -> <a href="./src/lithic/types/three_ds/decisioning_retrieve_secret_response.py">DecisioningRetrieveSecretResponse</a></code>
- <code title="post /v1/three_ds_decisioning/secret/rotate">client.three_ds.decisioning.<a href="./src/lithic/resources/three_ds/decisioning.py">rotate_secret</a>() -> None</code>

# Reports

Types:

```python
from lithic.types import SettlementDetail, SettlementReport, SettlementSummaryDetails
```

## Settlement

Methods:

- <code title="get /v1/reports/settlement/details/{report_date}">client.reports.settlement.<a href="./src/lithic/resources/reports/settlement/settlement.py">list_details</a>(report_date, \*\*<a href="src/lithic/types/reports/settlement_list_details_params.py">params</a>) -> <a href="./src/lithic/types/settlement_detail.py">SyncCursorPage[SettlementDetail]</a></code>
- <code title="get /v1/reports/settlement/summary/{report_date}">client.reports.settlement.<a href="./src/lithic/resources/reports/settlement/settlement.py">summary</a>(report_date) -> <a href="./src/lithic/types/settlement_report.py">SettlementReport</a></code>

### NetworkTotals

Types:

```python
from lithic.types.reports.settlement import NetworkTotalRetrieveResponse, NetworkTotalListResponse
```

Methods:

- <code title="get /v1/reports/settlement/network_totals/{token}">client.reports.settlement.network_totals.<a href="./src/lithic/resources/reports/settlement/network_totals.py">retrieve</a>(token) -> <a href="./src/lithic/types/reports/settlement/network_total_retrieve_response.py">NetworkTotalRetrieveResponse</a></code>
- <code title="get /v1/reports/settlement/network_totals">client.reports.settlement.network_totals.<a href="./src/lithic/resources/reports/settlement/network_totals.py">list</a>(\*\*<a href="src/lithic/types/reports/settlement/network_total_list_params.py">params</a>) -> <a href="./src/lithic/types/reports/settlement/network_total_list_response.py">SyncCursorPage[NetworkTotalListResponse]</a></code>

# CardPrograms

Types:

```python
from lithic.types import CardProgram
```

Methods:

- <code title="get /v1/card_programs/{card_program_token}">client.card_programs.<a href="./src/lithic/resources/card_programs.py">retrieve</a>(card_program_token) -> <a href="./src/lithic/types/card_program.py">CardProgram</a></code>
- <code title="get /v1/card_programs">client.card_programs.<a href="./src/lithic/resources/card_programs.py">list</a>(\*\*<a href="src/lithic/types/card_program_list_params.py">params</a>) -> <a href="./src/lithic/types/card_program.py">SyncCursorPage[CardProgram]</a></code>

# DigitalCardArt

Types:

```python
from lithic.types import DigitalCardArt
```

Methods:

- <code title="get /v1/digital_card_art/{digital_card_art_token}">client.digital_card_art.<a href="./src/lithic/resources/digital_card_art.py">retrieve</a>(digital_card_art_token) -> <a href="./src/lithic/types/digital_card_art.py">DigitalCardArt</a></code>
- <code title="get /v1/digital_card_art">client.digital_card_art.<a href="./src/lithic/resources/digital_card_art.py">list</a>(\*\*<a href="src/lithic/types/digital_card_art_list_params.py">params</a>) -> <a href="./src/lithic/types/digital_card_art.py">SyncCursorPage[DigitalCardArt]</a></code>

# BookTransfers

Types:

```python
from lithic.types import BookTransferResponse
```

Methods:

- <code title="post /v1/book_transfers">client.book_transfers.<a href="./src/lithic/resources/book_transfers.py">create</a>(\*\*<a href="src/lithic/types/book_transfer_create_params.py">params</a>) -> <a href="./src/lithic/types/book_transfer_response.py">BookTransferResponse</a></code>
- <code title="get /v1/book_transfers/{book_transfer_token}">client.book_transfers.<a href="./src/lithic/resources/book_transfers.py">retrieve</a>(book_transfer_token) -> <a href="./src/lithic/types/book_transfer_response.py">BookTransferResponse</a></code>
- <code title="get /v1/book_transfers">client.book_transfers.<a href="./src/lithic/resources/book_transfers.py">list</a>(\*\*<a href="src/lithic/types/book_transfer_list_params.py">params</a>) -> <a href="./src/lithic/types/book_transfer_response.py">SyncCursorPage[BookTransferResponse]</a></code>
- <code title="post /v1/book_transfers/{book_transfer_token}/reverse">client.book_transfers.<a href="./src/lithic/resources/book_transfers.py">reverse</a>(book_transfer_token, \*\*<a href="src/lithic/types/book_transfer_reverse_params.py">params</a>) -> <a href="./src/lithic/types/book_transfer_response.py">BookTransferResponse</a></code>

# CreditProducts

## ExtendedCredit

Types:

```python
from lithic.types.credit_products import ExtendedCredit
```

Methods:

- <code title="get /v1/credit_products/{credit_product_token}/extended_credit">client.credit_products.extended_credit.<a href="./src/lithic/resources/credit_products/extended_credit.py">retrieve</a>(credit_product_token) -> <a href="./src/lithic/types/credit_products/extended_credit.py">ExtendedCredit</a></code>

## PrimeRates

Types:

```python
from lithic.types.credit_products import PrimeRateRetrieveResponse
```

Methods:

- <code title="post /v1/credit_products/{credit_product_token}/prime_rates">client.credit_products.prime_rates.<a href="./src/lithic/resources/credit_products/prime_rates.py">create</a>(credit_product_token, \*\*<a href="src/lithic/types/credit_products/prime_rate_create_params.py">params</a>) -> None</code>
- <code title="get /v1/credit_products/{credit_product_token}/prime_rates">client.credit_products.prime_rates.<a href="./src/lithic/resources/credit_products/prime_rates.py">retrieve</a>(credit_product_token, \*\*<a href="src/lithic/types/credit_products/prime_rate_retrieve_params.py">params</a>) -> <a href="./src/lithic/types/credit_products/prime_rate_retrieve_response.py">PrimeRateRetrieveResponse</a></code>

# ExternalPayments

Types:

```python
from lithic.types import ExternalPayment
```

Methods:

- <code title="post /v1/external_payments">client.external_payments.<a href="./src/lithic/resources/external_payments.py">create</a>(\*\*<a href="src/lithic/types/external_payment_create_params.py">params</a>) -> <a href="./src/lithic/types/external_payment.py">ExternalPayment</a></code>
- <code title="get /v1/external_payments/{external_payment_token}">client.external_payments.<a href="./src/lithic/resources/external_payments.py">retrieve</a>(external_payment_token) -> <a href="./src/lithic/types/external_payment.py">ExternalPayment</a></code>
- <code title="get /v1/external_payments">client.external_payments.<a href="./src/lithic/resources/external_payments.py">list</a>(\*\*<a href="src/lithic/types/external_payment_list_params.py">params</a>) -> <a href="./src/lithic/types/external_payment.py">SyncCursorPage[ExternalPayment]</a></code>
- <code title="post /v1/external_payments/{external_payment_token}/cancel">client.external_payments.<a href="./src/lithic/resources/external_payments.py">cancel</a>(external_payment_token, \*\*<a href="src/lithic/types/external_payment_cancel_params.py">params</a>) -> <a href="./src/lithic/types/external_payment.py">ExternalPayment</a></code>
- <code title="post /v1/external_payments/{external_payment_token}/release">client.external_payments.<a href="./src/lithic/resources/external_payments.py">release</a>(external_payment_token, \*\*<a href="src/lithic/types/external_payment_release_params.py">params</a>) -> <a href="./src/lithic/types/external_payment.py">ExternalPayment</a></code>
- <code title="post /v1/external_payments/{external_payment_token}/reverse">client.external_payments.<a href="./src/lithic/resources/external_payments.py">reverse</a>(external_payment_token, \*\*<a href="src/lithic/types/external_payment_reverse_params.py">params</a>) -> <a href="./src/lithic/types/external_payment.py">ExternalPayment</a></code>
- <code title="post /v1/external_payments/{external_payment_token}/settle">client.external_payments.<a href="./src/lithic/resources/external_payments.py">settle</a>(external_payment_token, \*\*<a href="src/lithic/types/external_payment_settle_params.py">params</a>) -> <a href="./src/lithic/types/external_payment.py">ExternalPayment</a></code>

# ManagementOperations

Types:

```python
from lithic.types import ManagementOperationTransaction
```

Methods:

- <code title="post /v1/management_operations">client.management_operations.<a href="./src/lithic/resources/management_operations.py">create</a>(\*\*<a href="src/lithic/types/management_operation_create_params.py">params</a>) -> <a href="./src/lithic/types/management_operation_transaction.py">ManagementOperationTransaction</a></code>
- <code title="get /v1/management_operations/{management_operation_token}">client.management_operations.<a href="./src/lithic/resources/management_operations.py">retrieve</a>(management_operation_token) -> <a href="./src/lithic/types/management_operation_transaction.py">ManagementOperationTransaction</a></code>
- <code title="get /v1/management_operations">client.management_operations.<a href="./src/lithic/resources/management_operations.py">list</a>(\*\*<a href="src/lithic/types/management_operation_list_params.py">params</a>) -> <a href="./src/lithic/types/management_operation_transaction.py">SyncCursorPage[ManagementOperationTransaction]</a></code>
- <code title="post /v1/management_operations/{management_operation_token}/reverse">client.management_operations.<a href="./src/lithic/resources/management_operations.py">reverse</a>(management_operation_token, \*\*<a href="src/lithic/types/management_operation_reverse_params.py">params</a>) -> <a href="./src/lithic/types/management_operation_transaction.py">ManagementOperationTransaction</a></code>
