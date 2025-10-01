from fastapi import HTTPException, status

class HTTPExceptions:
     """Classe para gerenciar exceções HTTP personalizadas."""
     
     @staticmethod
     def not_found(detail: str = "Not Found"):
          return HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail=detail
          )
     
     @staticmethod
     def unauthorized(detail: str = "Unauthorized"):
          return HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail=detail
          )
     
     @staticmethod
     def bad_request(detail: str = "Bad Request"):
          return HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST,
               detail=detail
          )
     
     @staticmethod
     def internal_server_error(detail: str = "Internal Server Error"):
          return HTTPException(
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
               detail=detail
          )