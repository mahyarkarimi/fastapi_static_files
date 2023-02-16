import os
import stat

import anyio
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.datastructures import URL
from starlette.exceptions import HTTPException
from starlette.responses import FileResponse, RedirectResponse, Response
from starlette.types import Scope

templates_path = os.path.dirname(os.path.abspath(__file__)) + '/templates'
templates = Jinja2Templates(directory=templates_path)

class StaticIndexedFiles(StaticFiles):
    async def get_response(self, path: str, scope: Scope) -> Response:
        """
        Returns an HTTP response, given the incoming path, method and request headers.
        """
        if scope["method"] not in ("GET", "HEAD"):
            raise HTTPException(status_code=405)

        try:
            full_path, stat_result = await anyio.to_thread.run_sync(
                self.lookup_path, path
            )
        except PermissionError:
            raise HTTPException(status_code=401)
        except OSError:
            raise

        if stat_result and stat.S_ISREG(stat_result.st_mode):
            # We have a static file to serve.
            print('we have file')
            return self.file_response(full_path, stat_result, scope)

        elif stat_result and stat.S_ISDIR(stat_result.st_mode) and self.html:
            # We're in HTML mode, and have got a directory URL.
            # Check if we have 'index.html' file to serve.
            index_path = os.path.join(path, "index.html")
            full_path, stat_result = await anyio.to_thread.run_sync(
                self.lookup_path, index_path
            )
            if stat_result is not None and stat.S_ISREG(stat_result.st_mode):
                if not scope["path"].endswith("/"):
                    # Directory URLs should redirect to always end in "/".
                    url = URL(scope=scope)
                    url = url.replace(path=url.path + "/")
                    return RedirectResponse(url=url)
                return self.file_response(full_path, stat_result, scope)

        if self.html:
            # Check for '404.html' if we're in HTML mode.
            full_path, stat_result = await anyio.to_thread.run_sync(
                self.lookup_path, "404.html"
            )
            if stat_result and stat.S_ISREG(stat_result.st_mode):
                return FileResponse(
                    full_path,
                    stat_result=stat_result,
                    method=scope["method"],
                    status_code=404,
                )

        dirs = []
        files = []
        paths = os.listdir(full_path)
        for f in paths:
            if os.path.isdir(os.path.join(full_path, f)):
                dirs.append({'text': f, 'href': os.path.join(path, f)})
            else:
                files.append({'text': f, 'href': os.path.join(path, f)})
        relpath = '/' if path == '.' else os.path.join('/', path)
        return Response(content=templates.get_template('index.html').render(files=files, dirs=dirs, path=relpath))
