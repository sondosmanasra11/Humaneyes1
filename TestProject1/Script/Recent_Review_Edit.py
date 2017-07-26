import Main_page
import Unit_SetUp
import time
def Test_Recent():
  Unit_SetUp.SetUp()
  ProcessSys=Sys.Process("HumaneyesVRStudio")
  VuzeApp =ProcessSys.QtObject("VuzeApp", "Humaneyes VR Studio 1.1.3573", 1)
  app_area=VuzeApp.QtObject("QFrame", "", 1).QtObject("app_area")
  QStackedWidget=app_area.QtObject("QSplitter", "", 1).QtObject("QStackedWidget", "", 1)
  HE_ToolButton=QStackedWidget.QtObject("quick_launch").QtObject("HE_ToolButton", "Preview and Edit\nprojects or media\nyou\'ve already imported", 2)
  HE_ToolButton.Click()
  time.sleep(6)
  QStackedWidget2=QStackedWidget.QtObject("ProjectViewWidget", "", 1).QtObject("QStackedWidget", "", 1).QtObject("player_empty_area")
  Recent=QStackedWidget2.QtObject("HE_ToolButton", "Recent", 1)
  Recent.Click()
  app_area.QtObject("QSplitter", "", 1).QtObject("RecentViewWidget", "", 1).QtObject("QStackedWidget", "", 1).QtObject("VuzeViewWidget", "", 2).QtObject("QScrollArea", "", 1).QtObject("qt_scrollarea_viewport").QtObject("QWidget", "", 1).QtObject("VuzeViewItem", "", 1).QtObject("vuzeitem_type_thumb").DblClick()
  time.sleep(3)
  
  PlayerAreaWidget=QStackedWidget.QtObject("ProjectViewWidget", "", 1).QtObject("QStackedWidget", "", 1).QtObject("PlayerAreaWidget", "", 1)
  player_controls=PlayerAreaWidget.QtObject("player_controls").QtObject("QFrame", "", 2)
  Center_Button=player_controls.QtObject("HE_PushButton", "", 6).Click()
  time.sleep(3)
  QStackedWidget.QtObject("ProjectViewWidget", "", 1).QtObject("project_tools").QtObject("HE_PushButton", "",3).Click()
  PlayerAreaWidget.QtObject("HorizontalFOVTool", "", 1).Drag(98, 174, 221, 48)
  time.sleep(3)
#  
#  QStackedWidget.QtObject("ProjectViewWidget", "", 1).QtObject("explore_buttons").QtObject("HE_PushButton","Save",1).Click()
#  dialog_content=ProcessSys.QtObject("SaveProjectDialog", "", 1).QtObject("dialog_content")
#  LineEdit=dialog_content.QtObject("QFrame", "", 1).QtObject("QLineEdit", "", 1)
#  LineEdit.Click() 
#  LineEdit.Keys("Center_160")
#  time.sleep(3)
#  Save_Button=ProcessSys.dialog_content.QtObject("HE_PushButton", "Save", 3)