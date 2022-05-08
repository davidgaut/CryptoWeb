# # syntax=docker/dockerfile:1
# # FROM python:3.8-alpine
# # RUN pip3 install pandas
# # WORKDIR /CryptoWeb
# # ENV FLASK_APP=app.py
# # ENV FLASK_RUN_HOST=0.0.0.0
# # RUN apk add --no-cache gcc musl-dev linux-headers
# # COPY requirements.txt requirements.txt
# # RUN pip install -r requirements.txt
# # EXPOSE 5000
# # COPY . .
# # CMD ["flask", "run"]

# FROM alpine:latest

# WORKDIR /CryptoWeb

# # SOFTWARE PACKAGES
# #   * musl: standard C library
# #   * lib6-compat: compatibility libraries for glibc
# #   * linux-headers: commonly needed, and an unusual package name from Alpine.
# #   * build-base: used so we include the basic development packages (gcc)
# #   * bash: so we can access /bin/bash
# #   * git: to ease up clones of repos
# #   * ca-certificates: for SSL verification during Pip and easy_install
# #   * freetype: library used to render text onto bitmaps, and provides support font-related operations
# #   * libgfortran: contains a Fortran shared library, needed to run Fortran
# #   * libgcc: contains shared code that would be inefficient to duplicate every time as well as auxiliary helper routines and runtime support
# #   * libstdc++: The GNU Standard C++ Library. This package contains an additional runtime library for C++ programs built with the GNU compiler
# #   * openblas: open source implementation of the BLAS(Basic Linear Algebra Subprograms) API with many hand-crafted optimizations for specific processor types
# #   * tcl: scripting language
# #   * tk: GUI toolkit for the Tcl scripting language
# #   * libssl1.0: SSL shared libraries
# ENV PACKAGES="\
#     dumb-init \
#     musl \
#     libc6-compat \
#     linux-headers \
#     build-base \
#     bash \
#     git \
#     ca-certificates \
#     freetype \
#     libgfortran \
#     libgcc \
#     libstdc++ \
#     openblas \
#     tcl \
#     tk \
#     libssl1.0 \
# "

# # PYTHON DATA SCIENCE PACKAGES
# #   * numpy: support for large, multi-dimensional arrays and matrices
# #   * matplotlib: plotting library for Python and its numerical mathematics extension NumPy.
# #   * scipy: library used for scientific computing and technical computing
# #   * scikit-learn: machine learning library integrates with NumPy and SciPy
# #   * pandas: library providing high-performance, easy-to-use data structures and data analysis tools
# #   * nltk: suite of libraries and programs for symbolic and statistical natural language processing for English
# ENV PYTHON_PACKAGES="\
#     numpy \
#     matplotlib \
#     pandas \
# " 

# EXPOSE 5000
# COPY . .
# CMD ["flask", "run"]

# Base image
FROM python:3.8
# Creation of a working directory app
WORKDIR /app
# Copy all the files of this project inside the container
COPY . .
# Installation of code dependencies
RUN pip install -r requirements.txt
# Installation of spacy model
# RUN python -m spacy download en_core_web_sm
# Command to be executed when the container is launched
# CAREFUL - use the special IP 0.0.0.0 inside a container
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]