# website

This repository includes a minimal Python project configured with pytest,
flake8, and black. Continuous integration runs on GitHub Actions.

## Development

Install the development dependencies and run tests:

```bash
pip install -r requirements.txt
black --check .
flake8 .
pytest
```
