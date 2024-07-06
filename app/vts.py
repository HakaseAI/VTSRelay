
import pyvts
from pyvts import vts
from fastapi import FastAPI
from contextlib import asynccontextmanager

vts_obj: dict[str, vts] = {}
plugin_info = {
    "plugin_name": "VTSRelay",
    "developer": "zeroday0619",
    "authentication_token_path": "./token.txt"
}

@asynccontextmanager
async def vts_connection(app: FastAPI):
    vts_obj["vts"] = pyvts.vts(plugin_info=plugin_info)
    await vts_obj["vts"].connect()
    await vts_obj["vts"].request_authenticate_token()
    await vts_obj["vts"].request_authenticate()
    yield
    await vts_obj["vts"].close()
