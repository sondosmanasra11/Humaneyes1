import Unit_SetUp
import time
def Test1():
  Unit_SetUp.SetUp()
  ProcessSys=Sys.Process("HumaneyesVRStudio")
  VuzeApp =ProcessSys.QtObject("VuzeApp", "Humaneyes VR Studio 1.1.3573", 1)
  app_area=VuzeApp.QtObject("QFrame", "", 1).QtObject("app_area")
  QStackedWidget=app_area.QtObject("QSplitter", "", 1).QtObject("QStackedWidget", "", 1)
  HE_ToolButton3=QStackedWidget.QtObject("quick_launch").QtObject("HE_ToolButton", "Render\nany media or project\nfor viewing and sharing", 3)
  HE_ToolButton3.Click()
  time.sleep(3)

