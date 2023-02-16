# FastAPI Static File Serving

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
