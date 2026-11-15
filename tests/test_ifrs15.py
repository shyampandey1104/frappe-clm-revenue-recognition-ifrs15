import unittest
from ifrs15.engine import IFRS15RevenueRecognitionEngine, MultiElementContract, PerformanceObligation

class TestIFRS15RevenueRecognition(unittest.TestCase):
    def test_multi_element_saas_contract_allocation(self):
        engine = IFRS15RevenueRecognitionEngine()

        # Contract bundled price: ₹12 Lakhs
        # Individual SSP: Software License = 8L, Implementation = 4L, AMC = 4L (Total SSP = 16L)
        contract = MultiElementContract(
            contract_id="CNT-SAAS-2026",
            customer_name="HDFC Securities",
            total_contract_price_billed=1200000.0,
            obligations=[
                PerformanceObligation(
                    obligation_id="PPO-01",
                    description="Software License",
                    standalone_selling_price_ssp=800000.0,
                    satisfaction_percentage=100.0 # Delivered upfront
                ),
                PerformanceObligation(
                    obligation_id="PPO-02",
                    description="Implementation Services",
                    standalone_selling_price_ssp=400000.0,
                    satisfaction_percentage=50.0  # Milestone halfway done
                ),
                PerformanceObligation(
                    obligation_id="PPO-03",
                    description="Annual Maintenance (AMC)",
                    standalone_selling_price_ssp=400000.0,
                    satisfaction_percentage=0.0   # Starts post-go-live
                )
            ]
        )

        rep = engine.compute_revenue_recognition(contract)
        # Ratio for PPO-01 = 8/16 = 50% -> Allocated 600,000 -> 100% satisfied = 600,000
        # Ratio for PPO-02 = 4/16 = 25% -> Allocated 300,000 -> 50% satisfied = 150,000
        # Ratio for PPO-03 = 4/16 = 25% -> Allocated 300,000 -> 0% satisfied = 0
        # Total Recognized = 750,000. Deferred Revenue Liability = 450,000.
        self.assertEqual(rep.total_recognized_revenue, 750000.0)
        self.assertEqual(rep.deferred_revenue_contract_liability, 450000.0)

if __name__ == "__main__":
    unittest.main()
