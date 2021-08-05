# Deploy ACI and Kubernetes Integration

## Requirements
- Python 

- Ansible

- PyVmomi 

## How to use

#### Step 1. Create a VM template and name the template as aci-k8s-template

- Install Ubuntu 18.04+
- Install python3-pip
- Genenerate and copy public key from management station to VM
  - ssh-keygen -t rsa
  - ssh-copy-id  <VM>

- configure sudo without password prompt
- Setup proxy for the following (skip this step if you don’t need internect connection via proxy)
  - Enviroment
  - Docker
  - APT
#### Step 2. Clone repo to the home directory of the managment station
#### Step 3. Prepare the acc-provision template file and name the file name as aci-fabric.yaml
  - ACI Configuration Guide for reference: 
    https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/kb/b_Kubernetes_Integration_with_ACI.html
#### Step 4. Edit params in hosts and gvar.yml files to match up acc-provision template and IP scheme planned
  
#### Step 5. Exceution
      ansible-playbook -i hosts --become --become-user=root k8-cluster.yml
  




