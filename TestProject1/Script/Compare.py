 
def Compare():
  
  path1="C:\\Users\\wisam\\Humaneyes VR Studio\\Renders\\rendered_file.mp4"
  path2="C:\\Users\\wisam\\Humaneyes VR Studio\\Renders\\test3d.mp4"
  
  myFile = aqFile.OpenBinaryFile(path1,aqFile.faRead)
  s = myFile.ReadByte()
  Log.Message(s)
  myFile.Close()

  myFile2 = aqFile.OpenBinaryFile(path2,aqFile.faRead)
  s = myFile2.ReadByte()
  Log.Message(s)    
  myFile2.Close()

  if aqFile.Compare(path1, path2):
      Log.Message("they are equal")
  else:
      Log.Message("Not Equal")
      
  size=aqFile.GetSize(path1)
  Log.Message(size)
  
  size1=aqFile.GetSize(path2)
  Log.Message(size1)
 