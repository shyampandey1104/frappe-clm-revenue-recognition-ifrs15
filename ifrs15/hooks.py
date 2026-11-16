# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "ifrs15"
app_title = "Frappe Clm Revenue Recognition Ifrs15"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Clm Revenue Recognition Ifrs15 for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/ifrs15/css/ifrs15.bundle.css"
app_include_js = "/assets/ifrs15/js/ifrs15.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "ifrs15.engine.on_document_submit",
        "on_cancel": "ifrs15.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "ifrs15.engine.daily_scheduled_sync"
    ]
}
