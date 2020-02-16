import timeit
import json
import copy

import ujson
import msgpack

from Yurii_Khomych.l_1_functions.hw_start import insights as dataset

if __name__ == "__main__":
    print("copy.deepcopy(dataset)")
    print(
        timeit.timeit(
            "copy.deepcopy(dataset)",
            setup="from __main__ import copy, dataset",
            number=100,
        )
    )
    print("json.loads(json.dumps(dataset))")
    print(
        timeit.timeit(
            "json.loads(json.dumps(dataset))",
            setup="from __main__ import json, dataset",
            number=100,
        )
    )
    print("ujson.loads(ujson.dumps(dataset))")
    print(
        timeit.timeit(
            "ujson.loads(ujson.dumps(dataset))",
            setup="from __main__ import ujson, dataset",
            number=100,
        )
    )
    print("msgpack.unpackb(msgpack.packb(dataset))")
    print(
        timeit.timeit(
            "msgpack.unpackb(msgpack.packb(dataset))",
            setup="from __main__ import msgpack, dataset",
            number=100,
        )
    )
