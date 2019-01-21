from .decorators.argIsInstance import argIsInstance


@argIsInstance(str)
def appendStr(appendThis):
    fnName = appendStr.__name__

    @argIsInstance(str, fnName)
    def appendStr_inner(toThis):
        return toThis + appendThis

    return appendStr_inner
