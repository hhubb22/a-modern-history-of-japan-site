UV ?= uv

.PHONY: sync serve build

sync:
	$(UV) run python scripts/sync_content.py

serve: sync
	$(UV) run mkdocs serve

build: sync
	$(UV) run mkdocs build
