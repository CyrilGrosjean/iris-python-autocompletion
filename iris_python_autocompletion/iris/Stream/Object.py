from dataclasses import dataclass
from typing import Any
from iris_python_autocompletion.iris.Library.RegisteredObject import RegisteredObject
from iris_python_autocompletion.iris.Library.Status import Status

@dataclass
class Object(RegisteredObject):
    """
    abstract stream class %Stream.Object s’étend %Library.RegisteredObject\n
    For information on this class, see Working with Streams.\n
    The %Stream.Object class provides the basic mechanism by which stream objects are stored to and retrieved from a 
    database.\n
    A stream represents an arbitrary array of characters (or bytes) and a current position. The basic stream interface 
    provides the ability to read data from a stream, write data to the stream, and rewind the current position to the 
    beginning of the stream.\n
    Within InterSystems IRIS, streams are used to create large (greater than 32K) object attributes.
    """

    DEFAULTCONCURRENCY: Any

    _Concurrency: str
    _Location: str
    """
    %Location is place where stream data is stored. For global streams this will be a global reference. For file 
    streams it may be a directory. This is not the location of this specific stream, but the root location of what 
    may be multiple streams. 
    """

    AtEnd: bool
    """
    The AtEnd property is set to true (1) when, during a read, a stream has reached the end of its data source.
    """

    Id: str
    """
    Id is the unique identifier for a stream within the %Location.
    """

    LastModified: int
    """
    LastModified is a read-only property containing the %TimeStamp of the last modification to this stream. If the 
    stream is null then it will report "". 
    """

    Size: int
    """
    Size is a read-only property containing the current size of the stream (in bytes for a binary stream and characters 
    for a character stream).\n
    If a specific stream implementation cannot determine the size of the stream then Size will be equal to -1.
    """

    def _AcquireLock(self, locktype: Any) -> Status:
        """
        Acquires a lock for the current instance. \n
        The locktype argument specifies the type of lock to acquire. It can take the following values:\n
        - "e": Exclusive 	An exclusive lock will prevent any other process from acquiring any type of lock on this 
        object. \n
        - "s": Shared 	A shared lock will allow other processes to acquire shared locks but will prevent other 
        processes from acquiring an exclusive lock.\n
        Fails if the locktype parameter is not one of the values described above.\n
        Returns a %Status value indicating success or failure.
        """
        ...
    
    def _CheckUnique(self, idxlist: list = "") -> Status:
        ...
    
    def _Delete(self, oid: )