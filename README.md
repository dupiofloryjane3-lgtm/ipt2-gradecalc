# ipt2-gradecalc

A small grade calculator for IT 316 – Integrative Programming and Technologies 2.
It computes a final grade (30% prelim, 30% midterm, 40% finals) and a PASSED/FAILED remark.

<!-- Activity 3: paste your CI status badge on the next line -->
[![CI](https://github.com/dupiofloryjane3-lgtm/ipt2-gradecalc/actions/workflows/ci.yml/badge.svg)](https://github.com/dupiofloryjane3-lgtm/ipt2-gradecalc/actions/workflows/ci.yml)

## Team

Team description: Almira and Flory Jane are two IT students building a small, tested grade calculator with Git and CI.

| Role      | Name             | GitHub username        |
|-----------|------------------|------------------------|
| Partner A | Flory Jane Dupio | dupiofloryjane3-lgtm   |
| Partner B | Almira Durango   | durango1919almira-prog |
## How to run the tests

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -v --cov=grades --cov-report=term-missing
```
