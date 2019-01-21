# ------- #
# Imports #
# ------- #

from .internal.getTypedResult import getTypedResult


# ---- #
# Main #
# ---- #


def discardLast(n):
    fnName = discardLast.__name__

    def discardLast_inner(collection):
        discardFn = getTypedResult(collection, typeToDiscardLast, fnName)
        return discardFn(n, collection)

    return discardLast_inner


# ------- #
# Helpers #
# ------- #


def discardLast_viaSlice(n, sliceAble):
    return sliceAble[:-n]


typeToDiscardLast = {list: discardLast_viaSlice, str: discardLast_viaSlice}
