## Get the code

Option1:

Download the zip

Option2:

    git clone https://github.com/HeCraneChen/exploring_laplacian_graphics_course.git --recursive



## MacOS (terminal)

**Compile**

    cd week3
    cd HelloGraphics
    mkdir build
    cd build
    cmake ..
    make

**Run**

    ./HelloGraphics

## Windows (Visual Studio)

**Compile**

Open the Visual Studio IDE, and click the following

`Open a local folder` and open the total-curvature-estimation folder cloned from this repo

`File`  `Open`  `CMake...` and open the CMakeLists.txt

`Build`  `Build All`


**Run**

    cd total-curvature-estimation
    
    mkdir build
    
    scp ./out/build/x64-Debug/TotalCurvature.exe ./build/TotalCurvature.exe
    
    scp ./out/build/x64-Debug/_deps/gmp-src/lib/libgmp-10.dll ./build/libgmp-10.dll
    
    cd build
    
    TotalCurvature --in ../example_data/cow.ply --out ../results/cow_mesh.txt --format mesh
    
    TotalCurvature --in ../example_data/cow_points.ply ../example_data/cow_normals.ply --out ../results/cow_cloud.txt --format point_cloud
    



