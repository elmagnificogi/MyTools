cmake_minimum_required(VERSION 3.10)   # 指定最低 CMake 版本
project(MyProject1 VERSION 1.0)          # 定义项目名称和版本

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(${PROJECT_SOURCE_DIR}/include)

# 创建可执行文件目标
add_executable(MyExecutable ${PROJECT_SOURCE_DIR}/src/main.cpp)
