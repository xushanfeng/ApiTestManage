import types

from . import api
import json
from flask import jsonify, request
from ..util.tool_func import *
from app.models import *


@api.route('/buildIdentity')
def build_identity():
    identity_data = ''.join([b + '\n' for b in list(set([identity_generator() for j in range(100)]))])
    return jsonify({'data': identity_data, 'status': 1})
    # identity_data = [{'identity': b} for b in list(set([identity_generator() for j in range(100)]))]
    # return jsonify({'data': identity_data, 'status': 1, 'title': ['身份证']})


@api.route('/delSql', methods=['POST'])
def del_sql():
    a = ApiMsg.query.all()
    for a1 in a:
        project_id = Module.query.filter_by(id=a1.module_id).first().project_id
        a1.project_id = project_id
        db.session.commit()

    return jsonify({'msg': '修改完成', 'status': 1})


def is_function(tup):
    """ Takes (name, object) tuple, returns True if it is a function.
    """
    name, item = tup
    return isinstance(item, types.FunctionType)


@api.route('/runCmd', methods=['POST'])
def run_cmd():
    import importlib

    data = request.json
    name = data.get('funcName')
    import_path = 'func_list.build_in_func'
    func_list = importlib.reload(importlib.import_module(import_path))
    module_functions_dict = dict(filter(is_function, vars(func_list).items()))
    module_functions_dict[name]()

    return jsonify({'msg': '完成', 'status': 1})
    # identity_data = [{'identity': b} for b in list(set([identity_generator() for j in range(100)]))]
    # return jsonify({'data': identity_data, 'status': 1, 'title': ['身份证']})


@api.route('/optimizeError', methods=['POST'])
def optimize_error_data():

    data = request.json
    error_data = data.get('errorData')
    new_data = '\n'.join(error_data.split('↵'))
    # data = request.json
    # _data = data.get('dictData')
    # test = json.loads(_data)
    # d = TraverseDict()
    # d.get_dict_keys_path(test)
    # d.data_tidy(test)
    # d.get_dict_keys_path(test)
    # d.data_tidy(test)
    return jsonify({'status': 1, 'msg': '优化成功', 'data': new_data})


@api.route('/optimizeErrorData', methods=['POST'])
def deal_data():

    data1 = CaseData.query.all()
    for d in data1:
        d.time = 1
        db.session.commit()
    # data = request.json
    # _data = data.get('dictData')
    # test = json.loads(_data)
    # d = TraverseDict()
    # d.get_dict_keys_path(test)
    # d.data_tidy(test)
    # d.get_dict_keys_path(test)
    # d.data_tidy(test)
    return jsonify({'status': 1, 'msg': '优化成功'})


@api.route('/findSqlList')
def find_sql_list():
    import psycopg2

    # database="xiangrikui_production"
    conn = psycopg2.connect(database="team_test", user="xrkadmin", password="xrktest@2016", host="192.168.6.222",
                            port="5432")
    cur = conn.cursor()
    # cur.execute("""SELECT * FROM "xrk_bss"."follows" WHERE maturity='4';""")

    cur.execute("""SELECT * FROM "xrk_bss"."agents" WHERE name='袁一一';""")
    rows = cur.fetchall()
    title_data = [desc[0] for desc in cur.description]
    # sql_list = [{title_data[num]: _row} for row in rows for num, _row in enumerate(row)]
    sql_data = []
    for row in rows:
        _data = {}
        for num, _row in enumerate(row):
            _data[title_data[num]] = _row
        sql_data.append(_data.copy())

    # for row in rows:
    #     print(row)
    conn.close()
    return jsonify({'sql_data': sql_data, 'status': 1, 'title_data': title_data})
