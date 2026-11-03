PYTHON ?= python3

.PHONY: help register review review-check issues issues-check verify test

help:
	@printf '%s\n' \
	  'register      Regenerate docs/audit/ records and index from model/issues.json' \
	  'review        Regenerate OPH/LFDI review records and indexes from reviews/oph-lfdi-57/model/review.json' \
	  'review-check  Verify generated OPH/LFDI review records and indexes without writing' \
	  'issues        Create missing GitHub issues and refresh all issue bodies' \
	  'issues-check  Verify the GitHub mirror against the register (requires gh auth)' \
	  'verify        Run local validation and the test suite' \
	  'test          Run the unittest suite'

register:
	$(PYTHON) scripts/build_issue_register.py

review:
	$(PYTHON) scripts/build_review_register.py

review-check:
	$(PYTHON) scripts/build_review_register.py --check

issues:
	$(PYTHON) scripts/sync_issues.py

issues-check:
	$(PYTHON) scripts/sync_issues.py --check

verify:
	$(PYTHON) tools/validate.py
	$(PYTHON) scripts/build_issue_register.py --check
	$(PYTHON) scripts/build_review_register.py --check
	$(PYTHON) -m unittest discover -s tests -v

test:
	$(PYTHON) -m unittest discover -s tests -v
