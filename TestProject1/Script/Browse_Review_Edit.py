import Main_page
import Unit_SetUp
import time
def Test_Browse():
  Unit_SetUp.SetUp()
  ProcessSys=Sys.Process("HumaneyesVRStudio")
  VuzeApp =ProcessSys.QtObject("VuzeApp", "Humaneyes VR Studio 1.1.3573", 1)
  app_area=VuzeApp.QtObject("QFrame", "", 1).QtObject("app_area")
  QStackedWidget=app_area.QtObject("QSplitter", "", 1).QtObject("QStackedWidget", "", 1)
  HE_ToolButton2=QStackedWidget.QtObject("quick_launch").QtObject("HE_ToolButton", "Preview and Edit\nprojects or media\nyou\'ve already imported", 2)
  HE_ToolButton2.Click()
  time.sleep(3)
  QStackedWidget2=QStackedWidget.QtObject("ProjectViewWidget", "", 1).QtObject("QStackedWidget", "", 1).QtObject("player_empty_area")
  Browse=QStackedWidget2.QtObject("HE_ToolButton", "Browse", 2)
  Browse.Click()