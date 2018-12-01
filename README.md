# 2018agthon 農業開放資料處理

前置作業
# 安裝 Python 2 的 requests 模組
pip install requests

資料處理流程
- 匯入資料
- 資料處理
- 計量分析
- 依資料結果決定出貨地點與分級

產量 & 市場變數
- 取得全台小黃瓜拍賣價，依價格讀入

使用資料說明
https://data.coa.gov.tw/Query/ServiceDetail.aspx?id=037

資料介接 作物別：小黃瓜
http://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx?cropCode=fd1

get_data.py
