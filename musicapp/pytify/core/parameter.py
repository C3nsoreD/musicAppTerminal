from urllib.parse import urlencode
"""
Includes helper functions that prepare the parameters before passing them to WebAPI endpoints
"""

def validate_params(params, required):
    """ Validates params based on required field.
    If some params aren't passed but are required, this function catches that.
    """
    if required is None:
        return
    # partial dict contains all required params
    partial = {x: x in params.keys() for x in required}
    # creates a list of params that should be included but were not supplied.
    not_supplied = [x for x in partial if not partial[x]]
    # if not empty
    if not_supplied:
        msg = f'The parameters(s) "{', '.join(not_supplied)}" are required'
        raise AttributeError(msg)


def perpare_params(params, required=None):
    """ Entry point for params, calls to validate_params to sneure all params are supplied
    """
    if params is None and required is not None:
        msg = f'The parameters(s) "{', '.join(required)}" are required'
        raise AttributeError(msg)
    elif params is None and required is None:
        return ''
    else:
        validate_params(params, required)

    query = urlencode(
        '&'.join([f'{key}={value}' for key, value in params.items()])
    )
    return f'?{query}'
