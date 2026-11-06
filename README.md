# ipt2-gradecalc

A small grade calculator for IT 316 – Integrative Programming and Technologies 2.
It computes a final grade (30% prelim, 30% midterm, 40% finals) and a PASSED/FAILED remark.

<!-- Activity 3: paste your CI status badge on the next line -->


## Team

Team description: Flory Jane Dupio focuses on testing and quality checks for our grade calculator project.

| Role      | Name | GitHub username |
|-----------|------|-----------------|
| Partner A |      |                 |
| Partner B |      |                 |

## How to run the tests

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -v --cov=grades --cov-report=term-missing
```
