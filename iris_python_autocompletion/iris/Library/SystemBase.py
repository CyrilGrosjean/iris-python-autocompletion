from dataclasses import dataclass
from typing import Any
from iris_python_autocompletion.iris.Library.ObjectHandle import ObjectHandle
from iris_python_autocompletion.iris.Library.Status import Status

@dataclass
class SystemBase:
    """
    Base superclass. For internal use only, this is automatically added to all classes as a superclass. 
    """

    __name__ = "%%Libray.SystemBase"

    def _ClassIsLatestVersion(self) -> bool:
        """
        Return true if this instance is the latest version of this class, and false if the class has been recompiled 
        so there is a newer version on disk
        """
        ...
    
    def _ClassName(self, fullname: bool) -> str:
        """
        Returns the object's class name. The fullname determines how the class name is represented. If it is 1 then it 
        returns the full class name including any package qualifier. If it is 0 (the default) then it returns the name 
        of the class without the package, this is mainly for backward compatibility with the pre-package behaviour of 
        %ClassName.
        """
        ...
    
    def _DispatchClassMethod(self, Class: str, Method: str, **args) -> None:
        """
        Is used to implement an unknown class method call
        """
        ...

    def _DispatchGetModified(self, Property: str) -> None:
        """
        Is used to get the value of the modified flag for an unknown property.
        """
        ...
    
    def _DispatchGetProperty(self, Property: str) -> None:
        """
        Is used to get the value of an unknown property.
        """
        ...
    
    def _DispatchMethod(self, Method: str, **args) -> None:
        """
        Is used to implement an unknown method call. It is also used to resolve an unknown multidimensional property 
        reference (to get the value of a property) because that syntax is identical to a method call.
        """
        ...
    
    def _DispatchSetModified(self, Property: str, Val: Any) -> None:
        """
        Is used to set the value of the modified flag for an unknown property.
        """
        ...
    
    def _DispatchSetMultidimProperty(self, Property: str, Val: Any, **Subs) -> None:
        """
        Is used to set the value of an unknown multidimensional property.
        """
        ...
    
    def _DispatchSetProperty(self, Property: str, Val: Any) -> None:
        """
        is used to set the value of an unknown property.
        """
        ...
    
    def _Extends(self, isclass: str) -> int:
        """
        Returns true (1) if this class is inherited either via primary or secondary inheritance from 'isclass'.
        """
        ...
    
    def _GetParameter(self, paramname: str = "") -> str:
        """
        This method returns the value of a class parameter at runtime
        """
        ...
    
    def _IsA(self, isclass: str) -> int:
        """
        Returns true (1) if instances of this class are also instances of the isclass parameter. That is 'isclass' 
        is a primary superclass of this object.
        """
        ...
    
    def _New(self, initvalue: str) -> ObjectHandle:
        """
        Creates a new instance of object in memory. %New() creates an OREF value that refers to the object instance, 
        registers the OREF with the system along with its class name, and reserves system storage for the properties.\n
        %New() initializes all the object's properties to their default values and calls the user-provided method, 
        %OnNew(), if it is present. The optional arguments are passed on to the %OnNew() method. If the object is 
        persistent, its OID is set to null string (""). %New() returns an OREF value that refers to the new object 
        instance or $$$NULLOREF if unable to create the object instance.
        """
        ...
    
    def _OriginalNamespace(self) -> str:
        """
        Return the namespace this oref was created in. This also returns the namespace this class was first referenced 
        in if calling class methods.
        """
        ...
    
    def _PackageName(self) -> str:
        """
        Returns the object's package name.
        """
        ...

    def _SetModified(self, value: int) -> Status:
        """
        Setting the modified state of the object.
        """
        ...
