from dataclasses import dataclass
from typing import Any
from iris_python_autocompletion.iris.CSP.Page import Page
from iris_python_autocompletion.iris.Library.Status import Status

@dataclass
class Login(Page):
    """
    class %CSP.Login s’étend %CSP.Page\n
    Provide a default login and security-token pages for CSP applications. User can override the look of this page by 
    creating a subclass and overriding the DrawTitle method and the LOGINTITLE parameters.\n
    CORS processing for CSP pages that do not inherit from %CSP.REST is also provided here. To turn on CORS assign the 
    application's login page to be a subclass %CSP.Login that has the HandleCorsRequest parameter = 1. In addition, 
    OnHandleCorsRequest and/or OnHandleOptionsRequest methods may be overridden in order to override the default 
    behavior for the application. 
    """

    DOMAIN: Any
    """
    Login page localization domain
    """

    FAVORITEICON: Any
    """
    Home favorite icon.
    """

    HandleCorsRequest: Any
    """
    This parameter influences the CORS support for the CSP application that has this login page assigned. If set to 
    true (1) then CORS processing is ON. Otherwise CORS processing is OFF.
    """

    LOGINTITLE: Any
    """
    Title displayed for login page.\n
    Users can override this value to customize the login page.
    """

    STYLESHEET: Any
    """
    Name of stylesheet used for login page.\n
    Not used by default page: styles come from the DrawSTYLE method.
    """

    def DrawCSS3STYLE(self) -> None:
        """
        Draw the style definitions for the login page.\n
        Users can override this method to customize the login page.
        """
        ...
    
    def DrawHEAD(self, pTitle: Any = "") -> None:
        """
        Draw the HEAD section of the login page.\n
        Users can override this method to customize the login page.
        """
        ...
    
    def DrawSTHEAD(self) -> None:
        """
        Draw the HEAD section of the security token page.\n
        Users can override this method to customize the security token page.
        """
        ...
    
    def DrawSTTitle(self, pTitle: str) -> None:
        """
        Draw the title section of the security token page.\n
        pTitle is the title for the page.\n
        Users can override this method to customize the security token page.
        """
        ...
    
    def DrawSTYLE(self) -> None:
        """
        Draw the style definitions for the login page.\n
        Users can override this method to customize the login page.
        """
        ...
    
    def DrawTitle(self, pTitle: str) -> None:
        """
        Draw the title section of the login page.\n
        pTitle is the title for the page.\n
        Users can override this method to customize the login page.
        """
        ...
    
    def DrawTitleSection(self, msgs: str) -> None:
        """
        Draw the title section of the page.\n
        pTitle is the title for the page.\n
        Users can override this method to customize the page title section.
        """
        ...
    
    def OnErrorSetup(self, skipheader: bool) -> bool:
        ...
    
    def OnHandleCorsRequest(self, url: str) -> Status:
        """
        This is the CORS request handler. User should override this method in their login page if they don't want the 
        default behavior.
        """
        ...
    
    def OnHandleOptionsRequest(self, url: str) -> Status:
        """
        This methods provides handling of the options request for this CSP application. Note carefully: If 
        authentication is required then this method will be called before login and as such will have only limited 
        privileges.
        """
        ...
    
    def OnLoginPage(self) -> Status:
        ...
    
    def OnPage(self) -> Status:
        """
        Output the default login page as HTML
        """
        ...

    def OnPreHTTP(self) -> bool:
        """
        Determine if we need login CSRF tokens and if so add them. If a login page subclass overrides this method it 
        should call this implementation to ensure we set the login CSRF tokens if needed.
        """
        ...
    
    def OnSecurityTokenPage(self) -> Status:
        ...
    
    def SupportedVerbs(self, url: Any, verbs: str) -> Status:
        """
        By default all methods are supported.
        """
        ...
