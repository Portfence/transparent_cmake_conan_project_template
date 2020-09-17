add_executable(test_${PROJECT_NAME}
  doctest.cpp
  my_class_test.cpp
)

target_compile_features(test_${PROJECT_NAME}
  PRIVATE cxx_std_20
)

target_link_libraries(test_${PROJECT_NAME}
  PRIVATE ${PROJECT_NAME}::${PROJECT_NAME}
  PRIVATE doctest::doctest
  PRIVATE trompeloeil::trompeloeil
)

set_target_properties(test_${PROJECT_NAME}
  PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)
