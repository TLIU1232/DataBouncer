# DataBouncer

A lightweight privacy assistant that checks files before they are shared with AI tools.

Because "just upload the spreadsheet" is occasionally followed by a rather uncomfortable conversation.

---

## Overview

DataBouncer helps identify potentially sensitive information in CSV and Excel files before they are uploaded to AI services.

The workflow is intentionally simple:

1. Extract file metadata locally
2. Use an AI classifier to identify potentially sensitive columns
3. Replace sensitive values locally
4. Generate a safer copy of the original file

The original data is never sent to the classifier. Only the minimum metadata required for risk assessment is reviewed.

---

## Why?

AI assistants are becoming increasingly valuable for analysis, summarisation, coding, and automation.

Many organisations now provide approved AI solutions with appropriate security controls. However, employees may still use public AI services or unapproved tools when trying to solve a problem quickly.

A customer list, financial report, or internal document can leave the organisation with only a few clicks.

DataBouncer provides a small checkpoint before that happens.

Not because AI cannot be trusted, but because sometimes the person operating it needs a reminder.

---

## How It Works

```text
Input file
    |
    v
Extract column headers locally
    |
    v
Classify potentially sensitive fields
    |
    v
Anonymise sensitive values locally
    |
    v
Generate safer output file
```

The process separates:

- **Detection**: identifying what may be sensitive
- **Protection**: modifying data locally
- **Communication**: providing a risk summary

The classifier does not receive the underlying data values.

---

## Features

- Supports CSV and Excel files
- Extracts column headers without uploading file contents
- Identifies potentially sensitive fields using AI-assisted classification
- Anonymises sensitive columns locally
- Preserves file structure and relationships
- Maintains output format (`.csv` remains `.csv`, `.xlsx` remains `.xlsx`)
- Generates a security risk summary before AI usage

---

## Example

### Before

| customer_name | amount | department |
|---|---|---|
| John Smith | 1200 | Finance |

### After

| customer_name | amount | department |
|---|---|---|
| CUSTOMER_NAME_1 | 1200 | Finance |

Useful relationships remain intact. Unnecessary exposure does not.

---

## Installation

Clone the repository:

```bash
git clone <repository>
cd DataBouncer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

Run:

```bash
python main.py
```

---

## Project Structure

```text
DataBouncer/

├── main.py          # Application entry point
├── scanner.py       # File metadata extraction
├── classifier.py    # Sensitive field classification
├── anonymiser.py    # Local data transformation
├── roast.py         # Security feedback generator
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Privacy Design

DataBouncer follows a simple principle:

> Sensitive data should not leave the device just to ask whether it is sensitive.

The workflow only sends column-level metadata for classification.

Example:

Sent:

```json
{
  "columns": [
    "customer_name",
    "amount",
    "department"
  ]
}
```

Not sent:

```text
John Smith
1200
Finance
```

---

## Limitations

DataBouncer is designed as a lightweight safety checkpoint, not a complete data loss prevention system.

It does not replace:

- enterprise security controls
- approved AI governance policies
- access management
- employee training

It simply provides one additional moment of consideration before data goes somewhere it probably should not.

---

## Disclaimer

DataBouncer is a prototype designed to demonstrate safer AI adoption practices.

Please follow your organisation's security policies and approved AI usage guidelines.

The tool is designed to prevent avoidable mistakes. Unfortunately, the human element remains outside the scope of automation.