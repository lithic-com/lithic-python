# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DecisioningSimulateChallengeResponse"]


class DecisioningSimulateChallengeResponse(BaseModel):
    token: Optional[str] = None
    """
    A unique token to reference this transaction with later calls to void or clear
    the authorization. This token is used in
    /v1/three_ds_decisioning/simulate/challenge_response to Approve or Decline the
    authentication
    """
