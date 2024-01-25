from dataclasses import dataclass
from iris_python_autocompletion.iris.Exception.CPPException import CPPException
from iris_python_autocompletion.iris.Library.Status import Status

@dataclass
class AbstractException(CPPException):
    """
    abstract class %Exception.AbstractException s’étend %Exception.CPPException\n
    The %Exception.AbstractException defines the interface to exceptions that may be caught and thrown via the 
    Try/Catch exception handling facilities. Users wishing to define new exception classes should inherit from this 
    interface class. Only instances of classes that inherit from %Exception.AbstractException may be thrown with the 
    'throw' command. 
    """

    def _OnNew(self, pName: str, pCode: str, pLocation: str, pData: str, pInnerException: 'AbstractException') -> Status:
        ...
    
    def AsSQLCODE(self) -> int:
        """
        Return the SQLCODE value corresponding to the exception.
        """
        ...

    def AsSQLMessage(self) -> str:
        """
        Return the SQL %msg string describing details of the exception.
        """
        ...
    
    def AsStatus(self) -> Status:
        """
        Convert this exception to a %Status compatible value.
        """
        ...
    
    def DisplayString(self, pLevel: int = 0) -> str:
        """
        This returns a string that represents the exception. Users should feel free to modify the format in subclasses.
        """
        ...
    
    def Log(self) -> Status:
        """
        Call the log function (LOG^%ETN) to log this exception. You can view this log at the terminal with 'Do ^%ER' 
        utility or from the system management portal.
        """
        ...
    
    def OnAsSQLCODE(self) -> int:
        """
        Override this method to provide a custom conversion of an exception to an SQLCODE value.
        """
        ...
    
    def OnAsSQLMessage(self) -> str:
        """
        Override this method to provide a custom conversion of an exception to the SQL %msg string.
        """
        ...
    
    def OnAsStatus(self) -> Status:
        """
        Override this method to provide a custom conversion of an exception to a status.
        """
        ...
    
    def OutputToDevice(self, pLevel: int = 0) -> None:
        """
        This outputs the string representation of the exception to the current device, recursively outputing any 
        inner exceptions.
        """
        ...
    
    def OutputToStream(self, pStream: )