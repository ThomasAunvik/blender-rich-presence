def enumItemsFromList(itemData):
    """
    Create an enumerated tuple from item data.
    :param itemData: (_id, name)
    :type itemData: tuple(int, string)
    :return: items
    :rtype: list
    """
    items = []
    for _id, element in enumerate(itemData):
        items.append((element, element, "", "NONE", _id))
    if len(items) == 0:
        items = [("NONE", "NONE", "")]
    return sorted(items)
