# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .kyb_business_entity import KYBBusinessEntity
from .card_created_webhook_event import CardCreatedWebhookEvent
from .card_renewed_webhook_event import CardRenewedWebhookEvent
from .card_shipped_webhook_event import CardShippedWebhookEvent
from .card_reissued_webhook_event import CardReissuedWebhookEvent
from .card_converted_webhook_event import CardConvertedWebhookEvent
from .balance_updated_webhook_event import BalanceUpdatedWebhookEvent
from .dispute_updated_webhook_event import DisputeUpdatedWebhookEvent
from .loan_tape_created_webhook_event import LoanTapeCreatedWebhookEvent
from .loan_tape_updated_webhook_event import LoanTapeUpdatedWebhookEvent
from .statements_created_webhook_event import StatementsCreatedWebhookEvent
from .tokenization_result_webhook_event import TokenizationResultWebhookEvent
from .tokenization_updated_webhook_event import TokenizationUpdatedWebhookEvent
from .funding_event_created_webhook_event import FundingEventCreatedWebhookEvent
from .network_total_created_webhook_event import NetworkTotalCreatedWebhookEvent
from .network_total_updated_webhook_event import NetworkTotalUpdatedWebhookEvent
from .account_holder_created_webhook_event import AccountHolderCreatedWebhookEvent
from .card_transaction_updated_webhook_event import CardTransactionUpdatedWebhookEvent
from .external_payment_created_webhook_event import ExternalPaymentCreatedWebhookEvent
from .external_payment_updated_webhook_event import ExternalPaymentUpdatedWebhookEvent
from .financial_account_created_webhook_event import FinancialAccountCreatedWebhookEvent
from .financial_account_updated_webhook_event import FinancialAccountUpdatedWebhookEvent
from .settlement_report_updated_webhook_event import SettlementReportUpdatedWebhookEvent
from .account_holder_verification_webhook_event import AccountHolderVerificationWebhookEvent
from .dispute_transaction_created_webhook_event import DisputeTransactionCreatedWebhookEvent
from .dispute_transaction_updated_webhook_event import DisputeTransactionUpdatedWebhookEvent
from .payment_transaction_created_webhook_event import PaymentTransactionCreatedWebhookEvent
from .payment_transaction_updated_webhook_event import PaymentTransactionUpdatedWebhookEvent
from .internal_transaction_created_webhook_event import InternalTransactionCreatedWebhookEvent
from .internal_transaction_updated_webhook_event import InternalTransactionUpdatedWebhookEvent
from .management_operation_created_webhook_event import ManagementOperationCreatedWebhookEvent
from .management_operation_updated_webhook_event import ManagementOperationUpdatedWebhookEvent
from .external_bank_account_created_webhook_event import ExternalBankAccountCreatedWebhookEvent
from .external_bank_account_updated_webhook_event import ExternalBankAccountUpdatedWebhookEvent
from .tokenization_approval_request_webhook_event import TokenizationApprovalRequestWebhookEvent
from .dispute_evidence_upload_failed_webhook_event import DisputeEvidenceUploadFailedWebhookEvent
from .account_holder_document_updated_webhook_event import AccountHolderDocumentUpdatedWebhookEvent
from .three_ds_authentication_created_webhook_event import ThreeDSAuthenticationCreatedWebhookEvent
from .three_ds_authentication_updated_webhook_event import ThreeDSAuthenticationUpdatedWebhookEvent
from .tokenization_decisioning_request_webhook_event import TokenizationDecisioningRequestWebhookEvent
from .book_transfer_transaction_created_webhook_event import BookTransferTransactionCreatedWebhookEvent
from .book_transfer_transaction_updated_webhook_event import BookTransferTransactionUpdatedWebhookEvent
from .three_ds_authentication_challenge_webhook_event import ThreeDSAuthenticationChallengeWebhookEvent
from .auth_rules_backtest_report_created_webhook_event import AuthRulesBacktestReportCreatedWebhookEvent
from .digital_wallet_tokenization_result_webhook_event import DigitalWalletTokenizationResultWebhookEvent
from .card_authorization_approval_request_webhook_event import CardAuthorizationApprovalRequestWebhookEvent
from .digital_wallet_tokenization_updated_webhook_event import DigitalWalletTokenizationUpdatedWebhookEvent
from .card_transaction_enhanced_data_created_webhook_event import CardTransactionEnhancedDataCreatedWebhookEvent
from .card_transaction_enhanced_data_updated_webhook_event import CardTransactionEnhancedDataUpdatedWebhookEvent
from .three_ds_authentication_approval_request_webhook_event import ThreeDSAuthenticationApprovalRequestWebhookEvent
from .tokenization_two_factor_authentication_code_webhook_event import (
    TokenizationTwoFactorAuthenticationCodeWebhookEvent,
)
from .digital_wallet_tokenization_approval_request_webhook_event import (
    DigitalWalletTokenizationApprovalRequestWebhookEvent,
)
from .tokenization_two_factor_authentication_code_sent_webhook_event import (
    TokenizationTwoFactorAuthenticationCodeSentWebhookEvent,
)
from .digital_wallet_tokenization_two_factor_authentication_code_webhook_event import (
    DigitalWalletTokenizationTwoFactorAuthenticationCodeWebhookEvent,
)
from .digital_wallet_tokenization_two_factor_authentication_code_sent_webhook_event import (
    DigitalWalletTokenizationTwoFactorAuthenticationCodeSentWebhookEvent,
)

