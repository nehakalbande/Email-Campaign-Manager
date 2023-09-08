# Email Campaign Manager

Email Campaign Manager is a Python-based web application built using the Django web framework. It allows you to manage subscribers, send email campaigns, and optimize the sending process using parallelization.

## Features

- Add subscribers with email and first name.
- Unsubscribe users by marking them as "inactive."
- Use the Django Admin interface to manage subscribers and campaigns.
- Send email campaigns with subjects, preview text, article URLs, HTML content, plain text content, and published dates.
- Optimize sending time using parallelization (Celery).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/email-campaign-manager.git
   cd email-campaign-manager

2. Access the Django Admin Interface:

  ```bash
   Open a web browser and go to http://127.0.0.1:8000/admin/ 
   ```

## Usage

   - Add subscribers: Use the ``` /campaign/add-subscriber/ ``` API endpoint or the Django Admin interface.
   - Unsubscribe users: Use the ``` /campaign/unsubscribe/<str:email>/ ``` API endpoint.
   - Send campaigns: Use the ``` /campaign/send-campaign/<int:campaign_id>/ ``` API endpoint (with a dummy function for now).
   - Manage subscribers and campaigns through the Django Admin interface.



