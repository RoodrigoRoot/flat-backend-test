from rest_framework.exceptions import APIException


class FileWasNotCreatedException(APIException):
    status_code = 500
