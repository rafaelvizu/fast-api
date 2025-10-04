class _BaseProductException(Exception):
    """Base exception for product-related errors."""
    def __init__(self, message: str = "An error occurred with the product"):
        self.message = message
        super().__init__(self.message)


class ProductNotFoundException(_BaseProductException):
     """Exception for product not found."""
     def __init__(self, product_id: int):
          message = f"Product with ID {product_id} not found."
          super().__init__(message)

class ProductAlreadyExistsException(_BaseProductException):
     """Exception for product already exists."""
     def __init__(self, product_name: str):
          message = f"Product with name '{product_name}' already exists."
          super().__init__(message)

class InvalidProductDataException(_BaseProductException):
     """Exception for invalid product data."""
     def __init__(self, details: str):
          message = f"Invalid product data: {details}"
          super().__init__(message)

