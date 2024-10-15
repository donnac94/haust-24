def list_to_int_tuple(search_list):
    result = []
    for element in search_list:
        try:
            # Attempt to convert the element to an integer
            num = int(element)
            result.append(num)
        except ValueError:
            # Ignore elements that can't be converted
            continue
    return tuple(result)