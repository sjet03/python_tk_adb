# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 12:23:14
# @Author  : lileilei 

# import xlsxwriter
# workbook = xlsxwriter.Workbook('chart.xlsx')
# worksheet = workbook.add_worksheet()
# chart = workbook.add_chart({'type': 'column'})
# data = [
#     [1, 2, 3, 4, 5],
#     [2, 4, 6, 8, 10],
#     [3, 6, 9, 12, 15],
# ]
# worksheet.write_column('A1', data[0])
# worksheet.write_column('B1', data[1])
# worksheet.write_column('C1', data[2])
# chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
# chart.add_series({'values': '=Sheet1!$C$1:$C$5'})
# worksheet.insert_chart('A7', chart)
# workbook.close()
# import xlsxwriter
# workbook = xlsxwriter.Workbook('chart_area.xlsx')
# worksheet = workbook.add_worksheet('ceshi')
# bold = workbook.add_format({'bold': 1})
# headings = ['Number', 'Batch 1', 'Batch 2']
# data = [
#     [2, 3, 4, 5, 6, 7],
#     [40, 40, 50, 30, 25, 50],
#     [30, 25, 30, 10, 5, 10],
# ]
# worksheet.write_row('A1', headings, bold)
# worksheet.write_column('A2', data[0])
# worksheet.write_column('B2', data[1])
# worksheet.write_column('C2', data[2])
# chart1 = workbook.add_chart({'type': 'area'})
# chart1.add_series({
#     'name':       '=ceshi!$B$1',
#     'categories': '=ceshi!$A$2:$A$7',
#     'values':     '=ceshi!$B$2:$B$7',
# })
# chart1.add_series({
#     'name':       ['ceshi', 0, 2],
#     'categories': ['ceshi', 1, 0, 6, 0],
#     'values':     ['ceshi', 1, 2, 6, 2],
# })
# chart1.set_title ({'name': 'Results of sample analysis'})
# chart1.set_x_axis({'name': 'Test number'})
# chart1.set_y_axis({'name': 'Sample length (mm)'})
# chart1.set_style(11)
# worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
# workbook.close()
import xlsxwriter
# workbook=xlsxwriter.Workbook('chart_bar.xlsx')
# worksheet=workbook.add_worksheet('daohang')
# bold = workbook.add_format({'bold': 1})
# headings = ['Number', 'Batch 1', 'Batch 2']
# data = [
#     [2, 3, 4, 5, 6, 7],
#     [10, 40, 50, 20, 10, 50],
#     [30, 60, 70, 50, 40, 30],
# ]
# worksheet.write_row('A1', headings, bold)
# worksheet.write_column('A2', data[0])
# worksheet.write_column('B2', data[1])
# worksheet.write_column('C2', data[2])
# chart1=workbook.add_chart({'type':'bar'})
# chart1.add_series({
#     'name':       '=daohang!$B$1',
#     'categories': '=daohang!$A$2:$A$7',
#     'values':     '=daohang!$B$2:$B$7',
# })
# chart1.add_series({
#     'name':       ['daohang', 0, 2],
#     'categories': ['daohang', 1, 0, 6, 0],
#     'values':     ['daohang', 1, 2, 6, 2],
# })
# chart1.set_title ({'name': 'Results of sample analysis'})
# chart1.set_x_axis({'name': 'Test number'})
# chart1.set_y_axis({'name': 'Sample length (mm)'})
# chart1.set_style(11)
# worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
# workbook=xlsxwriter.Workbook('chart_line.xlsx')
# worksheet=workbook.add_worksheet()
# bold = workbook.add_format({'bold': 1})
# headings = ['Number', 'Batch 1', 'Batch 2']
# data = [
#     [2, 3, 4, 5, 6, 7],
#     [10, 40, 50, 20, 10, 50],
#     [30, 60, 70, 50, 40, 30],
# ]
# worksheet.write_row('A1', headings, bold)
# worksheet.write_column('A2', data[0])
# worksheet.write_column('B2', data[1])
# worksheet.write_column('C2', data[2])
# chart1 = workbook.add_chart({'type': 'line'})
# chart1.add_series({
#     'name':       '=Sheet1!$B$1',
#     'categories': '=Sheet1!$A$2:$A$7',
#     'values':     '=Sheet1!$B$2:$B$7',
# })
# chart1.add_series({
#     'name':       ['Sheet1', 0, 2],
#     'categories': ['Sheet1', 1, 0, 6, 0],
#     'values':     ['Sheet1', 1, 2, 6, 2],
# })
# chart1.set_title ({'name': 'Results of sample analysis'})
# chart1.set_x_axis({'name': 'Test number'})
# chart1.set_y_axis({'name': 'Sample length (mm)'})
# chart1.set_style(10)
# worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
# workbook.close()
# workbook=xlsxwriter.Workbook('chart_pie.xlsx')
# worksheet=workbook.add_worksheet()
# bold=workbook.add_format({'bold':1})
# headings = ['Category', 'Values']
# data = [
#     ['Apple', 'Cherry', 'Pecan'],
#     [60, 30, 10],
# ]
# worksheet.write_row('A1', headings, bold)
# worksheet.write_column('A2', data[0])
# worksheet.write_column('B2', data[1])
# chart1 = workbook.add_chart({'type': 'pie'})
# chart1.add_series({
#     'name':       'Pie sales data',
#     'categories': ['Sheet1', 1, 0, 3, 0],
#     'values':     ['Sheet1', 1, 1, 3, 1],
# })
# chart1.set_title({'name': 'Popular Pie Types'})#圆柱
# chart1.set_style(10)
# worksheet.insert_chart('C2', chart1, {'x_offset': 25, 'y_offset': 10})
# workbook.close()
# workbook = xlsxwriter.Workbook('chart_scatter.xlsx')
# worksheet = workbook.add_worksheet()
# bold = workbook.add_format({'bold': 1})
# headings = ['上传流量', '下载流量', '总流量']
# data = [
#     [2, 3, 4, 5, 6, 7],
#     [10, 40, 50, 20, 10, 50],
#     [30, 60, 70, 50, 40, 30],
# ]
# worksheet.write_row('A1', headings, bold)
# worksheet.write_column('A2', data[0])
# worksheet.write_column('B2', data[1])
# worksheet.write_column('C2', data[2])
# chart1 = workbook.add_chart({'type': 'scatter',
#                              'subtype': 'straight_with_markers'})
# chart1.add_series({
#     'name': '=Sheet1!$B$1',
#     'categories': '=Sheet1!$A$2:$A$7',
#     'values': '=Sheet1!$B$2:$B$7',
# })
# chart1.add_series({
#     'name':       ['Sheet1', 0, 2],
#     'categories': ['Sheet1', 1, 0, 6, 0],
#     'values':     ['Sheet1', 1, 2, 6, 2],
# })
# chart1.set_title ({'name': '流量监测'})
# chart1.set_x_axis({'name': '测试次数'})
# chart1.set_y_axis({'name': '流量 (kb)'})
# chart1.set_style(11)
# worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
# workbook.close()
def qidongceshi(cishu,start):
	workbook=xlsxwriter.Workbook('启动时间测试结果.xlsx')
	worksheet=workbook.add_worksheet('time')
	bold=workbook.add_format({'bold':1})
	headings=['启动id','启动时间']
	data=[cishu,start]
	worksheet.write_row('A1',headings,bold)
	worksheet.write_column('A2',data[0])
	worksheet.write_column('B2',data[1])
	chart1 = workbook.add_chart({'type': 'scatter',
                            'subtype': 'straight_with_markers'})
	chart1.add_series({
		'name':'=time!$B$1',
		'categories': '=time!$A$2:$A$%s'%(len(start)+1),
    	'values': '=time!$B$2:$B$%s'%(len(start)+1),
		})
	chart1.set_title({'name':'启动监测'})
	chart1.set_x_axis({'name':"启动次数"})
	chart1.set_y_axis({'name':'花费时间:ms'})
	chart1.set_style(11)
	worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
	workbook.close()
def getcpu(cishu,start):
	workbook=xlsxwriter.Workbook('cpu_liu_men_report.xlsx')
	worksheet=workbook.add_worksheet('report')
	bold=workbook.add_format({'bold':1})
	headings=['次数','cpu占用率']
	data=[cishu,start]
	worksheet.write_row('A1',headings,bold)
	worksheet.write_column('A2',data[0])
	worksheet.write_column('B2',data[1])
	chart1 = workbook.add_chart({'type': 'scatter',
                            'subtype': 'straight_with_markers'})
	chart1.add_series({
		'name':'=report!$B$1',
		'categories': '=report!$A$2:$A$%s'%(len(start)+1),
    	'values': '=report!$B$2:$B$%s'%(len(start)+1),
		})
	chart1.set_title({'name':'cpu占用率'})
	chart1.set_x_axis({'name':"次数"})
	chart1.set_y_axis({'name':'占用:%'})
	chart1.set_style(11)
	worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
	workbook.close()


