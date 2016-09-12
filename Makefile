run :
	@echo "**********************************"
	@echo "navigate to http://localhost:8000/"
	@echo "**********************************"
	jekyll serve --port 8000 || jekyll --server 8000

.PHONY: run
