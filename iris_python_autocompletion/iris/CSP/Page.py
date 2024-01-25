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

    def EscapeHTML(self, i: Any) -> str:
        """
        This method converts input HTML text into Escaped HTML text.
        """
        ...

    def EscapeURL(self, i: str, charset: str) -> str:
        """
        This method converts the in input URL string into Escaped URL string. Note that '/' is not escaped which is 
        consistent with rfc3986. The conversion first encodes the string using the current devices charset and then url 
        encodes the result. If you pass in charset then we will use this rather than the current devices charset for 
        the encoding.
        """
        ...
    
    def HyperEventCall(self, methodName: str, args: str, type: int = 0, mobile: bool = 0) -> str:
        """
        This method returns the string that needs to be written to the current device in order to insert a HyperEvent 
        into a CSP page that is defined via a class. This method is the hand written class equivalent of using 
        #call(...)#, #server(...)# or #vbserver(...)# in a CSP page.\n
        The methodName argument defines the method to call in the same format as #server: either 
        ..method or package.class.method.\n
        The args argument defines the runtime JavaScript arguments to be passed to the ObjectScript method as a 
        comma separated string.\n
        The type argument is 0 if you wish to use a #server(...)# style HyperEvent (this is the default), 1 if you 
        wish to use a #call(...) style HyperEvent. Note that browsers are deprecating the synchronous #server(...)# 
        style XMLHttpRequest so application should transition to using type=1. If the argument is 0 then it will use 
        double quotes for the JavaScript which is the behaviour of #vbserver in a csp page, this will work correctly 
        in both JavaScript and VBScript but you need to be aware that it will quote its parameter with ".\n
        In order to use this method, HyperEventHead() must be used in the <head> section.
        """
        ...

    def HyperEventHead(self, iframeOnly: bool, strict: bool, optionalBroker: bool) -> str:
        """
        This method returns the string that needs to be written to the current device during generation of the <head> 
        section in order to use HyperEvents. See HyperEventCall() for details. This is not needed if you are using 
        #server, #vbserver or #call calls from a .csp page as this is automatically inserted, it is only required when 
        generating the class or the HyperEvent calls directly. The iframeonly argument is now ignored since #call and 
        #server now both use XMLHttpRequest. However, the iframeonly argument is kept for compatibility. Passing the 
        argument strict=1 will create strict HTML 4 format of script tag.
        """
        ...
    
    def Include(self, url: str) -> None:
        """
        Include another csp page or file in the output at this point. If the url ends in either 'csp' or 'cls' then 
        it will call the csp or cls class to generate output skipping the output of the HTML headers. If the url is a 
        file then it uses the stream server to output this file. This url can be a relative path in which case it will 
        be resolved based on the current page url first. This is called by the <csp:include Page="page.csp"> tag.\n
        You can pass additional parameters to the included page by adding them to the url to call. These parameters 
        will only exist for the included page and the %request object is restored when it returns to the calling page.
        """
        ...
    
    def InsertHiddenField(self, url: str, name: str, value: str, extra: str = "") -> str:
        """
        Inserts a '<input type="hidden" name="Name" value="Value">' tag into the current document. If the target url 
        you are submitting to (url) is encoded then this will encrypt the data in this hidden link. In this way it is 
        similar to the Link(). The extra are any extra attributes to add to the tag.
        """
        ...
    
    def InsertHiddenFields(self, url: str, query: str) -> str:
        """
        Return the string containing the hidden form tags. You pass it the url URL of the target page that this form is 
        submitted to (the action=xxx attribute).\n
        The array, query, contains an optional set of name-value pairs which are also output as hidden input fields. 
        This is normally called automatically directly after the <FORM> tag to insert any hidden input tags that are 
        required. However if you generate a form programatically then you may need to call this function just after you 
        output the <FORM> tag.
        """
        ...
    
    def IsPrivate(self) -> bool:
        """
        Returns 1 if this page is in fact a private page (see PRIVATE).
        """
        ...
    
    def Link(self, link: str, query: str, addQ: bool = 0) -> str:
        """
        Tranforms the link specified by link into a URL and returns it as a string.\n
        The URL may be encrypted.\n
        The array, query, contains an optional set of name-value pairs which are added to the URL. For example 
        'Set query("name")="data"'\n
        If the optional argument addQ is true, then a ? or &, as appropriate, is added to end of the URL
        """
        ...
    
    def OnHTTPHeader(self, OutputBody: bool) -> Status:
        """
        Event handler for PAGE event: this is invoked in order to send HTTP headers. The default action is to invoke 
        the WriteHTTPHeader() of the %CSP.Response which generates HTTP 1.0 standard headers. Set OutputBody to 0 to 
        prevent prevent OnPage() from being called, leave it unchanged otherwise. Returns a %Status code.
        """
        ...
    
    def OnPage(self) -> Status:
        """
        Event handler for PAGE event: this is invoked in order to generate the content of a csp page.
        """
        ...
    
    def OnPageError(self, sc: Status) -> Status:
        """
        Event handler for any error that occurs on the page. If an error occurs and this method is defined it calls 
        this method passing it the error code by reference. You may change the error code if wished, if you set it 
        to $$$OK then it will cancel the error and the CSP error page will not be displayed.
        """
        ...
    
    def OnPostHTTP(self) -> None:
        """
        Event handler for POSTPAGE event: this is invoked after the data for the CSP page has been sent to the browser 
        from the the InterSystems IRIS server.
        """
        ...
    
    def OnPostHyperEvent(self, classe: str, method: str) -> Status:
        """
        Event handler which is invoked after a hyperevent method is called on this page.
        """
        ...
    
    def OnPreHTTP(self) -> bool:
        """
        Event handler for PreHTTP event: this is invoked before the HTTP headers for a CSP page have been sent. All 
        changes to the %CSP.Response class, such as adding cookies, HTTP headers, setting the content type etc. must 
        be made from within the OnPreHTTP() method. Also changes to the state of the CSP application such as changing 
        %session.EndSession or %session.AppTimeout must be made within the OnPreHTTP() method. It is prefered that 
        changes to %session.Preserve are also made in the OnPreHTTP() method as this is more efficient, although it is 
        supported in any section of the page. Return 0 to prevent OnPage() from being called.
        """
        ...
    
    def OnPreHyperEvent(self, classe: str, method: str) -> Status:
        """
        Event handler which is invoked before a hyperevent method is called on this page. This gives you a chance to 
        modify the behavior of every hyperevent call within this page. Return an error code to prevent the hyperevent 
        from being called.
        """
        ...
    
    def Page(self, skipheader: bool = 1) -> Status:
        """
        Process a request to serve a CSPPage. This method is invoked by the CSP Server. In turn, this method invokes:\n
        - OnPreHTTP()\n
        - OnPage()\n
        - OnPostHTTP()\n
        Note that OnPostHTTP() always gets run, even if there was an error.\n
        skipheader will skip the running of the OnPreHTTP() method.
        """
        ...
    
    def QuoteJS(self, i: Any) -> str:
        """
        This method converts input string into quoted JavaScript literal
        """
        ...
    
    def RewriteURL(self, url: str) -> str:
        """
        This method will rewrite a URL to use #url()# if needed
        """
        ...
    
    def ShowError(self, sc: Status) -> None:
        """
        Display a %Status error code to the CSP Page.
        """
        ...
    
    def StartTimer(self, name: str) -> None:
        """
        Used to get performance information on your CSP pages. This is called to start the timing of a block of code. 
        The name specifies the type of component we are timing, for example we automatically call this with 'Page' at 
        the start and end of the rendering of the CSP page. The idea is that you can call this at the start and end of 
        any block of code to log information on how long this is taking.\n
        This is a default implementation of what sort of information to log, however you can subclass this and 
        StopTimer() to enhance the information that is logged.
        """
        ...
    
    def StopTimer(self, name: str) -> None:
        """
        Used to time performance information on your CSP pages. This is called to stop the timing of a block of code. 
        The name specifies the type of component to time. See StartTimer() for more information on this.
        """
        ...
    
    def ThrowError(self, sc: Status) -> None:
        """
        Passed a %Status code this goes to the error page passing this status code
        """
        ...
    
    def UnescapeHTML(self, i: Any) -> str:
        """
        This method converts Escaped HTML text into normal HTML text
        """
        ...
    
    def UnescapeURL(self, i: str, charset: str) -> str:
        """
        This method converts the in Escaped URL string back to its original form. The conversion first unescapes the 
        URL then decodes the string using the current devices charset. If you pass in charset then we will use this 
        rather than the current devices charset for the decoding.
        """
        ...
