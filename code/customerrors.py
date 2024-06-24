"""

"""
# class RuntimeErrorWithCode(TypeError):
class RuntimeErrorWithCode(Exception):
    """
    Exception raised when a specific error code is needed.
    """

    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

# raise MyCustomError('OUCH an error happened. ', 500)

err = RuntimeErrorWithCode("An error happened", 500)
print(err.__doc__)