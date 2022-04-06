class BusinessException(Exception):
    pass


class ObjectDoesNotExist(BusinessException):
    ...


from app.exceptions.country import *
