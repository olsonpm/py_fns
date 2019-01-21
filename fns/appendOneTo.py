# ------- #
# Imports #
# ------- #

from .internal.getTypedResult import getTypedResult
from .appendOne import typeToAppendOne


# ---- #
# Main #
# ---- #


def appendOneTo(collection):
    def appendOneTo_inner(el):
        typedAppendOneTo = getTypedResult(
            collection, typeToAppendOne, appendOneTo.__name__
        )
        return typedAppendOneTo(el, collection)

    return appendOneTo_inner
