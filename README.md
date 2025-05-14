# FastAPI Static File Serving
[![](https://img.shields.io/github/license/mahyarkarimi/fastapi_static_files.svg?colorB=ff0000)](https://github.com/mahyarkarimi/fastapi_static_files/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/fastapi_static_files?logo=pypi)](https://pypi.org/project/fastapi_static_files/)
[![PyPI Downloads/month](https://static.pepy.tech/personalized-badge/fastapi_static_files?period=month&units=international_system&left_color=grey&right_color=blue&left_text=pypi%20downloads/month)](https://pepy.tech/project/jacoco-badge-generator)
[![PyPI Downloads/week](https://static.pepy.tech/personalized-badge/fastapi_static_files?period=week&units=international_system&left_color=grey&right_color=blue&left_text=pypi%20downloads/week)](https://pepy.tech/project/jacoco-badge-generator) 

## 📦 Installation

```
pip install fastapi_static_files
```

## 🔨 Usage

```python
from fastapi import FastAPI
from fastapi_static_files import StaticIndexedFiles
app = FastAPI()

app.mount('/public', StaticIndexedFiles(directory="./public"), name="static")
```

## 🔗 Links

- [Pypi Page](https://pypi.org/project/fastapi-static-files/0.1.0/)
