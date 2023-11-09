    import numpy as np
    import json
    # load test split of AVDN dataset
    path_to_test = './test_unseen_data.json'
    test = json.load(open(path_to_test))
    
    inference_result = {}
    for i in range(len(test)):
        key = test[i]['map_name'] + '__' + test[i]['route_index']

        # Random a predicted trajectory with only two view areas
        center_1 = np.random.rand(2)*10 # (latitude, longitude)
        center_2 = np.random.rand(2)*10 # (latitude, longitude)

        # The two random view areas are represented by their four corners in the order of [bottem left corner, top left corner, top right corner, bottom right corner].
        inference_result[key] = {
            'path_corners': [
                [
                    [center_1[0] + 0.0003, center_1[1] - 0.0003],
                    [center_1[0] - 0.0003, center_1[1] - 0.0003],
                    [center_1[0] - 0.0003, center_1[1] + 0.0003],
                    [center_1[0] + 0.0003, center_1[1] + 0.0003],
                ],
                [
                    [center_2[0] + 0.0003, center_2[1] - 0.0003],
                    [center_2[0] - 0.0003, center_2[1] - 0.0003],
                    [center_2[0] - 0.0003, center_2[1] + 0.0003],
                    [center_2[0] + 0.0003, center_2[1] + 0.0003],
                ]
            ]
        }
    np.save('./output_inference_result', inference_result)
