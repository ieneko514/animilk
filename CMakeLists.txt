cmake_minimum_required(VERSION 3.16)
project(animilk CXX)

find_package(Qt6 REQUIRED COMPONENTS Core)

qt6_add_resources(RES_SRC res.qrc OPTIONS --generator python)

add_custom_target(res_py ALL
  DEPENDS ${RES_SRC}
  COMMAND ${CMAKE_COMMAND} -E copy_if_different ${RES_SRC} ${CMAKE_CURRENT_SOURCE_DIR}/res.py)
