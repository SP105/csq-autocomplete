class ReadException(Exception):
    def __init__(self, message: str, original_exception=None):
        """
        :type original_exception: Exception
        """
        self.message = message
        self.original_exception = original_exception

        super().__init__(self.message + (": %s" % original_exception))

