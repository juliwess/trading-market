
#----------------------------------------------#
#-------------Configure CMake------------------#
#----------------------------------------------#

cmake_minimum_required(VERSION 3.14)

project(market)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_BUILD_TYPE Release)
# Optional: Prüfe alle Targets auf Speicherlecks
 add_compile_options(-fsanitize=address)
 add_link_options(-fsanitize=address)

 #Add the include directories

 include_directories(include)
 include_directories(external)


 #setup the global variable SRC_FILES to target
 #files to be compiled
 file(GLOB SRC_FILES
  ${PROJECT_SOURCE_DIR}/src/*.cpp)



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

# Download GoogleTest (we use version 1.12.1)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# Workaround for Windows:
# Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Include CMake configuration of GoogleTest
FetchContent_MakeAvailable(googletest)
include(GoogleTest)

# Enable GoogleTest
enable_testing()




#----------------------------------------------#
#-------------Creating main-executables--------#
#----------------------------------------------#


add_executable(demo
examples/demo.cpp
${SRF_FILES})


#----------------------------------------------#
#-------------Creating test programs-----------#
#----------------------------------------------#

add_executable(test1
tests/test1.cpp
${SRC_FILES})
target_link_libraries(test1 GTest::gtest_main)
gtest_discover_tests(test1)