__all__ = [
    "ParsedWebhookEvent",
    "KYBPayload",
    "KYBPayloadUpdateRequest",
    "KYBPayloadUpdateRequestBeneficialOwnerIndividual",
    "KYBPayloadUpdateRequestBeneficialOwnerIndividualAddress",
    "KYBPayloadUpdateRequestControlPerson",
    "KYBPayloadUpdateRequestControlPersonAddress",
    "KYCPayload",
    "KYCPayloadUpdateRequest",
    "KYCPayloadUpdateRequestIndividual",
    "KYCPayloadUpdateRequestIndividualAddress",
    "LegacyPayload",
]


class KYBPayloadUpdateRequestBeneficialOwnerIndividualAddress(BaseModel):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: str
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: str
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""


class KYBPayloadUpdateRequestBeneficialOwnerIndividual(BaseModel):
    address: Optional[KYBPayloadUpdateRequestBeneficialOwnerIndividualAddress] = None
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Optional[str] = None
    """Individual's date of birth, as an RFC 3339 date."""

    email: Optional[str] = None
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Optional[str] = None
    """Individual's first name, as it appears on government-issued identity documents."""

    last_name: Optional[str] = None
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Optional[str] = None
    """Individual's phone number, entered in E.164 format."""


class KYBPayloadUpdateRequestControlPersonAddress(BaseModel):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: str
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: str
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""


class KYBPayloadUpdateRequestControlPerson(BaseModel):
    """
    An individual with significant responsibility for managing the legal entity (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating Officer, Managing Member, General Partner, President, Vice President, or Treasurer). This can be an executive, or someone who will have program-wide access to the cards that Lithic will provide. In some cases, this individual could also be a beneficial owner listed above. See [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf) (Section II) for more background.
    """

    address: Optional[KYBPayloadUpdateRequestControlPersonAddress] = None
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Optional[str] = None
    """Individual's date of birth, as an RFC 3339 date."""

    email: Optional[str] = None
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Optional[str] = None
    """Individual's first name, as it appears on government-issued identity documents."""

    last_name: Optional[str] = None
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Optional[str] = None
    """Individual's phone number, entered in E.164 format."""


class KYBPayloadUpdateRequest(BaseModel):
    """Original request to update the account holder."""

    beneficial_owner_entities: Optional[List[KYBBusinessEntity]] = None
    """Deprecated."""

    beneficial_owner_individuals: Optional[List[KYBPayloadUpdateRequestBeneficialOwnerIndividual]] = None
    """
    You must submit a list of all direct and indirect individuals with 25% or more
    ownership in the company. A maximum of 4 beneficial owners can be submitted. If
    no individual owns 25% of the company you do not need to send beneficial owner
    information. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section I) for more background on individuals that should be included.
    """

    business_entity: Optional[KYBBusinessEntity] = None
    """
    Information for business for which the account is being opened and KYB is being
    run.
    """

    control_person: Optional[KYBPayloadUpdateRequestControlPerson] = None
    """
    An individual with significant responsibility for managing the legal entity
    (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating
    Officer, Managing Member, General Partner, President, Vice President, or
    Treasurer). This can be an executive, or someone who will have program-wide
    access to the cards that Lithic will provide. In some cases, this individual
    could also be a beneficial owner listed above. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section II) for more background.
    """


class KYBPayload(BaseModel):
    """KYB payload for an updated account holder."""

    token: str
    """The token of the account_holder that was created."""

    update_request: KYBPayloadUpdateRequest
    """Original request to update the account holder."""

    event_type: Optional[Literal["account_holder.updated"]] = None
    """The type of event that occurred."""

    external_id: Optional[str] = None
    """
    A user provided id that can be used to link an account holder with an external
    system
    """

    nature_of_business: Optional[str] = None
    """
    Short description of the company's line of business (i.e., what does the company
    do?).
    """

    website_url: Optional[str] = None
    """Company website URL."""


class KYCPayloadUpdateRequestIndividualAddress(BaseModel):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: str
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: str
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""


class KYCPayloadUpdateRequestIndividual(BaseModel):
    """
    Information on the individual for whom the account is being opened and KYC is being run.
    """

    address: Optional[KYCPayloadUpdateRequestIndividualAddress] = None
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Optional[str] = None
    """Individual's date of birth, as an RFC 3339 date."""

    email: Optional[str] = None
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Optional[str] = None
    """Individual's first name, as it appears on government-issued identity documents."""

    last_name: Optional[str] = None
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Optional[str] = None
    """Individual's phone number, entered in E.164 format."""


