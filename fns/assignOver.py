# ------- #
# Imports #
# ------- #

from .internal.getTypedResult import getTypedResult
from types import SimpleNamespace
from copy import copy


# ---- #
# Main #
# ---- #


def assignOver(collection):
    fnName = assignOver.__name__
    assignOverFn = getTypedResult(collection, typeToAssignOver, fnName)

    return assignOverFn(collection)


# ------- #
# Helpers #
# ------- #


def assignOver_simpleNamespace(secondary):
    def assignOver_simpleNamespace_inner(primary):
        result = copy(primary)

        for k, v in secondary.__dict__.items():
            if k not in result.__dict__:
                setattr(result, k, v)

        return result

    return assignOver_simpleNamespace_inner


def assignOver_dict(secondary):
    def assignOver_dict_inner(primary):
        result = copy(primary)

        for k, v in secondary.items():
            if k not in result:
                result[k] = v

        return result

    return assignOver_dict_inner


typeToAssignOver = {
    dict: assignOver_dict,
    SimpleNamespace: assignOver_simpleNamespace,
}
