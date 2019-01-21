# ------- #
# Imports #
# ------- #

from .internal.getTypedResult import getTypedResult


# ---- #
# Main #
# ---- #


def flatten(collection):
    typedFlatten = getTypedResult(collection, typeToFlatten, "flatten")
    return typedFlatten(collection)


# ------- #
# Helpers #
# ------- #


def flatten_list(aList):
    result = []
    for maybeInnerList in aList:
        if isinstance(maybeInnerList, list):
            for el in maybeInnerList:
                result.append(el)
        else:
            result.append(maybeInnerList)

    return result


typeToFlatten = {list: flatten_list}
