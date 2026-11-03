PYTHON ?= python3

.PHONY: help register issues issues-check verify test

help:
	@printf '%s\n' \
	  'register      Regenerate docs/audit/ records and index from model/issues.json' \
	  'issues        Create missing GitHub issues and refresh all issue bodies' \
	  'issues-check  Verify the GitHub mirror against the register (requires gh auth)' \
	  'verify        Run local validation and the test suite' \
	  'test          Run the unittest suite'

register:
	$(PYTHON) scripts/build_issue_register.py

issues:
	$(PYTHON) scripts/sync_issues.py

issues-check:
	$(PYTHON) scripts/sync_issues.py --check

verify:
	$(PYTHON) tools/validate.py
	$(PYTHON) scripts/build_issue_register.py --check
	$(PYTHON) -m unittest discover -s tests -v

test:
	$(PYTHON) -m unittest discover -s tests -v
