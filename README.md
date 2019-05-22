# rpi_gige_v_framework
ROS package providing a basic Python API to access DALSA GigE cameras using OpenCV and numpy. Tested with DALSA Genie Nano C2450. See "Issues" section for know issues.

The [DALSA GigE-V Framework for Linux](https://www.teledynedalsa.com/imaging/products/software/linux-gige-v/) must be installed. Be sure to run 'corinstall' and then logout/login to fully install the framework.

Interfaces to the GevApi library were generated using [ctypesgen.py](https://github.com/davidjamesca/ctypesgen).

# usage:
`rosrun rpi_gige_v_framework ros_image_publisher`

or

`rosrun rpi_gige_v_framework ros_image_publisher show_image=true`