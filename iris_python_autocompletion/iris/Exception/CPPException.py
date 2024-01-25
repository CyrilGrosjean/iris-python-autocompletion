from dataclasses import dataclass
from iris_python_autocompletion.iris.Library.SystemBase import SystemBase

@dataclass
class CPPException(SystemBase):
    """
    class %Exception.CPPException s’étend %Library.SystemBase\n
    For InterSystems internal use only, subject to change without notice
    """

    Code: str
    """
    Code is the error code 
    """

    Data: str
    """
    Data is extra information supplied for certain errors 
    """

    InnerException: str
    """
    This holds an Inner exception. It is typically set to the caught exception when creating a new exception object 
    in a catch block. 
    """

    Location: str
    """
    Location is the location at which the error occurred 
    """

    Name: str
    """
    Name is the name of the error 
    """

    def DisplayString(self, pLevel: int = 0) -> str:
        """
        This returns a string that represents the exception. Users should feel free to modify the format in subclasses
        """
        ...
