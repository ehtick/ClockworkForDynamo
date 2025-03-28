import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

def IsCategoryVisibleInView(cat, view):
	if view.GetCategoryHidden(cat.Id): return False
	else: return True

cats = IN[0]
views = UnwrapElement(IN[1])

if isinstance(IN[0], list):
	if isinstance(IN[1], list):  OUT = [[IsCategoryVisibleInView(x, y) for x in cats] for y in views]
	else: OUT = [IsCategoryVisibleInView(x, views) for x in cats]
else:
	if isinstance(IN[1], list): OUT = [IsCategoryVisibleInView(cats, x) for x in views]
	else: OUT = IsCategoryVisibleInView(cats, views)