cmake_minimum_required(VERSION 3.2 FATAL_ERROR)

add_compile_options(-Wall)
add_compile_options(-Wno-uninitialized)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(reqclient
    reqclient.cc
)
target_include_directories(reqclient PRIVATE
    $ENV{CONDA_PREFIX}/include
)
target_link_libraries(reqclient
    zmq
    xtcdata::xtc
)
install(TARGETS reqclient
    RUNTIME DESTINATION bin
)
