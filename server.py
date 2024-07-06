__version__ = '0.1.0'

import uvicorn

from app.config import get_config
from app.vts import vts_connection
from apis import root
from fastapi import FastAPI

app = FastAPI(
    title="VTSRelay",
    description="VTube Studio API over REST API",
    version=__version__,
    lifespan=vts_connection
)

if __name__ == '__main__':
    app.include_router(router=root, prefix="/api")
    config = get_config()
    try:
        host, port = config['host'], config['port']
    except KeyError:
        raise KeyError('host and port must be defined in config')
    uvicorn.run(app, host=host, port=port)