cmake_minimum_required(VERSION 3.0.2)
project(PIXYSDK)
set(PIXYSDK_VERSION master)

if(NOT EXTERNAL_INSTALL_LOCATION)
  set(EXTERNAL_INSTALL_LOCATION ${CMAKE_BINARY_DIR}/external)
endif()

#############
## Library ##
#############
file(MAKE_DIRECTORY ${EXTERNAL_INSTALL_LOCATION}/include)
file(MAKE_DIRECTORY ${EXTERNAL_INSTALL_LOCATION}/lib)

include(ExternalProject)
ExternalProject_Add(PIXY_SDK_IMPORT
  SOURCE_DIR ${EXTERNAL_INSTALL_LOCATION}/src
  URL https://github.com/charmedlabs/pixy/archive/${PIXYSDK_VERSION}.tar.gz
  BINARY_DIR ${EXTERNAL_INSTALL_LOCATION}/src/scripts
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ${EXTERNAL_INSTALL_LOCATION}/src/scripts/build_libpixyusb_swig.sh
  INSTALL_COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/install-pixy ${EXTERNAL_INSTALL_LOCATION} ${PIXY_NODE_SOURCE_DIR}
)

#############
## Install ##
#############
install(
  DIRECTORY ${EXTERNAL_INSTALL_LOCATION}/lib/
  DESTINATION lib/
)

install(
  DIRECTORY ${EXTERNAL_INSTALL_LOCATION}/include/
  DESTINATION include
)

## Mark executables and/or libraries for installation
export(PACKAGE ${PROJECT_NAME})
