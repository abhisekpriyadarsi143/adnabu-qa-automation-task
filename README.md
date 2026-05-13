# AdNabu QA Automation — Quality Assurance Engineer Assignment

## Overview

Selenium + Python test suite for [AdNabuTestStore](https://adnabuteststore.myshopify.com) covering:

- **Task 1**: Manual test cases for Product Search and Add to Cart
- **Task 2**: Automated end-to-end scenario — Search for a product → Select it → Add to Cart

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Test language |
| Selenium 4.x | Browser automation |
| pytest | Test runner |
| pytest-html | HTML reports |
| webdriver-manager | Auto-manages ChromeDriver |

---

## Folder Structure

```
adnabu-qa/
├── README.md
├── .gitignore
├── requirements.txt
├── pytest.ini
├── conftest.py                  # Fixtures (driver setup/teardown)
│
├── config/
│   └── settings.py              # Base URL, credentials, timeouts
│
├── pages/                       # Page Object Model
│   ├── __init__.py
│   ├── base_page.py             # Shared helpers (wait, click, type)
│   ├── home_page.py             # Search bar interactions
│   ├── search_results_page.py   # Product listing & selection
│   ├── product_page.py          # Product detail + Add to Cart
│   └── cart_page.py             # Cart assertions
│
├── tests/
│   ├── __init__.py
│   ├── test_product_search.py   # TC-S01 → TC-S06 (Search test cases)
│   └── test_add_to_cart.py      # TC-C01 → TC-C06 (Cart test cases)
│
├── test_cases/
│   └── manual_test_cases.md     # All 12 manual test cases (Task 1)
│
└── reports/                     # Auto-generated pytest-html reports
    └── .gitkeep
```

---

## Setup

```bash
# 1. Clone the repo
git clone <repo-url>
cd adnabu-qa

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Running Tests

```bash
# Run all tests
pytest

# Run only automation scenario (Task 2)
pytest tests/test_product_search.py::test_search_and_add_to_cart -v

# Run with HTML report
pytest --html=reports/report.html --self-contained-html

# Run specific test case
pytest -k "test_search_valid_product" -v
```

---

## Store Credentials

- **Store URL**: https://adnabuteststore.myshopify.com
- **Password**: `AdNabuQA`

> Store is password-protected. The `conftest.py` handles login automatically.

---

## Key Design Decisions

- **No hardcoded sleeps** — all waits use `WebDriverWait` with `ExpectedConditions`
- **Page Object Model** — each page is a class; tests never call Selenium directly
- **Modular fixtures** — driver lifecycle managed in `conftest.py`
- **Assertions are explicit** — every test has clear `assert` statements with messages
