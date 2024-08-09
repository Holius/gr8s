# local

PHONY: locali i mt install-hooks

# use this command to have executing shell source
# eval $(make -s i)
locali:
	@echo ". .venv/bin/activate && pip install -e ."

i: pip3 install .

# manual tset
mt:
	python -m gr8s "--client-ca-file=/etc/kubernetes/pki/ca.crt --etcd-certfile=$$(pwd)/.local/cert.pem"

install-hooks:
	pip install pyright
	pip install pre-commit
	pre-commit install
	pre-commit run --all-files