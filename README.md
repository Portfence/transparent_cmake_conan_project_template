# transparent_cmake_conan_project_template

## install dependencies
```
$ conan install . -if build
```

## build project
```
$ conan build . -bf build
```

## Create package
```
$ conan create . <user>/<channel>
```
e.g.
```
$ conan create . project/stable
```
