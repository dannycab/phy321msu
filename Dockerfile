FROM ubuntu:24.04

# Install required system packages
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    make \
    python3 \
    python3-venv \
    python3-pip \
    git \
    nano \
    libgobject-2.0-0 \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libcairo2 \
    libjpeg-dev \
    libxml2 \
    libxslt1-dev \
    libssl-dev \
    libpq-dev \
    --no-install-recommends

# Set up environment variables
ENV USER_HOME=/home \
    VIRTUAL_ENVIRONMENT=/home/venv

# Create and activate a Python virtual environment
RUN python3 -m venv $VIRTUAL_ENVIRONMENT
ENV PATH="$VIRTUAL_ENVIRONMENT/bin:$PATH"

# Upgrade pip and install required Python packages
RUN pip install --upgrade pip && \
    pip install \
    jupyter-book \
    matplotlib \
    numpy \
    ipykernel \
    pandas \
    sphinxcontrib-bibtex \
    nbconvert \
    weasyprint \
    scipy \
    seaborn \
    scikit-learn

# Create and install the 'teaching' Jupyter kernel
RUN python3 -m ipykernel install --user --name=jbook --display-name "Python 3"

# Set working directory
WORKDIR /mnt/jbook