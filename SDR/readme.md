# SDR Setup

Follow installation instructions for PicoScenes this will also install UHD for the USRP our model used was a n200.
see section [4.1.2. Installation of (Multiple) USRP Devices](https://ps.zpj.io/installation.html#installation-of-multiple-usrp-devices)

# CSI capture

Once PicoScenes has been installed the USRP is setup configured and you have verified connectivity with uhd_find_devices and uhd_usrp_probe you can use the following command to capture CSI data.

`PicoScenes "-i usrp192.168.10.2 --mode logger --freq 5.220e+09 --rx-cbw 20 --rx-channel 0 --rx-ant TX/RX --rx-gain 15 --transfer-type 8"`

The above command was configured for our N200 unit change -i usrp192.168.10.2 to match your units Ip address adjust freq to match the WiFi frequency you wish to capture the above represents 5GHz channel 44 at 5220MHz see https://en.wikipedia.org/wiki/List_of_WLAN_channels for a quick break down of 5GHz channels.

# Read CSI

## Install PicoScenes-Python-Toolbox

PicoScenes CSI data can be read with Matlab or python for our project Python was used follow the instructions on
[PicoScenes Python Toolbox ](https://gitlab.com/wifisensing/PicoScenes-Python-Toolbox) to install the tool box.

## Convert CSI data to NumPy array

Once the PicoScenes-Python-Toolbox tool box is installed you can use PullCSI.py to convert the PicoScenes CSI data into the NumPy array.
Modify the file to target the source CSI data and provide the file name for the NumPy Array.
e.g.
`save_CSI("2023-03-01-Test2/SDR_AltAP_Test1_MultiPose.csi","2023-03-01-Test2/CSI_AltAP_Test1_MultiPose")`
