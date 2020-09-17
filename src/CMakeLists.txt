add_library(${PROJECT_NAME} SHARED
  my_class.cpp
)

target_compile_features(${PROJECT_NAME}
  PRIVATE cxx_std_20
)

target_compile_options(${PROJECT_NAME}
  PRIVATE -Wall
  PRIVATE -Wextra
  PRIVATE -Wshadow
  PRIVATE -Wnon-virtual-dtor
  PRIVATE -Wpedantic
)

target_link_libraries(${PROJECT_NAME}
  PRIVATE Threads::Threads
)

add_library(${PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_include_directories(${PROJECT_NAME}
  PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
  PUBLIC $<INSTALL_INTERFACE:include>
  PRIVATE src
)

# # ############ INSTALL TARGET ############
include(GNUInstallDirs)

# # Install public header directory mylibrary/ in /usr/local/include/
install(DIRECTORY ${CMAKE_SOURCE_DIR}/include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# # Install libMyLibrary.so in /usr/local/lib/
install(TARGETS ${PROJECT_NAME}
  EXPORT         ${PROJECT_NAME}-export
  LIBRARY        DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE        DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

# # Create and install CXXProjectConanTargets.cmake in lib/cmake/CXXProjectConan/ from the export defined above
install(EXPORT ${PROJECT_NAME}-export
  FILE         ${PROJECT_NAME}Targets.cmake
  NAMESPACE    ${PROJECT_NAME}::
  DESTINATION  ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
)

# Generate CXXProjectConanConfig.cmake from cmake/CXXProjectConanConfig.cmake.in
# CXXProjectConanConfig includes CXXProjectConanTargets.cmake to find the transitive dependencies
include(CMakePackageConfigHelpers)
configure_package_config_file(
    ${PROJECT_SOURCE_DIR}/cmake/${PROJECT_NAME}Config.cmake.in
    ${CMAKE_BINARY_DIR}/${PROJECT_NAME}Config.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
)

# Install CXXProjectConanConfig.cmake in lib/cmake/CXXProjectConan
# find_package(CXXProjectConan CONFIG REQUIRED)
# link with CXXProjectConan::CXXProjectConan
install(FILES
    ${CMAKE_BINARY_DIR}/${PROJECT_NAME}Config.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
)
