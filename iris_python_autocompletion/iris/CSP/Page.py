from dataclasses import dataclass
from typing import Any, Union
from iris_python_autocompletion.iris.Library.Base import Base
from iris_python_autocompletion.iris.Library.Status import Status

@dataclass
class Page(Base):
    """
    abstract class %CSP.Page s’étend %Library.Base\n
    The %CSP.Page object serves as an event handler for CSP requests. All .csp pages by default derive from %CSP.Page, 
    although you can override this using the <CSP:CLASS> tag. CSP Servlets can be created by deriving a class from 
    %CSP.Page, see %CSP.StreamServer as an example. 
    """

    CHARSET: Any
    """
    Specifies the default character set for the page. This can be overriden using the <CSP:CONTENT CHARSET=> tag, or by 
    setting the %response.CharSet property in the OnPreHTTP() method. If this parameter is not specified, then for the 
    default charset is utf-8.
    """

    CONTENTTYPE: Any
    """
    Specifies the default content type for the page. This can be overriden using the <CSP:CONTENT TYPE=> tag, or by 
    setting the %response.ContentType property in the OnPreHTTP() method. The default value if this parameter is not 
    set is text/html.
    """

    CONVERTINPUTSTREAM: int = 0
    """
    Specifies if input %request.Content or %request.MimeData values are converted from their original character set on 
    input. By default (0) we do not modify these and receive them as a binary stream which may need to be converted 
    manually later. If 1 then if there is a 'charset' value in the request Content-Type or mime section we will convert 
    from this charset when the input data is text based. For either json or xml data with no charset this will convert 
    from utf-8 or honor the BOM if one is present.
    """

    CSPFILE: Any
    """
    If this page was compiled from a .csp file, then this parameter contains the filename used for compilation.
    """

    CSPSTRICT: Any
    """
    The CSPSTRICT parameter is set to 1, if the DOCTYPE indicates that this is a strict or frameset XHTML or 
    HTML 4 page.
    """

    CSPURL: Any
    """
    This parameter is used to make sure that if multiple CSP applications are mapped to the same namespace that the CSP 
    engine can correctly identify which class corresponds with which URL. If 'LockCSPName' is true (the default, 
    defined in the CSP application) then you can only access this page if the url exactly matches this 'CSPURL'. You 
    can set this parameter to "" if you wish to disable this check for this class. This check is applied for all CSP 
    urls (cls/csp/zen).\n
    If this page was compiled from a .csp file, then this parameter is automatically set to contain the url of this 
    file used for compilation.
    """

    CSPXHTML: Any
    """
    The CSPXHTML parameter is set to 1, if the DOCTYPE indicates that this is an XHTML page.
    """

    DOMAIN: Any
    """
    The default domain for csp:text, span and div tags. This parameter is used to specify the subset of localized 
    messages to be used on this page.
    """

    ENCODED: int = 0
    """
    Controls how the query parameters for this page are passed, it can be set to one of the following:\n
    - ENCODED=0 - Query parameters are not encrypted\n
    - ENCODED=1 - Query parameters are encrypted and passed within CSPToken\n
    - ENCODED=2 - Same as '1' except any unencrypted parameters are removed from the %request object before calling the 
    Page() method. This ensures that only encrypted parameter are available in the %CSP.Request object.
    """

    ERRORPAGE: Any
    """
    Specify a custom error page to call if there are any problems with generating this page. If this is not specified 
    it will use the default error page specified for this CSP application, and if this is not specified it will use the 
    system default error page. For example this could be set to '/csp/samples/error.csp' to display the sample error 
    page.
    """

    EXPIRES: Union[int, str] = -1
    """
    Specified the default value for the %response.Expires.\n
    It can be set to one of the following values:\n
    - -1: Expire immediately, this is the default for a CSP page\n
    - 0: Expire immediately, this also sets the 'no-store' option so using the back button will request a new page\n
    - "": Never expire (no HTTP Expires header is sent)\n
    - nnnnn: Number of seconds from now when the object should expire\n
    - Thu, 29 Oct 1998 17:04:19 GMT: Absolute time at which the object should expire\n
    - ddddd,sssss: Absolute time the object should expire in $ZTimeStamp format. Note that this must be specified in 
    the GMT timezone\n
    Note that setting this header also effects the 'Cache-Control' and 'Pragma' headers. If the page is set to expire 
    immediately then it will send a 'Cache-Control: no-cache' and 'Pragma: no-cache' to prevent any caches from storing 
    the page. If the page is set to never expires then it will not send any 'Cache-Control' or 'Pragma' headers. If you 
    set an expires date then it will not modify the 'Cache-Control' or 'Pragma' headers so if they are set they will be
    sent as specified and if you did not set them then nothing will be sent for these headers.
    """

    NOCHARSETCONVERT: Any
    """
    Specifies if we wish to turn off charset conversion for this page. Normally CSP uses the tables built into 
    InterSystems IRIS to convert between different charset's, however if you do not have a charset available you may 
    wish to turn this off to avoid getting the error page saying that this charset is not installed. Then the data will 
    be output and read in using RAW mode. This can be overridden using the <CSP:CONTENT NOCHARSETCONVERT=1> tag, or by 
    setting the %response.NoCharSetConvert property in the OnPreHTTP() method.
    """

    PAGETIMING: int = 0
    """
    If this parameter is true then we automatically record timing statistics of how long it takes to produce this page. 
    It is off by default.
    """

    PRIVATE: int = 0
    """
    Controls the access to the page, it can be set to one of the following:\n
    - PRIVATE=0 - Page can be linked to/bookmarked\n
    - PRIVATE=1 - Can only be referenced from another CSP page\n
    The user needs initially to enter the site through a PUBLIC page.
    """

    SECURITYRESOURCE: Any
    """
    This is a comma-delimited list of system Resources and associated permissions. A user must hold the specified 
    permissions on all of the specified resources in order to view this page.\n
    The format of each item in the list should be as follows:\n
    Resource[:Permission]\n
    Permission is optional, and defaults to USE if not supplied. If it is supplied, it should be one of USE, READ or 
    WRITE. You can also specify or grouping using the '|' character, so 'R1,R2|R3,R3|R4' means you must have resource 
    R1 and one of R2 or R3 and one of R3 or R4. So if you have R1,R3 it will pass, if you have R1,R4 it will not as it
    does not meet the R2|R3 condition. So the '|' or condition takes precedence over the ',' and condition.
    """

    TIMINGSLOTS: int = 48
    """
    Used by the timing to decide how many slots a day should be divided up into. The default is to record the timings 
    over half an hour (48 slots per day). If you need more detail you can modify this value in the superclass.
    """

    UseSession: int = 1
    """
    This parameter controls the CSP session support. By default CSP will use a persistent session which holds a license 
    until the session is ended or times out. If you override this then this CSP page will use a transient session which 
    is never persisted.
    """

    def ConvertParameter(self, url: str, name: str, value: str) -> Status:
        """
        You pass this the url of the page you are going to and a name and value parameter and it will return the name 
        and value encrypted if the target page is encoded.
        """
        ...

    def Decrypt(self, data: str) -> bytes:
        """
        Decrypts the input string using the %session.Key value that is unique to this user session. The input string is 
        the string provided by the Encrypt() method, the output is the decoded string.
        """
        ...
    
    def Encrypt(self, data: bytes) -> str:
        """
        Encrypts the input string using the %session.Key value that is unique to this user session. The output string 
        is a string that can be included in HTML and in URLs as it does not contain any characters that need to be 
        escaped in these environments. It can be decrypted with the Decrypt().\n
        Note that the data must not contain any unicode characters as the encryption function just takes a byte stream. 
        If you wish to encrypt unicode data then the simplest way is to form a $listbuild of the string first to 
        convert it into a byte stream.\n
        This function should only be used to encrypt server side data, do not make this function available from a 
        client or allow data passed from a client say as a url parameter to be encrypted and returned to the client. 
        If you do this will break the CSP security model as a client will be able to ask the server to encrypt any 
        value they choose and so the server can not rely on the decrypted values as a client will be able to create and 
        pass any encrypted value they want. Also you only want to encrypt data which is valid for this entire session, 
        so be aware that data that page a.csp encrypted could be copied by a client and inserted into a request for 
        page b.csp.
        """
        ...

    def EscapeHTML(i: Any) -> str:
        """
        This method converts input HTML text into Escaped HTML text.
        """
        ...