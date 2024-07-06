from app.vts import vts_obj
from fastapi import APIRouter


root = APIRouter(prefix="/v1")


@root.get("/hot_keys")
async def hot_keys():
    vts = vts_obj["vts"]
    response_data = await vts.request(vts.vts_request.requestHotKeyList())
    hotkey_list = []
    for hotkey in response_data['data']['availableHotkeys']:
        hotkey_list.append(hotkey['name'])
    return {
        "status": True,
        "data": hotkey_list
    }
