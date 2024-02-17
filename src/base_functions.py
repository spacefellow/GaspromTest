def get_min(
        data: list,
        param: str
):
    result = float("inf")
    for elem in data:
        result = min(elem[param], result)
    return result


def get_max(
        data: list,
        param: str
):
    result = float("-inf")
    for elem in data:
        result = max(elem[param], result)
    return result


def get_sum(
        data: list,
        param: str
):
    result = 0
    for elem in data:
        result += elem[param]
    return result


def get_mean(
        data: list,
        param: str
):
    sorted_params = sorted([el[param] for el in data])
    n = len(sorted_params)
    if n % 2 == 0:
        return (sorted_params[n // 2] + sorted_params[n // 2 - 1]) / 2
    else:
        return sorted_params[n // 2]


def model_to_dict(list_of_devices):
    result = [
        dict(
            id=device.id,
            x=device.x,
            y=device.y,
            z=device.z,
            created_at=device.created_at
        ) for device in list_of_devices
    ]
    return result


def aggregate_data(data: list):
    result = {
        'min_x': get_min(data, 'x'),
        'min_y': get_min(data, 'y'),
        'min_z': get_min(data, 'z'),
        'max_x': get_max(data, 'x'),
        'max_y': get_max(data, 'y'),
        'max_z': get_max(data, 'z'),
        'sum_x': get_sum(data, 'x'),
        'sum_y': get_sum(data, 'y'),
        'sum_z': get_sum(data, 'z'),
        'mean_x': get_mean(data, 'x'),
        'mean_y': get_mean(data, 'y'),
        'mean_z': get_mean(data, 'z'),
        'amount': len(data)
    }
    return result
