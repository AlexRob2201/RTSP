# RTSP
RTSP SERVER 
# RS tool v0.3.4
# FTP tool v.0.0.1

The utility uses RTSP streams to save photos from them for a certain period of time.

## Description

rtsp_data.db - An SQL database stores data for the following fields.
    ├── RTSP stream 
    ├── Device Name
    ├── interval
    └── save path
ftp_data.conf -   Logging file related to FTP
RTSPMonitor.txt - Logging file related to RTSP monitor
ftp_data.conf -   File where FTP connection data is stored

## Structure

project_folder/
    ├── RS_tool.py
    ├── rtsp_data.db
    ├── ftp_data.conf
    ├── ftp_log.txt
    ├── RTSPMonitor.txt
    └── README.md

# # Minimum System Requirements for a PC Handling 5 Simultaneous Video Streams and a Graphical Interface

For the proper functioning of the program handling 5 simultaneous video streams along with a graphical interface, it is recommended to use the following computer specifications:

- **Processor:** At least an Intel Core i5 or equivalent AMD processor with a clock speed of no less than 2.5 GHz.

- **Memory:** A minimum of 8 GB of RAM.

- **Graphics Card:** A video card with hardware-accelerated video support (e.g., NVIDIA GeForce or AMD Radeon).

- **Storage:** Free disk space of no less than 20 GB for storing video files and the program.

- **Operating System:** Windows 10 or Linux (e.g., Ubuntu).

- **Monitor:** Screen resolution of no less than 1920x1080.

Please note that actual requirements may be higher depending on the complexity of video processing and other factors. It is also advisable to ensure that the appropriate drivers for the graphics card and other components are optimized for maximum performance.

Note: Before using the program, check for driver updates and monitor system resource usage when working with a large number of video streams.

   
    
    
