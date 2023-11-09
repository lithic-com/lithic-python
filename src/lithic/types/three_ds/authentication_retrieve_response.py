# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "AuthenticationRetrieveResponse",
    "Cardholder",
    "CardholderBillingAddress",
    "CardholderShippingAddress",
    "Merchant",
    "MerchantRiskIndicator",
    "AdditionalData",
    "App",
    "Browser",
    "Transaction",
]


class CardholderBillingAddress(BaseModel):
    address1: Optional[str] = None
    """First line of the street address provided by the cardholder."""

    address2: Optional[str] = None
    """Second line of the street address provided by the cardholder."""

    address3: Optional[str] = None
    """Third line of the street address provided by the cardholder."""

    city: Optional[str] = None
    """City of the address provided by the cardholder."""

    country: Optional[str] = None
    """
    Country of the address provided by the cardholder in ISO 3166-1 alpha-3 format
    (e.g. USA)
    """

    postal_code: Optional[str] = None
    """Postal code (e.g., ZIP code) of the address provided by the cardholder"""


class CardholderShippingAddress(BaseModel):
    address1: Optional[str] = None
    """First line of the street address provided by the cardholder."""

    address2: Optional[str] = None
    """Second line of the street address provided by the cardholder."""

    address3: Optional[str] = None
    """Third line of the street address provided by the cardholder."""

    city: Optional[str] = None
    """City of the address provided by the cardholder."""

    country: Optional[str] = None
    """
    Country of the address provided by the cardholder in ISO 3166-1 alpha-3 format
    (e.g. USA)
    """

    postal_code: Optional[str] = None
    """Postal code (e.g., ZIP code) of the address provided by the cardholder"""


class Cardholder(BaseModel):
    address_match: Optional[bool] = None
    """
    Indicates whether the shipping address and billing address provided by the
    cardholder are the same. This value - and assessment of whether the addresses
    match - is provided directly in the 3DS request and is not determined by Lithic.
    Maps to EMV 3DS field addrMatch.
    """

    billing_address: Optional[CardholderBillingAddress] = None
    """Object containing data on the billing address provided during the transaction."""

    email: Optional[str] = None
    """
    Email address that is either provided by the cardholder or is on file with the
    merchant in a 3RI request. Maps to EMV 3DS field email.
    """

    name: Optional[str] = None
    """Name of the cardholder. Maps to EMV 3DS field cardholderName."""

    phone_number_home: Optional[str] = None
    """Home phone number provided by the cardholder.

    Maps to EMV 3DS fields homePhone.cc and homePhone.subscriber.
    """

    phone_number_mobile: Optional[str] = None
    """Mobile/cell phone number provided by the cardholder.

    Maps to EMV 3DS fields mobilePhone.cc and mobilePhone.subscriber.
    """

    phone_number_work: Optional[str] = None
    """Work phone number provided by the cardholder.

    Maps to EMV 3DS fields workPhone.cc and workPhone.subscriber.
    """

    shipping_address: Optional[CardholderShippingAddress] = None
    """Object containing data on the shipping address provided during the transaction."""


class MerchantRiskIndicator(BaseModel):
    delivery_email_address: Optional[str] = None
    """
    In transactions with electronic delivery, email address to which merchandise is
    delivered. Maps to EMV 3DS field deliveryEmailAddress.
    """

    delivery_time_frame: Optional[
        Literal["ELECTRONIC_DELIVERY", "SAME_DAY_SHIPPING", "OVERNIGHT_SHIPPING", "TWO_DAY_OR_MORE_SHIPPING"]
    ] = None
    """The delivery time frame for the merchandise.

    Maps to EMV 3DS field deliveryTimeframe.
    """

    gift_card_amount: Optional[float] = None
    """
    In prepaid or gift card purchase transactions, purchase amount total in major
    units (e.g., a purchase of USD $205.10 would be 205). Maps to EMV 3DS field
    giftCardAmount.
    """

    gift_card_count: Optional[float] = None
    """
    In prepaid or gift card purchase transactions, count of individual prepaid or
    gift cards/codes purchased. Maps to EMV 3DS field giftCardCount.
    """

    gift_card_currency: Optional[str] = None
    """In prepaid or gift card purchase transactions, currency code of the gift card.

    Maps to EMV 3DS field giftCardCurr.
    """

    order_availability: Optional[Literal["MERCHANDISE_AVAILABLE", "FUTURE_AVAILABILITY"]] = None
    """
    Indicates whether the purchase is for merchandise that is available now or at a
    future date. Maps to EMV 3DS field preOrderPurchaseInd.
    """

    pre_order_available_date: Optional[datetime] = None
    """
    In pre-order purchase transactions, the expected date that the merchandise will
    be available. Maps to EMV 3DS field preOrderDate.
    """

    reorder_items: Optional[Literal["FIRST_TIME_ORDERED", "REORDERED"]] = None
    """Indicates whether the cardholder is reordering previously purchased merchandise.

    Maps to EMV 3DS field reorderItemsInd.
    """

    shipping_method: Optional[
        Literal[
            "SHIP_TO_BILLING_ADDRESS",
            "SHIP_TO_OTHER_VERIFIED_ADDRESS",
            "SHIP_TO_NON_BILLING_ADDRESS",
            "SHIP_TO_STORE",
            "DIGITAL_GOODS",
            "TRAVEL_AND_EVENT_TICKETS",
            "OTHER",
            "PICK_UP_AND_GO_DELIVERY",
            "LOCKER_DELIVERY",
        ]
    ] = None
    """Shipping method that the cardholder chose for the transaction.

    If purchase includes one or more item, this indicator is used for the physical
    goods; if the purchase only includes digital goods, this indicator is used to
    describe the most expensive item purchased. Maps to EMV 3DS field shipIndicator.
    """


