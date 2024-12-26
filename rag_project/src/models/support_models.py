from dataclasses import dataclass, field
from typing import Optional

@dataclass
class SupportDependencies:
    """
    Represents dependencies for support-related operations.
    
    Attributes:
        customer_id (int): Unique identifier for the customer
        db (DatabaseConn): Database connection for customer information
    """
    customer_id: int
    db: Optional[object] = None  # Replace with actual DatabaseConn type

@dataclass
class SupportResult:
    """
    Represents the result of a support query or evaluation.
    
    Attributes:
        support_advice (str): Advice returned to the customer
        block_card (bool): Whether to block the customer's card
        risk (int): Risk level of query, ranging from 0 to 10
    """
    support_advice: str = field(default='')
    block_card: bool = field(default=False)
    risk: int = field(default=0, metadata={'description': 'Risk level of query', 'ge': 0, 'le': 10})

    def __post_init__(self):
        """
        Validate risk level after initialization.
        
        Raises:
            ValueError: If risk is not between 0 and 10
        """
        if not (0 <= self.risk <= 10):
            raise ValueError("Risk must be between 0 and 10")
