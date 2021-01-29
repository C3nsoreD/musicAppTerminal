from urllib.parse import urlencode



def validate_params(params, required):
    if required in None:
        return

    partial = {x: x in params.keys() for x in required}
    not_supplied = [x for x in partial if not partial[x]]
    if not_supplied:
        msg = f'The parameters(s) "{', '.join(not_supplied)}" are required'
        raise AttributeError(msg)

        
def perpare_params(params, required=None):

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
