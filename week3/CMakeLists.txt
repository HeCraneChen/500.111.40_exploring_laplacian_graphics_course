cmake_minimum_required(VERSION 3.16)
project(HelloGraphics)

list(PREPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

# Eigen
if(WIN32)
    # On Windows, include Eigen from the local source directory
    include_directories(${CMAKE_CURRENT_SOURCE_DIR}/eigen)
else()
    # On other operating systems, use find_package
    find_package(Eigen3 REQUIRED)
    include_directories(${EIGEN3_INCLUDE_DIR})
endif()

# Libigl
include(libigl)

# Enable the targets
igl_include(core)
igl_include(copyleft cgal)


# polyscope
add_subdirectory("polyscope")


# Add your project files
file(GLOB SRC_FILES *.cpp)
add_executable(${PROJECT_NAME} ${SRC_FILES})
target_link_libraries(${PROJECT_NAME} PUBLIC igl_copyleft::cgal polyscope)