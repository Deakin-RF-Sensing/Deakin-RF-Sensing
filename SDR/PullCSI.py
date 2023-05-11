from picoscenes import  Picoscenes
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def save_CSI(source_filename,save_filename):
 MyA = []

 frames = Picoscenes(source_filename)

 for x in frames.raw:
  #MyA.append([x.get("RxSBasic").get("timestamp"),x.get("CSI").get("CSI")])
  MyA.append([x.get("RxSBasic").get("systemns"),datetime.utcfromtimestamp(x.get("RxSBasic").get("systemns")/1000000000), x.get("CSI").get("CSI")])
 CSI = np.array(MyA)
 np.save(save_filename,CSI)



# use save_CSI to save CSI data to a numpy array
# arguments are the source file and the save file

#save_CSI("2023-03-01-Test1/SDR_Test1-ArmsUp1643.csi","2023-03-01-Test1/CSI_Test1-ArmsUp1643")
#save_CSI("2023-03-01-Test1/SDR_Test2ArmsYShape1647.csi","2023-03-01-Test1/CSI_Test2ArmsYShape1647")
#save_CSI("2023-03-01-Test1/SDR_Test3ArmsLow1652.csi","2023-03-01-Test1/CSI_Test3ArmsLow1652")
#save_CSI("2023-03-01-Test1/SDR_Test4NutralRight.csi","2023-03-01-Test1/CSI_Test4NutralRight")
#save_CSI("2023-03-01-Test1/SDR_Test5NutralLeft.csi","2023-03-01-Test1/CSI_Test5NutralLeft")
#save_CSI("2023-03-01-Test1/SDR_Test6NutralCentre.csi","2023-03-01-Test1/CSI_Test6NutralCentre")
#save_CSI("2023-03-01-Test1/SDR_Test7Sitting.csi","2023-03-01-Test1/CSI_Test7Sitting")
#save_CSI("2023-03-01-Test1/SDR_Test8MultiPose.csi","2023-03-01-Test1/CSI_Test8MultiPose")
save_CSI("2023-03-01-Test2/SDR_AltAP_Test1_MultiPose.csi","2023-03-01-Test2/CSI_AltAP_Test1_MultiPose")



#Command for loading the numpy array
#np.load("CSI_Test1-ArmsUp1643.npy",allow_pickle=True)


