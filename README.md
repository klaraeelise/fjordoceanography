# GEOF232 Docker Environment Setup

## Prerequisites
- Docker Desktop for Mac (with Apple Silicon support)
- VS Code with Docker extension

## Setup Instructions

1. **Place these files in your project directory:**
   ```
   /Users/klaraeelise/Projects/uni/fjordoceanography/
   ├── Dockerfile
   ├── docker-compose.yml
   └── README.md
   ```

2. **Build the Docker image:**
   Open Terminal and navigate to your project directory:
   ```bash
   cd /Users/klaraeelise/Projects/uni/fjordoceanography
   docker-compose build
   ```

3. **Start the container:**
   ```bash
   docker-compose up
   ```

4. **Access Jupyter Lab:**
   Open your browser and go to: `http://localhost:8888`

5. **Using with VS Code:**
   - Install the "Dev Containers" extension in VS Code
   - Open your project folder in VS Code
   - Click the blue icon in the bottom-left corner
   - Select "Reopen in Container"
   - VS Code will connect to your running container

## Useful Docker Commands

- **Start container:** `docker-compose up -d` (detached mode)
- **Stop container:** `docker-compose down`
- **View logs:** `docker-compose logs -f`
- **Execute commands in container:** `docker-compose exec geof232 bash`
- **Rebuild after changes:** `docker-compose build --no-cache`

## Package List (Pre-installed)
All packages from the course requirements:
- numpy
- matplotlib
- pandas
- netCDF4
- scipy
- jupyter/jupyterlab
- cartopy
- cmocean
- gsw (Gibbs SeaWater)
- seabird
- GFPy

## Directory Structure
Your local folder is mounted to `/workspace` in the container:
- Code: `/workspace/code` (create if needed)
- Data: `/workspace/data` (automatically created)

## Notes
- The container is configured for Apple Silicon (ARM64)
- Jupyter runs without token/password (for local development only)
- All files saved in the container are automatically synced to your Mac