# Development Sandbox

Start CrateDB.
```shell
docker run --rm -it --name=cratedb \
  --publish=4200:4200 --publish=5432:5432 \
  --env=CRATE_HEAP_SIZE=2g crate:latest -Cdiscovery.type=single-node
```

Install Python package and project manager [uv].
```shell
{apt,brew,pip,zypper} install uv
```

Set up Python environment and install requirements.
```shell
uv venv --python=python3.12
uv pip install --upgrade -r requirements.txt -r requirements-dev.txt
```

Invoke linters and software tests.
```shell
source .venv/bin/activate
poe check
```

Run individual software tests.
```shell
pytest -k multi
pytest -k timeseries
pytest -k vector
```