class Merchant(BaseModel):
    id: str
    """Merchant identifier as assigned by the acquirer.

    Maps to EMV 3DS field acquirerMerchantId.
    """

    country: str
    """Country code of the merchant requesting 3DS authentication.

    Maps to EMV 3DS field merchantCountryCode.
    """

    mcc: str
    """
    Merchant category code assigned to the merchant that describes its business
    activity type. Maps to EMV 3DS field mcc.
    """

    name: str
    """Name of the merchant. Maps to EMV 3DS field merchantName."""

    risk_indicator: MerchantRiskIndicator
    """
    Object containing additional data indicating additional risk factors related to
    the e-commerce transaction.
    """


class AdditionalData(BaseModel):
    network_decision: Optional[Literal["LOW_RISK", "NOT_LOW_RISK"]] = None
    """
    Mastercard only: Indicates whether the network would have considered the
    authentication request to be low risk or not.
    """

    network_risk_score: Optional[float] = None
    """
    Mastercard only: Assessment by the network of the authentication risk level,
    with a higher value indicating a higher amount of risk.
    """


class App(BaseModel):
    device_info: Optional[str] = None
    """
    Device information gathered from the cardholder's device - JSON name/value pairs
    that is Base64url encoded. Maps to EMV 3DS field deviceInfo.
    """

    ip: Optional[str] = None
    """External IP address used by the app generating the 3DS authentication request.

    Maps to EMV 3DS field appIp.
    """


class Browser(BaseModel):
    ip: Optional[str] = None
    """
    IP address of the browser as returned by the HTTP headers to the 3DS requestor
    (e.g., merchant or digital wallet). Maps to EMV 3DS field browserIP.
    """

    java_enabled: Optional[bool] = None
    """Indicates whether the cardholder's browser has the ability to execute Java.

    Maps to EMV 3DS field browserJavaEnabled.
    """

    javascript_enabled: Optional[bool] = None
    """Indicates whether the cardholder's browser has the ability to execute
    JavaScript.

    Maps to EMV 3DS field browserJavascriptEnabled.
    """

    language: Optional[str] = None
    """Language of the cardholder's browser as defined in IETF BCP47.

    Maps to EMV 3DS field browserLanguage.
    """

    time_zone: Optional[str] = None
    """
    Time zone of the cardholder's browser offset in minutes between UTC and the
    cardholder browser's local time. The offset is positive if the local time is
    behind UTC and negative if it is ahead. Maps to EMV 3DS field browserTz.
    """

    user_agent: Optional[str] = None
    """Content of the HTTP user-agent header. Maps to EMV 3DS field browserUserAgent."""


class Transaction(BaseModel):
    amount: float
    """Amount of the purchase in minor units of currency with all punctuation removed.

    Maps to EMV 3DS field purchaseAmount.
    """

    currency: str
    """Currency of the purchase. Maps to EMV 3DS field purchaseCurrency."""

    currency_exponent: float
    """Minor units of currency, as specified in ISO 4217 currency exponent.

    Maps to EMV 3DS field purchaseExponent.
    """

    date_time: datetime
    """
    Date and time when the authentication was generated by the merchant/acquirer's
    3DS server. Maps to EMV 3DS field purchaseDate.
    """

    type: Optional[
        Literal[
            "GOODS_SERVICE_PURCHASE",
            "CHECK_ACCEPTANCE",
            "ACCOUNT_FUNDING",
            "QUASI_CASH_TRANSACTION",
            "PREPAID_ACTIVATION_AND_LOAD",
        ]
    ]
    """Type of the transaction for which a 3DS authentication request is occurring.

    Maps to EMV 3DS field transType.
    """


