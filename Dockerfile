# Use Python 3.9.18 with ARM64 support for Apple Silicon
FROM --platform=linux/arm64 python:3.9.18-slim-bullseye

# Set working directory
WORKDIR /workspace

# Install system dependencies needed for scientific packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libhdf5-dev \
    libnetcdf-dev \
    libgeos-dev \
    libproj-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install Python packages in the order specified in the instructions
RUN pip install --no-cache-dir \
    numpy \
    matplotlib \
    pandas \
    netCDF4 \
    scipy \
    jupyter \
    jupyterlab \
    cartopy \
    cmocean \
    gsw \
    seabird \
    GFPy

# Create data directory
RUN mkdir -p /workspace/data

# Expose Jupyter port
EXPOSE 8888

# Set default command to start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]