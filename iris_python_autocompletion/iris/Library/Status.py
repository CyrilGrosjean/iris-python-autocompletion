from dataclasses import dataclass

@dataclass
class Status:
    """
    datatype class %Library.Status\n
    Type ODBC : VARCHAR\n
    The %Status data type class is used to represent an error status code.\n
    Many of the methods provided by the system classes return error status information using the %Status data type. 
    The include file %occStatus.INC contains several macro definitions that are useful in testing the value of an error 
    code in %Status format. These macros include:\n
    - $$$ISOK(status:%Status) returns true (1) if the status code status does not represent an error condition.\n
    - $$$ISERR(status:%Status) returns true (1) if the status code status represents an error condition.\n
    You can get a more detailed description of an error by using 
    $system.Status.DecomposeStatus(status:%Status,&err,flag), which takes a status code and returns an array of error 
    strings; see %SYSTEM.Status. 
    """

    JSONTYPE: str
    """
    JSONTYPE is JSON type used for this datatype.
    """

    XSDTYPE: bytes
    """
    Declares the XSD type used when projecting XML Schemas.
    """
    
    def LogicalToOdbc(self, val="") -> str:
        """
        Converts the value of this data type from $List format to a delimited string using the value of the 
        ODBCDELIMITER parameter as a delimiter.
        """
        ...
    
    def LogicalToXSD(self, val: bytes) -> str:
        """
        Converts the %Binary value to the SOAP base64 encoded value.
        """
        ...
    
    def XSDToLogical(self, val: str) -> bytes:
        """
        Converts the SOAP encoded base64 input value to a logical value.
        """
        ...
