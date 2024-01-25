from dataclasses import dataclass
from typing import Any
from iris_python_autocompletion.iris.CSP.Login import Login
from iris_python_autocompletion.iris.Library.Status import Status

@dataclass
class Rest(Login):
    """
    class %CSP.REST s’étend %CSP.Login\n
    Applications wishing to support REST should subclass this class, implement the methods to be called, and define a 
    UrlMap XDATA block which maps Urls and request Method (DELETE/GET/POST/PUT) to those methods. Users define a csp 
    web application which will be serviced by their custom subclass. To achieve this, in the management portal set the 
    'Dispatch Class' to the name of the custom subclass of %CSP.REST.\n
    Note: %CSP.REST extends %CSP.Login instead of just %CSP.Page because %CSP.Login contains the default CORS support 
    as well as being a subclass of %CSP.Page. 
    """
    
    CONTENTTYPEJSON: Any
    CONTENTTYPETEXT: Any
    HTTP200OK: Any
    HTTP201CREATED: Any
    HTTP202ACCEPTED: Any
    HTTP204NOCONTENT: Any
    HTTP304NOTMODIFIED: Any
    HTTP400BADREQUEST: Any
    HTTP401UNAUTHORIZED: Any
    HTTP403FORBIDDEN: Any
    HTTP404NOTFOUND: Any
    HTTP405METHODNOTALLOWED: Any
    HTTP406NOTACCEPTABLE: Any
    HTTP409CONFLICT: Any
    HTTP415UNSUPPORTEDMEDIATYPE: Any
    HTTP422UNPROCESSABLEENTITY: Any
    HTTP423LOCKED: Any
    HTTP500INTERNALSERVERERROR: Any
    HandleCorsRequest: Any
    """
    This parameter influences the CORS support. The default is an empty string meaning 'not specified'. If set to true 
    (1) then CORS processing is ON. If set to false (0) then CORS processing is OFF. If left unset ("") then the 
    decision to process CORS is delegated to the setting on the URL map route.
    """

    TokenLoginEndpoint: Any
    """
    If the REST application is using token authentication, then this parameter gives the path to use for the "login" 
    endpoint. The default is "/login".
    """

    TokenLogoutEndpoint: Any
    """
    If the REST application is using token authentication, then this parameter gives the path to use for the "logout" 
    endpoint. The default is "/logout".
    """

    TokenRefreshEndpoint: Any
    """
    If the REST application is using token authentication, then this parameter gives the path to use for the "refresh" 
    endpoint. The default is "/refresh".
    """

    TokenRevokeEndpoint: Any
    """
    If the REST application is using token authentication, then this parameter gives the path to use for the token 
    revocation endpoint. The default is "/revoke".
    """

    UseSession: bool = 0
    """
    This parameter controls the CSP session support. By default the CSP session will be ended after each request in 
    accordance with the spirit of REST. However this CAN be overridden by the user. To use a session, it's necessary 
    to manage the CSPSESSION cookie. Browsers do this automatically but command line tools such as CURL require the 
    setting of options.\n
    Note that if you choose to use a session then this will use a CSP license until the session is ended or expires and 
    the grace period has been satisfied. If you use the default of no session then this will be the same behavior as 
    SOAP requests of holding a license for ten seconds.
    """

    def AcceptsContentType(self, pType: str) -> bool:
        """
        This method tests the HTTP_ACCEPT header and returns true if the passed content type is acceptable
        """
        ...
    
    def AccessCheck(self, pAuthorized: bool = 0) -> Status:
        """
        This method performs a basic access check. You can override this to add additional checks.
        """
        ...
    
    def DispatchRequest(self, url: str, method: str, forwaded: bool, **args) -> Status:
        """
        Dispatch a REST request according to URL and Method. The pArgs argument is a local array of parameters from the 
        caller. The forwarded argument is no longer used.
        """
        ...
    
    def Error(self, skipheader: bool = 1) -> Status:
        """
        Called for a REST page in the event of an error being trapped by CSP server
        """
        ...
    
    def GetAuthChallenge(self) -> str:
        """
        This method determines what challenge will be sent with a 401 (Unauthorized) response. The default is the type 
        of the Authorization header used in the request. For unauthenticated requests, the default is 'Basic'. Note 
        most browsers will display a native login prompt in response to a 'Basic' challenge.
        """
        ...
    
    def Http405(self, pSc: Status) -> Status:
        """
        Issue a '405' error ( user can override)
        """
        ...
    
    def Http500(self, pE: )