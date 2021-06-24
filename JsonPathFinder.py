import json
from typing import List


class JsonPathFinder:
    def __init__(self, json_str, mode='key'):
        self.data = json.loads(json_str)
        self.mode = mode

    def iter_node(self, rows, road_step, target):
        if isinstance(rows, dict):
            key_value_iter = (x for x in rows.items())
        elif isinstance(rows, list):
            key_value_iter = (x for x in enumerate(rows))
        else:
            return
        for key, value in key_value_iter:
            current_path = road_step.copy()
            current_path.append(key)
            if self.mode == 'key':
                check = key
            else:
                check = value
            if check == target:
                yield current_path
            if isinstance(value, (dict, list)):
                yield from self.iter_node(value, current_path, target)

    def find_one(self, target: str) -> list:
        path_iter = self.iter_node(self.data, [], target)
        for path in path_iter:
            return path
        return []

    def find_all(self, target) -> List[list]:
        path_iter = self.iter_node(self.data, [], target)
        return list(path_iter)


if __name__ == '__main__':
    import os
    jsonfile = os.path.join(os.path.dirname(__file__), 'sample.json')
    with open(jsonfile, ) as f:
        json_data = f.read()

    print('开始测试按 Key 搜索...')
    finder = JsonPathFinder(json_data)
    path_list = finder.find_all('full_text')
    data = finder.data
    for path in path_list:
        print(path)

    print('开始测试按 Value 搜索：...')

    # value_finder = JsonPathFinder(json_data, mode='value')
    # path_lits = value_finder.find_all(103)
    # for path in path_lits:
    #     print('path: ', path)
    #     value = json.loads(json_data)
    #     for step in path:
    #         value = value[step]
    #     assert value == 103
