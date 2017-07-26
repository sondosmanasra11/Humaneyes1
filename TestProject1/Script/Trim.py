import Unit_SetUp
import time
 
def Test_import():
  #Launch the application
  Unit_SetUp.SetUp()
  time.sleep(3)
  
  #Detect the application process
  ProcessSys=Sys.Process("HumaneyesVRStudio")
  VuzeApp =ProcessSys.QtObject("VuzeApp", "Humaneyes VR Studio 1.1.3573", 1)
  app_area=VuzeApp.QtObject("QFrame", "", 1).QtObject("app_area")
  
  #Detect the Import button
  QStackedWidget=app_area.QtObject("QSplitter", "", 1).QtObject("QStackedWidget", "", 1)
  HE_ToolButton2=QStackedWidget.QtObject("quick_launch").QtObject("HE_ToolButton", "Import\nto start editing in studio", 1)
  HE_ToolButton2.Click()
  time.sleep(3)
  
  #Select video folder 
  importViewWidget = QStackedWidget.QtObject("ImportViewWidget", "", 1)
  HE_PushButton=importViewWidget.QtObject("HE_TabBar", "", 1).QtObject("HE_PushButton", "", 2).Click()
  time.sleep(3)
  
  dialog_content=ProcessSys.QtObject("MediaBrowserWidget", "", 1).QtObject("dialog_content")
  Select=dialog_content.QtObject("HE_PushButton", "Select", 3).Click()
  time.sleep(3)
  
  #Select a file to import
  QScrollArea=importViewWidget.WaitQtObject("QStackedWidget", "", 1).QtObject("VuzeViewWidget", "", 1).QtObject("QScrollArea", "", 1)
  VuzeViewItem2=QScrollArea.QtObject("qt_scrollarea_viewport").QtObject("QWidget", "", 1).QtObject("VuzeViewItem", "", 2).QtObject("vuzeitem_type_thumb")
  VuzeViewItem2.ClickR()
  time.sleep(2)  
  importViewWidget.QtObject("explore_buttons").QtObject("HE_PushButton", "Import", 2).Click()
  time.sleep(2)
  
  #Select a video to Preview & Edit
  ImportDialog=ProcessSys.QtObject("ImportDialog", "", 1)
  Import_Button=ImportDialog.QtObject("dialog_content").QtObject("HE_PushButton", "Import", 3).Click()
  time.sleep(2)
  
  QScrollArea=app_area.QtObject("QSplitter", "", 1).QtObject("RecentViewWidget", "", 1).QtObject("QStackedWidget", "", 1).QtObject("VuzeViewWidget", "", 1).QtObject("QScrollArea", "", 1)
  scrollBar =QScrollArea.QtObject("qt_scrollarea_vcontainer").QtObject("QScrollBar", "", 1)
  scrollBar.wPosition = 0
  QScrollArea.QtObject("qt_scrollarea_viewport").QtObject("QWidget", "", 1).QtObject("VuzeViewItem", "",1).QtObject("vuzeitem_type_thumb").DblClick()
  time.sleep(2)
  
#  #Save the project
#  QStackedWidget.QtObject("ProjectViewWidget", "", 1).QtObject("explore_buttons").QtObject("HE_PushButton", " Save ", 1).Click()
# 
#  dialog_content=ProcessSys.QtObject("SaveProjectDialog", "", 1).QtObject("dialog_content")
#  LineEdit=dialog_content.QtObject("QFrame", "", 1).QtObject("QLineEdit", "", 1)
#  LineEdit.Click() 
#  LineEdit.Keys("Center_160")
#  time.sleep(2)
#  ProcessSys.QtObject("SaveProjectDialog", "", 1).QtObject("dialog_content").QtObject("HE_PushButton", "Save", 3).Click()
#  
