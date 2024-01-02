# kkbox1227

## 作業說明

- src/kkbox1227/api: Re-implement of:
  - def get_access_token() 取得 access_token
  - kkbox_charts1.py --> def get_charts() 取得排行榜歌單
  - kkbox_charts3.py --> def get_charts_tracks(chart_id) 搜尋歌單
- src/kkbox1227/crud: Re-implement of:
  - kkbox 串接mysql Workbench 新增
  - kkbox 串接mysql Workbench 查詢
  - kkbox 串接mysql Workbench 修改
  - kkbox 串接mysql Workbench 刪除

## Run example

```bash
KKBOX_CLIENT_ID="..." KKBOX_CLIENT_SECRET="..." rye run uvicorn --reload kkbox1227.api:app

KKBOX_CLIENT_ID="..." KKBOX_CLIENT_SECRET="..." DATABASE_URL="mysql+pymysql://localhost:[password]@localhost/yourdb" rye run uvicorn --reload kkbox1227.crud:app
```
