import json
from typing import List


class JsonPathFinder:
    def __init__(self, json_str):
        self.data = json.loads(json_str)

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
            if key == target:
                yield current_path
            if isinstance(value, (dict, list)):
                yield from self.iter_node(value, current_path, target)

    def find_one(self, key: str) -> list:
        path_iter = self.iter_node(self.data, [], key)
        for path in path_iter:
            return path
        return []

    def find_all(self, key) -> List[list]:
        path_iter = self.iter_node(self.data, [], key)
        return list(path_iter)


if __name__ == '__main__':
    with open('sample.json', ) as f:
        json_data = f.read()
    finder = JsonPathFinder(json_data)
    path_list = finder.find_all('full_text')
    data = finder.data
    for path in path_list:
        print(path)