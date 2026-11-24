# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "ifrs15"
app_title = "Frappe Clm Revenue Recognition Ifrs15"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Clm Revenue Recognition Ifrs15 - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/ifrs15/css/ifrs15.bundle.css"
app_include_js = "/assets/ifrs15/js/ifrs15.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Clm Revenue Recognition Ifrs15 Entry": {
        "validate": "ifrs15.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "ifrs15.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "ifrs15.tasks.hourly_sync"
    ],
    "daily": [
        "ifrs15.tasks.daily_reconciliation"
    ],
    "weekly": [
        "ifrs15.tasks.weekly_digest"
    ]
}
