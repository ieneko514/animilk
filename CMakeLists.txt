cmake_minimum_required(VERSION 3.20)
project(animilk CXX)

find_package(Qt6 REQUIRED COMPONENTS Widgets)

qt6_add_resources(RES_SRC res.qrc OPTIONS --generator python)

add_custom_target(res_py ALL
  DEPENDS ${RES_SRC}
  COMMAND ${CMAKE_COMMAND} -E copy_if_different ${RES_SRC} ${CMAKE_CURRENT_SOURCE_DIR}/res.py)

qt6_wrap_ui(UI_SRCS
  anime_chooser.ui
  new_anime.ui
  OPTIONS -g python)

foreach(UI_SRC IN LISTS UI_SRCS)
  cmake_path(GET UI_SRC FILENAME UI_BASENAME)
  string(REGEX REPLACE "\\.h$" "" UI_NAME ${UI_BASENAME})
  add_custom_target(${UI_NAME}_py ALL
    DEPENDS ${UI_SRC}
    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${UI_SRC} ${CMAKE_CURRENT_SOURCE_DIR}/${UI_NAME}.py)
endforeach()
