
#----------------------------------------------#
#-------------Configure CMake------------------#
#----------------------------------------------#

cmake_minimum_required(VERSION 3.14)

project(market)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_BUILD_TYPE Release)

 #Add the include directories

 include_directories(include)
 include_directories(external)


 #setup the global variable SRC_FILES to target
 #files to be compiled



#----------------------------------------------#
#-------------Setup Doxygen--------------------#
#----------------------------------------------#
find_package(Doxygen)

if (DOXYGEN_FOUND)
    # set input and output files
    set(DOXYGEN_IN ${CMAKE_CURRENT_SOURCE_DIR}/docs/Doxyfile)
    set(DOXYGEN_OUT ${CMAKE_CURRENT_BINARY_DIR}/../docs/Doxyfile)

    # request to configure the file
    configure_file(${DOXYGEN_IN} ${DOXYGEN_OUT} @ONLY)
    message("Doxygen build started")

    # note the option ALL which allows to build the docs together with the application
    add_custom_target( doc_doxygen ALL
        COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYGEN_OUT}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen"
        VERBATIM )
else (DOXYGEN_FOUND)
  message("Doxygen need to be installed to generate the doxygen documentation")
endif (DOXYGEN_FOUND)

#----------------------------------------------#
#----Download and configure GOOGLE-Test--------#
#----------------------------------------------#
include(FetchContent)
# Workaround for CMake >= 3.24
# Avoid warning about DOWNLOAD_EXTRACT_TIMESTAMP
if (CMAKE_VERSION VERSION_GREATER_EQUAL "3.24.0")
  cmake_policy(SET CMP0135 NEW)
endif()





find_package(pybind11 REQUIRED)

#Create Variable to specify the source files to be compiled
file(GLOB SRC_FILES ${PROJECT_SOURCE_DIR}/src/*.cpp)



#----------------------------------------------#
#-------------------Pybind---------------------#
#----------------------------------------------#

#add pybind-modules
pybind11_add_module(market
  extra/pybind_files/pybind-market.cpp
  ${SRC_FILES}
)

pybind11_add_module(trader
  extra/pybind_files/pybind-trader.cpp
  ${SRC_FILES}
)

pybind11_add_module(good
  extra/pybind_files/pybind-good.cpp
  ${SRC_FILES}
)

pybind11_add_module(account
  extra/pybind_files/pybind-account.cpp
  ${SRC_FILES}
)

#install pybind-modules
install(TARGETS market
  COMPONENT python
  LIBRARY DESTINATION "${PROJECT_SOURCE_DIR}/extra")

install(TARGETS trader
  COMPONENT python
  LIBRARY DESTINATION "${PROJECT_SOURCE_DIR}/extra")
  
install(TARGETS good
  COMPONENT python
  LIBRARY DESTINATION "${PROJECT_SOURCE_DIR}/extra")

install(TARGETS account
  COMPONENT python
  LIBRARY DESTINATION "${PROJECT_SOURCE_DIR}/extra")

#install pybind-modules into the other directory
install(TARGETS market
  COMPONENT python
  LIBRARY DESTINATION "${PROJECT_SOURCE_DIR}/extra/GUI")

install(TARGETS trader
  COMPONENT python
  LIBRARY DESTINATION "${PROJECT_SOURCE_DIR}/extra/GUI")
  
install(TARGETS good
  COMPONENT python
  LIBRARY DESTINATION "${PROJECT_SOURCE_DIR}/extra/GUI")

install(TARGETS account
  COMPONENT python
  LIBRARY DESTINATION "${PROJECT_SOURCE_DIR}/extra/GUI")
#----------------------------------------------#
#-------------Creating main-executables--------#
#----------------------------------------------#

add_executable(demo
examples/demo.cpp
${SRC_FILES}
)

add_executable(t
examples/test.cpp
${SRC_FILES}
)


#----------------------------------------------#
#-------------Creating test programs-----------#
#----------------------------------------------#

