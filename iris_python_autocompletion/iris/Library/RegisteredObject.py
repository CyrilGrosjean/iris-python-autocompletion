from dataclasses import dataclass
from typing import Any
from iris_python_autocompletion.iris.Library.Base import Base
from iris_python_autocompletion.iris.Library.Status import Status

@dataclass
class RegisteredObject(Base):
    """
    abstract class %Library.RegisteredObject s’étend %Library.Base\n
    For information on this class, see Working with Registered Objects.\n
    The %RegisteredObject class provides the core capabilities needed to manage the in-memory version of an object. 
    Specifically, %RegisteredObject provides the ability to create and destroy object references (OREFs) as well as 
    support for polymorphism. The %RegisteredObject class also provides the ability to swizzle other referenced 
    objects (persistent or serial) into memory.\n
    Classes derived directly from %RegisteredObject can be used as transient objects; objects that exist in memory-and 
    can be used from client applications-but are not stored in the database.
    """

    CAPTION: Any
    """
    Optional name used by the Form Wizard for a class when generating forms.
    """

    JAVATYPE: Any
    """
    The Java type to be used when exported.
    """

    PROPERTYVALIDATION: int = 2
    """
    This parameter controls the default validation behavior for the object.\n
    It can take one of the following values:\n
    - 0: NoValidate 	Perform no automatic property validation.\n
    - 1: ValidateOnSet 	Perform validation (call the property's ..IsValid method) every time an attribute value is set.\n
    - 2: ValidateOnSave 	Perform property validation (in the %ValidateObject() method)) when the object is saved. 
    This is only applicable to persistent objects.\n
    Note: The use of ValidateOnSet is not recommended-it can cause excessive communication between client and server in 
    distributed applications. It is provided for compatability with previous versions.
    """
    
    def _AddToSaveSet(self, depth: int = 3, refresh: int = 0) -> Status:
        """
        This method adds the current object to the SaveSet containing objects that are part of the current %Save() for 
        persistent classes or %GetSwizzleObject for serial classes. A queue of objects to be saved or serialized is 
        also constructed. Only modified objects are included in the save queue. The value (OID or serial value in OID 
        form) of each object is also placed in the SaveSet.\n
        This method will invoke the %OnAddToSaveSet method if it is implemented. See that method for more information.\n
        %AddToSaveSet should not ever be invoked directly except from %OnAddToSaveSet().\n
        This method takes these parameters: depth, with these values:\n
        - 1:  	Include this object in the SaveSet and, if it has not been serialized put it in the save queue and 
        invoke %AddToSaveSet on any objects referenced by this object to the SaveSet with a depth of 1.\n
        - 2: 	Include this object in the SaveSet and save queue. Also invoke %AddToSaveSet on any referenced objects 
        in the SaveSet with a depth of 1.\n
        - 3: 	Include this object in the SaveSet and, if modified, the save queue. Also invoke %AddToSaveSet on any 
        referenced objects in the SaveSet with a depth of 3.\n
        refresh, with these values:\n
        - 0: Add this object to the save set only if it isn't already included.\n
        - 1: Add this object to the SaveSet even if it already exists. This causes object dependencies to be rebuilt. 
        Typically, this value is only passed by %OnAddToSaveSet when it modifies objects other than the current one.\n
        Note: Swizzled serial objects always have an empty serial value and will always be placed in the save queue and 
        the SaveSet. the value of depth simply gets passed on to its referenced objects.
        """
        ...
    
    def _ConstructClone(self, deep: int, cloned: str, location: str) -> 'RegisteredObject':
        """
        Clone the current object to a new object. If deep is 1 then this does a deep copy which will also copy any 
        subobjects and if deep is 0 then it will create another reference to any subobjects and increment the reference 
        count appropriately. It returns the new cloned object.\n
        Note that even if deep=0 when you clone a parent object in a parent child relationship or a one object of a one 
        to many relationship then it will construct clones of all the child/many objects. This is because a child/many 
        object can only point at a single parent and so if we did not create a clone of these then you would have a 
        relationship with zero items in it. If you really just want to clone the object without these child/many 
        objects then pass deep=-1 to this method.\n
        After the clone is constructed it will call %OnConstructClone(object,deep,.cloned) on the clone if it is 
        defined so that you can perform any additional steps e.g. taking out a lock. This works just the same way as 
        %OnNew() does.\n
        The object is the oref of the original object that was cloned. The cloned array is just used internally when 
        doing a deep clone to prevent recursive loops, do not pass anything in at all for this parameter on the initial 
        call. If you write a %OnConstructClone and from here you wish to call %ConstructClone on another object pass in 
        the cloned array, e.g. 'Do oref.%ConstructClone(1,.cloned)' so that it can prevent recursive loops.\n
        The location is used internally to pass the new location for stream objects.
        """
        ...
    
    def _ConstructCloneInit(self, object: 'RegisteredObject', deep: int, cloned: str, location: str) -> Status:
        ...
    
    def _IsModified(self) -> int:
        """
        Returns true (1) if a property of this instance has been modified, otherwise false (0). A TRUE result does not 
        necessarily mean that any property has actually been changed. If %IsModified() returns false then the object 
        has not been modified. There are some situations where we simply cannot efficiently detect a change in value. 
        In these cases we will set the modified status of the property.
        """
        ...
    
    def _NormalizeObject(self) -> Status:
        """
        Normalizes all of an object's property values by invoking the data type Normalize methods. Many data types may 
        allow many different representations of the same value. Normalization converts a value to its cannonical, or 
        normalized, form.
        """
        ...
    
    def _ObjectModified(self) -> int:
        """
        This method is somewhat similar to %IsModified but it also checks to see if swizzled references would cause the 
        object to become modified should they be serialized. This works on the assumption that a reference to a 
        persistent object will never be modified if the ID has already been assigned. For references to serial objects, 
        a call to %ObjectModified indicates whether or not the serialized value is different. If the reference to a 
        swizzled object is different from the initial object state then the $$$objModAll macro will already return 
        true. Reference the Set code. Returns true (1) if this instance has been modified, otherwise false (0).
        """
        ...
    
    def _OnAddToSaveSet(self, depth: int = 3, insert: int = 0, callcount: int = 0) -> Status:
        """
        This callback method is invoked when the current object is added to the SaveSet, either because %Save() was 
        invoked on this object or on an object that references this object. %OnAddToSaveSet can modify the current 
        object. It can also add other objects to the current SaveSet by invoking %AddToSaveSet or remove objects by 
        calling %RemoveFromSaveSet.\n
        If this method returns an error status then %Save() will fail and the transaction will be rolled back.
        """
        ...
    
    def _OnClose(self) -> Status:
        """
        This callback method is invoked by the %Close() method to provide notification that the current object is 
        being closed.\n
        The return value of this method is ignored.
        """
        ...
    
    def _OnConstructClone(self, object: 'RegisteredObject', deep: bool, cloned: str) -> Status:
        """
        This callback method is invoked by the %ConstructClone() method to provide notification that a clone of an 
        object is being created. It passes in the oref of the object that was cloned in object.\n
        If this method returns an error then the object will not be created.
        """
        ...
    
    def _OnNew(self) -> Status:
        """
        This callback method is invoked by the %New() method to provide notification that a new instance of an object 
        is being created.\n
        If this method returns an error then the object will not be created.\n
        It is passed the arguments provided in the %New call. When customizing this method, override the arguments with 
        whatever variables and types you expect to receive from %New(). For example, if you're going to call %New, 
        passing 2 arguments, %OnNew's signature could be:\n
        Method %OnNew(dob as %Date = "", name as %Name = "") as %Status If instead of returning a %Status code this 
        returns an oref and this oref is a subclass of the current class then this oref will be the one returned to the 
        caller of %New method.
        """
        ...
    
    def _OnValidateObject(self) -> Status:
        """
        This callback method is invoked by the %ValidateObject() method to provide notification that the current object 
        is being validated.\n
        If this method returns an error then %ValidateObject() will fail.
        """
        ...
    
    def _RemoveFromSaveSet(self) -> Status:
        """
        This method removes the current object from the SaveSet. If this object is also in the save queue it is removed 
        from there as well.
        """
        ...
    
    def _SerializeObject(self, serial: bytes, partial: int = 0) -> Status:
        """
        This method retrieves all of the serial values for referenced objects and places them into the instance 
        variables, Validates, Normalizes, and serializes the object (with a save of the persistent image if persistent).\n
        This method is not meant to be called directly. It is called by %Save and by %GetSwizzleObject.
        """
        ...
    
    def _ValidateObject(self, unused: int = 0, checkserial: int = 1) -> Status:
        """
        This method validates an object.\n
        The %Save() method of a persistent class calls this method before filing any objects in the database. The 
        %ValidateObject() of a referencing object can call it. You can also call it explicitly at any time.\n
        %ValidateObject() does the following:\n
        - 1. If present, it will call a user-supplied %OnValidateObject() method.\n
        - 2. It checks if any required property values are missing.\n
        - 3. If the PROPERTYVALIDATION class parameter is set to ValidateOnSave, it validates each non-null property 
        value by calling the property method IsValid on each literal property and the %ValidateObject method for each 
        object-valued embedded object property (properties whose type extend %SerialObject).\n
        - 4. If checkserial is 1, it forces the checking of any embedded object properties by calling their 
        %ValidateObject method after swizzling this property.\n
        - 5. If checkserial is 2, it forces the checking of any collections of serial types by iterating over those 
        collections and calling their %ValidateObject() method after swizzling this property, in addition to the 
        validation that occurs when checkserial is 1.\n
        %ValidateObject() returns a %Status indicating success or error. It is up to the caller to process the error 
        value.\n
        %ValidateObject() does not validate object-valued reference properties (properties whose type extends 
        %Persistent) due to the possibility of circular dependencies between objects. The %Save() method of a 
        persistent class automatically detects and handles circular references between objects. If you require the 
        validation of reference properties, you can override this method in a subclass or call %Save() directly.
        """
        ...
