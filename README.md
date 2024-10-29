# API Fetcher DAG

## Description

API Fetching Module for Airflow DAG

- API를 통한 비정형 데이터 수집 모듈 만들기 / 테스트
- ES, HDFS client 모듈화 하기 (안할지도)
- ~~사실 일하기 싫어서 python 공부나 하려고 하는거임~~

## Installation

- `Python version : 3.10.12`
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

### Mocking Server (temp)
[infra/mocking-server](https://github.com/yeoV/api-fetcher/tree/main/infra/mocking-server)
- 테스트용 Mocking server
- `go 1.23.2 `
- Using docker
```bash
# Image build
docker build -t mocking-server .

# container run
docker run -it -p 9000:9000 --name <name> mocking-server

# Test URL
curl localhost:9000/fake-data/3
```

## Usage

- Run code

```bash
uv run <code>
```

## Contributing
훈수, 조언 대환영.. issue 에 적어주세요

- Git Commit message setting

```bash
git config --local commit.template .github/.gitmessage.txt
```