class KYCPayloadUpdateRequest(BaseModel):
    """Original request to update the account holder."""

    individual: Optional[KYCPayloadUpdateRequestIndividual] = None
    """
    Information on the individual for whom the account is being opened and KYC is
    being run.
    """


class KYCPayload(BaseModel):
    """KYC payload for an updated account holder."""

    token: str
    """The token of the account_holder that was created."""

    update_request: KYCPayloadUpdateRequest
    """Original request to update the account holder."""

    event_type: Optional[Literal["account_holder.updated"]] = None
    """The type of event that occurred."""

    external_id: Optional[str] = None
    """
    A user provided id that can be used to link an account holder with an external
    system
    """


class LegacyPayload(BaseModel):
    """Legacy payload for an updated account holder."""

    token: str
    """The token of the account_holder that was created."""

    business_account_token: Optional[str] = None
    """
    If applicable, represents the business account token associated with the
    account_holder.
    """

    created: Optional[datetime] = None
    """When the account_holder updated event was created"""

    email: Optional[str] = None
    """
    If updated, the newly updated email associated with the account_holder otherwise
    the existing email is provided.
    """

    event_type: Optional[Literal["account_holder.updated"]] = None
    """The type of event that occurred."""

    external_id: Optional[str] = None
    """If applicable, represents the external_id associated with the account_holder."""

    first_name: Optional[str] = None
    """If applicable, represents the account_holder's first name."""

    last_name: Optional[str] = None
    """If applicable, represents the account_holder's last name."""

    legal_business_name: Optional[str] = None
    """If applicable, represents the account_holder's business name."""

    phone_number: Optional[str] = None
    """
    If updated, the newly updated phone_number associated with the account_holder
    otherwise the existing phone_number is provided.
    """


ParsedWebhookEvent: TypeAlias = Union[
    AccountHolderCreatedWebhookEvent,
    KYBPayload,
    KYCPayload,
    LegacyPayload,
    AccountHolderVerificationWebhookEvent,
    AccountHolderDocumentUpdatedWebhookEvent,
    CardAuthorizationApprovalRequestWebhookEvent,
    TokenizationDecisioningRequestWebhookEvent,
    AuthRulesBacktestReportCreatedWebhookEvent,
    BalanceUpdatedWebhookEvent,
    BookTransferTransactionCreatedWebhookEvent,
    BookTransferTransactionUpdatedWebhookEvent,
    CardCreatedWebhookEvent,
    CardConvertedWebhookEvent,
    CardRenewedWebhookEvent,
    CardReissuedWebhookEvent,
    CardShippedWebhookEvent,
    CardTransactionUpdatedWebhookEvent,
    CardTransactionEnhancedDataCreatedWebhookEvent,
    CardTransactionEnhancedDataUpdatedWebhookEvent,
    DigitalWalletTokenizationApprovalRequestWebhookEvent,
    DigitalWalletTokenizationResultWebhookEvent,
    DigitalWalletTokenizationTwoFactorAuthenticationCodeWebhookEvent,
    DigitalWalletTokenizationTwoFactorAuthenticationCodeSentWebhookEvent,
    DigitalWalletTokenizationUpdatedWebhookEvent,
    DisputeUpdatedWebhookEvent,
    DisputeEvidenceUploadFailedWebhookEvent,
    ExternalBankAccountCreatedWebhookEvent,
    ExternalBankAccountUpdatedWebhookEvent,
    ExternalPaymentCreatedWebhookEvent,
    ExternalPaymentUpdatedWebhookEvent,
    FinancialAccountCreatedWebhookEvent,
    FinancialAccountUpdatedWebhookEvent,
    FundingEventCreatedWebhookEvent,
    LoanTapeCreatedWebhookEvent,
    LoanTapeUpdatedWebhookEvent,
    ManagementOperationCreatedWebhookEvent,
    ManagementOperationUpdatedWebhookEvent,
    InternalTransactionCreatedWebhookEvent,
    InternalTransactionUpdatedWebhookEvent,
    NetworkTotalCreatedWebhookEvent,
    NetworkTotalUpdatedWebhookEvent,
    PaymentTransactionCreatedWebhookEvent,
    PaymentTransactionUpdatedWebhookEvent,
    SettlementReportUpdatedWebhookEvent,
    StatementsCreatedWebhookEvent,
    ThreeDSAuthenticationCreatedWebhookEvent,
    ThreeDSAuthenticationUpdatedWebhookEvent,
    ThreeDSAuthenticationChallengeWebhookEvent,
    TokenizationApprovalRequestWebhookEvent,
    TokenizationResultWebhookEvent,
    TokenizationTwoFactorAuthenticationCodeWebhookEvent,
    TokenizationTwoFactorAuthenticationCodeSentWebhookEvent,
    TokenizationUpdatedWebhookEvent,
    ThreeDSAuthenticationApprovalRequestWebhookEvent,
    DisputeTransactionCreatedWebhookEvent,
    DisputeTransactionUpdatedWebhookEvent,
]
