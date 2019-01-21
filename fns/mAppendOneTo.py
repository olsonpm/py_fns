# ------- #
# Imports #
# ------- #

from .internal.getTypedResult import getTypedResult
from .mAppendOne import typeToMAppendOne


# ---- #
# Main #
# ---- #


def mAppendOneTo(collection):
    def mAppendOneTo_inner(el):
        typedMAppendOneTo = getTypedResult(
            collection, typeToMAppendOne, mAppendOneTo.__name__
        )
        return typedMAppendOneTo(el, collection)

    return mAppendOneTo_inner
