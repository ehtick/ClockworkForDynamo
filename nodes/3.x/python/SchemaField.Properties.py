import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def FieldProperties(field):
	if hasattr(field, "FieldName"):
		return field.FieldName, field.Documentation, System.Enum.GetName(ExtensibleStorage.ContainerType, field.ContainerType), field.GetSpecTypeId(), field.ValueType, field.SubSchema, field.SubSchemaGUID
	else: return None, None, None, None, None, None, None

fields = IN[0]

if isinstance(IN[0], list): OUT = map(list, zip(*[FieldProperties(x) for x in fields]))
else: OUT = FieldProperties(fields)