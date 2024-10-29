# API Fetcher DAG

## Description

API Fetching Pipeline DAG for Airflow

API를 통한 비정형 데이터 수집 ~ 적재까지의 파이프라인 DAG 개발 / 테스트
~~사실 python 공부좀 하려고 하는거임~~
## Installation

- Python version : **3.10.12**
- Package Manager : UV
 <https://github.com/astral-sh/uv>

```bash

git clone https://github.com/yeoV/api-fetcher-dag.git
cd api-fetcher-dag

# If uv is not installed
pip install uv

# Create venv and Sync
uv sync 
```

## Usage

- Run code

```bash
uv run <code>
```

## Contributing

- Git Commit message setting

```bash
git config --local commit.template .github/.gitmessage.txt
```
