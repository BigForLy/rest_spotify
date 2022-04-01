def log_errors(func):
    def _(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            error_message = f'Errors: {ex}'
            print(error_message)
            raise ex

    return _
