# CollabRepo

---

### A repo for us to practice making a webapp and api

## Project goal: Create an open-source learning platform with functions similar to existing closed-source options

## Installation
1. Clone the repository with `git clone https://github.com/Devoodie/CollabRepo.git`
2. Move into the cloned directory `cd CollabRepo`
3. Run `pip install -r requirements.txt`
4. Run `main.py`

## Installation (Podman/Docker)
1. Clone the repository with `git clone https://github.com/Devoodie/CollabRepo.git`
2. Move into the cloned directory `cd CollabRepo`
3. Build the container image `podman build -t collabrepo .` or ` docker build -t collabrepo -f Containerfile .`
4. Expose ports for, name, and run the container `docker run -d -p 8000:8000 --name=collab collabrepo`