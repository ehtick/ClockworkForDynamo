import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def DetailLevel(view):
	if hasattr(view, "DetailLevel"): return System.Enum.GetName(ViewDetailLevel, view.DetailLevel)
	else: return None

views = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [DetailLevel(x) for x in views]
else: OUT = DetailLevel(views)