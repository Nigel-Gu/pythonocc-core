from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *

#the following typedef cannot be wrapped as is
TopLoc_IndexedMapOfLocation = NewType('TopLoc_IndexedMapOfLocation', Any)
#the following typedef cannot be wrapped as is
TopLoc_MapIteratorOfMapOfLocation = NewType('TopLoc_MapIteratorOfMapOfLocation', Any)
#the following typedef cannot be wrapped as is
TopLoc_MapLocationHasher = NewType('TopLoc_MapLocationHasher', Any)
#the following typedef cannot be wrapped as is
TopLoc_MapOfLocation = NewType('TopLoc_MapOfLocation', Any)

class TopLoc_Datum3D(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, T: gp_Trsf) -> None: ...
	def Form(self) -> gp_TrsfForm: ...
	def Transformation(self) -> gp_Trsf: ...
	def Trsf(self) -> gp_Trsf: ...

class TopLoc_ItemLocation:
	def __init__(self, D: TopLoc_Datum3D, P: int) -> None: ...

class TopLoc_Location:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, T: gp_Trsf) -> None: ...
	@overload
	def __init__(self, D: TopLoc_Datum3D) -> None: ...
	def Divided(self, Other: TopLoc_Location) -> TopLoc_Location: ...
	def FirstDatum(self) -> TopLoc_Datum3D: ...
	def FirstPower(self) -> int: ...
	def HashCode(self, theUpperBound: int) -> int: ...
	def Identity(self) -> None: ...
	def Inverted(self) -> TopLoc_Location: ...
	def IsDifferent(self, Other: TopLoc_Location) -> bool: ...
	def IsEqual(self, Other: TopLoc_Location) -> bool: ...
	def IsIdentity(self) -> bool: ...
	def Multiplied(self, Other: TopLoc_Location) -> TopLoc_Location: ...
	def NextLocation(self) -> TopLoc_Location: ...
	def Powered(self, pwr: int) -> TopLoc_Location: ...
	def Predivided(self, Other: TopLoc_Location) -> TopLoc_Location: ...
	def Transformation(self) -> gp_Trsf: ...

class TopLoc_SListNodeOfItemLocation(Standard_Transient):
	def __init__(self, I: TopLoc_ItemLocation, aTail: TopLoc_SListOfItemLocation) -> None: ...
	def Tail(self) -> TopLoc_SListOfItemLocation: ...
	def Value(self) -> TopLoc_ItemLocation: ...

class TopLoc_SListOfItemLocation:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, anItem: TopLoc_ItemLocation, aTail: TopLoc_SListOfItemLocation) -> None: ...
	@overload
	def __init__(self, Other: TopLoc_SListOfItemLocation) -> None: ...
	@overload
	def __init__(self, theOther: TopLoc_SListOfItemLocation) -> None: ...
	def Assign(self, Other: TopLoc_SListOfItemLocation) -> TopLoc_SListOfItemLocation: ...
	def Clear(self) -> None: ...
	def Construct(self, anItem: TopLoc_ItemLocation) -> None: ...
	def IsEmpty(self) -> bool: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Tail(self) -> TopLoc_SListOfItemLocation: ...
	def ToTail(self) -> None: ...
	def Value(self) -> TopLoc_ItemLocation: ...

# harray1 classes
# harray2 classes
# hsequence classes
