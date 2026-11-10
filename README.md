# AutomataLab — Input Validation Studio

A polished, interactive web showcase and Python test suite for the 21CSC301T Formal Language and Automata assessment.

## Live demo locally
Open `web/index.html` in any modern browser. No server, packages, or internet connection required.

## Three automata
- **Password policy:** 8–20 ASCII characters; at least one lowercase, uppercase, digit, and one of `!@#$%^&*`; no other symbols.
- **Email syntax:** restricted common email grammar with one `@`, valid local-part dot placement, at least two domain labels, and a final label of at least two letters.
- **ATM PIN:** exactly four ASCII digits; leading zeroes allowed.

## Python tests
Python 3.10+:
```bash
python -m unittest discover -s tests -v
```

## Repository layout
- `web/index.html` — interactive dashboard, no dependencies
- `automata/validators.py` — Python recognizers
- `tests/test_validators.py` — automated tests
- `report.md` — academic design note
- `diagrams/` — Mermaid automata diagrams

## GitHub Pages
To publish the interactive demo:
1. Push this repository to GitHub.
2. Open **Settings → Pages**.
3. Under Build and deployment, select **Deploy from a branch**.
4. Select `main` and `/ (root)` if you copy `web/index.html` to root as `index.html`, or choose `/web` if the Pages UI offers it.
5. Save and wait for the deployment URL.

Simplest setup: copy `web/index.html` to the repository root and name it `index.html`. Then choose `main` and `/ (root)`.

## Important limitations
This is a syntax/policy demonstration, not a production authentication system. Email validation is intentionally restricted and is not a full RFC parser. Real password and PIN verification require security controls, secure storage, account checks, and rate limiting. See `report.md`.

**SDG 9:** design-level alignment through structured, repeatable input validation as a foundational software reliability technique.
