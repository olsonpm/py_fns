# ------- #
# Imports #
# ------- #

from .internal.getTypedResult import getTypedResult
from .appendAll import typeToAppendAll


# ---- #
# Main #
# ---- #


def appendAllTo(collection):
    def appendAllTo_inner(collectionToAppend):
        typedAppendAllTo = getTypedResult(
            collection, typeToAppendAll, appendAllTo.__name__
        )
        return typedAppendAllTo(collectionToAppend, collection)

    return appendAllTo_inner