class AuthenticationRetrieveResponse(BaseModel):
    token: str
    """Globally unique identifier for the 3DS authentication."""

    account_type: Optional[Literal["NOT_APPLICABLE", "CREDIT", "DEBIT"]]
    """Type of account/card that is being used for the transaction.

    Maps to EMV 3DS field acctType.
    """

    authentication_result: Optional[Literal["SUCCESS", "DECLINE"]]
    """Indicates the outcome of the 3DS authentication process."""

    card_expiry_check: Literal["MATCH", "MISMATCH", "NOT_PRESENT"]
    """
    Indicates whether the expiration date provided by the cardholder during checkout
    matches Lithic's record of the card's expiration date.
    """

    card_token: str
    """
    Globally unique identifier for the card on which the 3DS authentication has
    occurred.
    """

    cardholder: Cardholder
    """Object containing data about the cardholder provided during the transaction."""

    channel: Literal["APP_BASED", "BROWSER", "THREE_DS_REQUESTOR_INITIATED"]
    """Channel in which the authentication occurs.

    Maps to EMV 3DS field deviceChannel.
    """

    created: datetime
    """Date and time when the authentication was created in Lithic's system."""

    decision_made_by: Optional[Literal["NETWORK", "LITHIC_DEFAULT", "LITHIC_RULES", "CUSTOMER_ENDPOINT", "UNKNOWN"]]
    """Entity that made the authentication decision."""

    merchant: Merchant
    """
    Object containing data about the merchant involved in the e-commerce
    transaction.
    """

    message_category: Literal["PAYMENT_AUTHENTICATION", "NON_PAYMENT_AUTHENTICATION"]
    """Either PAYMENT_AUTHENTICATION or NON_PAYMENT_AUTHENTICATION.

    For NON_PAYMENT_AUTHENTICATION, additional_data and transaction fields are not
    populated.
    """

    additional_data: Optional[AdditionalData] = None
    """
    Object containing additional data about the 3DS request that is beyond the EMV
    3DS standard spec (e.g., specific fields that only certain card networks send
    but are not required across all 3DS requests).
    """

    app: Optional[App] = None
    """Object containing data about the app used in the e-commerce transaction.

    Present if the channel is 'APP_BASED'.
    """

    authentication_request_type: Optional[
        Literal[
            "PAYMENT_TRANSACTION",
            "RECURRING_TRANSACTION",
            "INSTALLMENT_TRANSACTION",
            "ADD_CARD",
            "MAINTAIN_CARD",
            "EMV_TOKEN_CARDHOLDER_VERIFICATION",
            "BILLING_AGREEMENT",
            "SPLIT_SHIPMENT",
            "DELAYED_SHIPMENT",
            "SPLIT_PAYMENT",
        ]
    ] = None
    """
    Type of authentication request - i.e., the type of transaction or interaction is
    causing the merchant to request an authentication. Maps to EMV 3DS field
    threeDSRequestorAuthenticationInd.
    """

    browser: Optional[Browser] = None
    """Object containing data about the browser used in the e-commerce transaction.

    Present if the channel is 'BROWSER'.
    """

    three_ri_request_type: Optional[
        Literal[
            "RECURRING_TRANSACTION",
            "INSTALLMENT_TRANSACTION",
            "ADD_CARD",
            "MAINTAIN_CARD_INFO",
            "ACCOUNT_VERIFICATION",
            "SPLIT_SHIPMENT",
            "TOP_UP",
            "MAIL_ORDER",
            "TELEPHONE_ORDER",
            "TRUST_LIST_STATUS_CHECK",
            "OTHER_PAYMENT",
            "BILLING_AGREEMENT",
            "DEVICE_BINDING_STATUS_CHECK",
            "CARD_SECURITY_CODE_STATUS_CHECK",
            "DELAYED_SHIPMENT",
            "SPLIT_PAYMENT",
        ]
    ] = None
    """
    Type of 3DS Requestor Initiated (3RI) request i.e., a 3DS authentication that
    takes place at the initiation of the merchant rather than the cardholder. The
    most common example of this is where a merchant is authenticating before billing
    for a recurring transaction such as a pay TV subscription or a utility bill.
    Maps to EMV 3DS field threeRIInd.
    """

    transaction: Optional[Transaction] = None
    """
    Object containing data about the e-commerce transaction for which the merchant
    is requesting authentication.
    """
