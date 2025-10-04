from fastapi import HTTPException as _HTTPException, status as _status

class HTTPExceptions:
     """Classe para gerenciar exceções HTTP personalizadas."""
     
     @staticmethod
     def not_found(detail: str = "Not Found"):
          return _HTTPException(
               status_code=_status.HTTP_404_NOT_FOUND,
               detail=detail
          )
     
     @staticmethod
     def unauthorized(detail: str = "Unauthorized"):
          return _HTTPException(
               status_code=_status.HTTP_401_UNAUTHORIZED,
               detail=detail
          )
     
     @staticmethod
     def bad_request(detail: str = "Bad Request"):
          return _HTTPException(
               status_code=_status.HTTP_400_BAD_REQUEST,
               detail=detail
          )
     
     @staticmethod
     def internal_server_error(detail: str = "Internal Server Error"):
          return _HTTPException(
               status_code=_status.HTTP_500_INTERNAL_SERVER_ERROR,
               detail=detail
          )