from openpyxl import Workbook

from Test.requests_util import RequestUtil
from Test.yaml_util import read_yaml

url = 'https://api.drumbeatsoft.com/process-engine-v3/field/query_data_page'
res = RequestUtil().send_all_request(method='post', url=url, headers=read_yaml('headers'), json=read_yaml('json')).json()

res_list = res['data']['rows']
export_field = ['procdef_name', 'start_account_name', 'starter_company_name', 'starter_dept_name', 'proc_inst_number', 'approve_state', 'current_activity_name', 'assignee_name',
                'start_time', 'end_time', 'proc_inst_id',
                '7', '6', '5', '4', '3', '2', '1']


outwb = Workbook()
outws = outwb.worksheets[0]
gauge_outfit = ['流程名称', '发起人名称', '发起公司', '发起部门', '单号', '审核状态', '审批位置', '审批人', '单据创建时间', '单据最终审核时间', '流程实例ID', '合计金额', '采购所属门店',
     '付款说明', '申请时间', '部门', '公司', '发起人']
outws.append(gauge_outfit)  # 先添加一行表头
# 遍历外层列表
for new_dict in res_list:
    a_list = []
    # 遍历内层每一个字典dict，把dict每一个值存入list
    for i in export_field:
        if i in new_dict.keys():
            a_list.append(new_dict[i])
        else:
            a_list.append('')

    # sheet直接append list即可
    outws.append(a_list)
outwb.save(r'test.xlsx')
print('数据存入excel成功')
