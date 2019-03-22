cmake_minimum_required(VERSION 3.0.2)
project(pixy_node)

set(PIXY_NODE_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
add_subdirectory(pixysdk)
find_package(catkin REQUIRED COMPONENTS actionlib_msgs message_generation rospy std_msgs)

catkin_python_setup()

catkin_package(
  LIBRARIES pixy_node
  CATKIN_DEPENDS message_runtime rospy std_msgs
)

catkin_install_python(PROGRAMS bin/pixy_node
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

set(PIXYSDK_EXTERNAL_LIB_DIR ${CMAKE_BINARY_DIR}/external/lib)
install(
  DIRECTORY ${PIXYSDK_EXTERNAL_LIB_DIR}/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

#install(PROGRAMS
#  src/pixy_node.py
#  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)

#install(DIRECTORY
#  config
#  launch
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
#)
