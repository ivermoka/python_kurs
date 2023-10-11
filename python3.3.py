globalVariable = "global"

def function() -> str:
    global globalVariable

    localVariable = "local"
    globalVariable = "global changed"

    return globalVariable, localVariable
globalVariable, localVariable = function()

print(f'global: {globalVariable} local: {localVariable}')
