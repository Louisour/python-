import  weather
import openpyxl
html=weather.get_html()#发请求，得响应结果
lst=weather.parse_html(html)#解析数据
workbook = openpyxl.Workbook()#创建一个excel
sheet=workbook.create_sheet('景区天气')
for item in lst:
    sheet.append(item)


workbook.save('景区天qi.xlsx')