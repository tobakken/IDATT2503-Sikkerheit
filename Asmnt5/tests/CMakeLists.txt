
add_executable(encode_fuzzer encode_fuzzer_test.c)
target_link_libraries(encode_fuzzer utility)
target_compile_options(encode_fuzzer PRIVATE -fsanitize=fuzzer,address)
target_link_options(encode_fuzzer PRIVATE -fsanitize=fuzzer,address)

