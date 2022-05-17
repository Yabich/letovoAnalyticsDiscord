connected = False
class NotAuthorized(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class NothingFoundError(Exception):
    pass

def connection():
    return connected