# Frappe IFRS 15 / Ind AS 115 Revenue Recognition Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![IFRS](https://img.shields.io/badge/Accounting-IFRS%2015%20%2F%20Ind%20AS%20115-indigo.svg)](https://ifrs.org)

SaaS, EPC, and IT professional services companies face stringent audit scrutiny under IFRS 15 / Ind AS 115. Bundled software licenses and multi-year services cannot be recognized upon billing.

## Core Capabilities
- **5-Step Model Compliance:** Evaluates customer contracts, identifies distinct performance obligations, and allocates transaction prices based on Standalone Selling Price (SSP) ratios.
- **Contract Asset vs Liability:** Automatically calculates Deferred Revenue (Contract Liability) and Unbilled Work-in-Progress (Contract Asset).
- **Audit Schedules:** Produces GAAP-compliant amortization schedules for Big-4 statutory audits.

## Tests
```bash
python3 -m unittest discover tests
```
