# private-pypi-hub

Set up your own private PyPI server using pypiserver, a PyPI-compatible server, and Docker. We'll host the server on an AWS EC2 instance.

---

## Overview
- **EC2 Deployment**: Host your private PyPI server on Amazon EC2 instances
- **Docker Containerized**: Deploy pypiserver using Docker containers
- **Private Distribution**: Secure internal package management with pypiserver

---

## Architecture
- **EC2 Instance**: Runs the Docker container hosting pypiserver
- **Docker Container**: pypiserver application serving packages
- **Local Storage**: Package files stored on EC2 instance storage

---

## Features
- **PyPI-Compatible**: Full compatibility with pip and other Python package managers
- **Private & Secure**: Internal server accessible only to authorized users
- **Docker Deployment**: Easy containerized deployment of pypiserver
- **Version Management**: Support for stable and development package versions

---

## Resources
- [pypiserver Documentation](https://github.com/pypiserver/pypiserver)
- [Python Packaging User Guide](https://packaging.python.org/)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [Docker Documentation](https://docs.docker.com/)

---

# Setup Instructions

## Step 1: Provision the EC2 Instances
Use Terraform to provision the EC2 instances for the private PyPI servers.

```bash
cd infra
terraform init
terraform apply
```

## Step 2: Configure the EC2 Instances
SSH into the provisioned EC2 instances and install the required dependencies:

```bash
ssh -i <your-key.pem> ec2-user@<EC2_IP>
scp -i <your-key.pem> -r server ec2-user@<EC2_IP>:/home/ec2-user/pypi
bash /home/ec2-user/pypi/server/setup.sh
```

## Step 3: Set Up Authentication
Create the `.htpasswd` file for authentication:

```bash
bash /home/ec2-user/pypi/server/auth.sh
```

## Step 4: Start the PyPI Server
Run the PyPI server on the EC2 instance:

```bash
bash /home/ec2-user/pypi/server/start.sh
```

## Step 5: Build and Upload the Package
Build the Python package and upload it to the private PyPI server:

```bash
python3 -m build testpackage
python3 -m twine upload --repository-url http://<EC2_IP>:8080/ /testpackage/dist/*
```

## Step 6: Verify the Package
Install the uploaded package from the private PyPI server:

```bash
pip install --index-url http://<EC2_IP>:8080/simple/ <package-name>
```