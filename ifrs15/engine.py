"""IFRS 15 / Ind AS 115 5-Step Performance Obligation Revenue Recognition Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class PerformanceObligation:
    obligation_id: str
    description: str
    standalone_selling_price_ssp: float
    allocated_transaction_price: float = 0.0
    is_satisfied: bool = False
    satisfaction_percentage: float = 0.0  # 0 to 100%


@dataclass
class MultiElementContract:
    contract_id: str
    customer_name: str
    total_contract_price_billed: float
    obligations: List[PerformanceObligation]


@dataclass
class RevenueRecognitionReport:
    contract_id: str
    total_billed_price: float
    total_recognized_revenue: float
    deferred_revenue_contract_liability: float
    unbilled_revenue_contract_asset: float
    line_item_allocations: List[Dict[str, Any]]


class IFRS15RevenueRecognitionEngine:
    """Implements the mandatory 5-step IFRS 15 / Ind AS 115 revenue model for multi-element enterprise contracts."""

    def allocate_transaction_price(self, contract: MultiElementContract):
        total_ssp = sum(o.standalone_selling_price_ssp for o in contract.obligations)
        if total_ssp <= 0:
            raise ValueError("Total Standalone Selling Price must be positive.")

        # Step 4: Allocate transaction price based on relative standalone selling prices
        for o in contract.obligations:
            ratio = o.standalone_selling_price_ssp / total_ssp
            o.allocated_transaction_price = round(contract.total_contract_price_billed * ratio, 2)

    def compute_revenue_recognition(
        self,
        contract: MultiElementContract
    ) -> RevenueRecognitionReport:
        self.allocate_transaction_price(contract)

        recognized_total = 0.0
        line_items = []

        for o in contract.obligations:
            earned = round((o.allocated_transaction_price * o.satisfaction_percentage) / 100.0, 2)
            recognized_total += earned
            line_items.append({
                "obligation_id": o.obligation_id,
                "description": o.description,
                "ssp": o.standalone_selling_price_ssp,
                "allocated_price": o.allocated_transaction_price,
                "satisfaction_pct": o.satisfaction_percentage,
                "recognized_revenue": earned
            })

        recognized_total = round(recognized_total, 2)
        deferred_revenue = max(0.0, round(contract.total_contract_price_billed - recognized_total, 2))
        unbilled_asset = max(0.0, round(recognized_total - contract.total_contract_price_billed, 2))

        return RevenueRecognitionReport(
            contract_id=contract.contract_id,
            total_billed_price=contract.total_contract_price_billed,
            total_recognized_revenue=recognized_total,
            deferred_revenue_contract_liability=deferred_revenue,
            unbilled_revenue_contract_asset=unbilled_asset,
            line_item_allocations=line_items
        )
