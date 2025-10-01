class BaseAppException(Exception):
    """Exceção base da aplicação"""
    def __init__(self, message: str = "An error occurred"):
        self.message = message
        super().__init__(self.message)


class UserNotFoundException(BaseAppException):
     """Exceção para usuário não encontrado"""
     def __init__(self, user_id: int):
          message = f"User with ID {user_id} not found."
          super().__init__(message)


class UserAlreadyExistsException(BaseAppException):
     """Exceção para usuário já existente"""
     def __init__(self, username: str):
          message = f"User with username '{username}' already exists."
          super().__init__(message)

class InvalidCredentialsException(BaseAppException):
     """Exceção para credenciais inválidas"""
     def __init__(self):
          message = "Invalid username or password."
          super().__init__(message)