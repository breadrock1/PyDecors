
class AsyncRuntimeException(Exception):
    """Exception that thrown if invoked method has been thrown"""
    pass


class AsyncValueErrorException(Exception):
    """Exception that thrown if invoked method has returned non-expected type object"""
    pass
