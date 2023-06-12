
class BaseException(Exception):
    pass

class ValueErrorException(BaseException):
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __str__(self):
        return f'Matrix of wrong dimensions'
    
class NotMatrixException(BaseException):
    
    def __init__(self, matrix):
        self.matirx = matrix
        
    def __str__(self):
        return f"It's not the matrix"
    
class WrongTypeException(BaseException):
    
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __str__(self):
        return f"Wrong type. Try again"