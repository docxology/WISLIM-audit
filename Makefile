PYTHON ?= python3

OPH_REPO ?= .oph
OPH_REF ?= origin/main

.PHONY: help register review review-check reply reply-check reply-issues reply-issues-check issues issues-check verify verify-oph oph-drift test

help:
	@printf '%s\n' \
	  'register      Regenerate docs/audit/ records and index from model/issues.json' \
	  'review        Regenerate OPH/LFDI review records and indexes from reviews/oph-lfdi-57/model/review.json' \
	  'review-check  Verify generated OPH/LFDI review records and indexes without writing' \
	  'reply         Regenerate the reply register, corrections, and correspondence ledger' \
	  'reply-check   Verify the reply register, corrections, and ledger without writing' \
	  'reply-issues  Create missing GitHub issues for the reply register and corrections' \
	  'reply-issues-check  Verify that GitHub mirror (requires gh auth)' \
	  'issues        Create missing GitHub issues and refresh all issue bodies' \
	  'issues-check  Verify the GitHub mirror against the register (requires gh auth)' \
	  'verify        Run local validation and the test suite' \
	  'verify-oph    Check every OPH quotation at the pinned commit (OPH_REPO=<clone>)' \
	  'oph-drift     List pinned OPH quotations that moved or vanished at OPH_REF (default origin/main)' \
	  'test          Run the unittest suite'

register:
	$(PYTHON) scripts/build_issue_register.py

review:
	$(PYTHON) scripts/build_review_register.py

review-check:
	$(PYTHON) scripts/build_review_register.py --check

reply:
	$(PYTHON) scripts/build_reply_register.py

reply-check:
	$(PYTHON) scripts/build_reply_register.py --check

reply-issues:
	$(PYTHON) scripts/sync_reply_issues.py

reply-issues-check:
	$(PYTHON) scripts/sync_reply_issues.py --check

issues:
	$(PYTHON) scripts/sync_issues.py

issues-check:
	$(PYTHON) scripts/sync_issues.py --check

verify:
	$(PYTHON) tools/validate.py
	$(PYTHON) scripts/build_issue_register.py --check
	$(PYTHON) scripts/build_review_register.py --check
	$(PYTHON) scripts/build_reply_register.py --check
	$(PYTHON) -m unittest discover -s tests -v

verify-oph:
	$(PYTHON) scripts/verify_oph_quotes.py --oph-repo "$(OPH_REPO)"

oph-drift:
	$(PYTHON) scripts/verify_oph_quotes.py --oph-repo "$(OPH_REPO)" --ref "$(OPH_REF)"

test:
	$(PYTHON) -m unittest discover -s tests -v
