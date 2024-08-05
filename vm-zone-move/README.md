# Failover scripts

During zone down scenario, customers will not be able to access impacted VMs and consequently the data persisted in their data disks. These scripts will bring back the vm in a different zone or region depending upon the type of disks (ZRS/LRS) attached to the vm. Effectively moving the VM. Once the VM is moved, the ARM ID and UniqueVMId for the VM will be changed.

## How to Use? 

* Ensure that python is installed on the machine where these scripts are going to be run. 
* Install the required python packages as mentioned in requirements.txt
  * pip install -r requirements.txt
* Run main.py with the arguments as the details of the affected VM in the zonal outage. In case all the requirements are met, the VM will be brought back up in a different zone or region with the disks attached.

### Example: 
python "path to main.py" --subscription_id "subscription id" --old_vm_name "old vm name" --new_vm_name "recovered vm name" --resource_group_name "resource group name" --new_zone "zone number" --admin_password "password"

## Parameters


1. **old_vm_name**
   - **Option:** `-oldvm`, `--old_vm_name`
   - **Description:** Old VM name
   - **Type:** String
   - **Required:** Yes

2. **new_vm_name**
   - **Option:** `-newvm`, `--new_vm_name`
   - **Description:** New VM name
   - **Type:** String
   - **Required:** Yes

3. **subscription_id**
   - **Option:** `-subid`, `--subscription_id`
   - **Description:** Azure subscription ID
   - **Type:** String
   - **Required:** Yes

4. **resource_group_name**
   - **Option:** `-rg`, `--resource_group_name`
   - **Description:** Resource group name
   - **Type:** String
   - **Required:** Yes

5. **new_zone**
   - **Option:** `-nz`, `--new_zone`
   - **Description:** Availability zone for the new VM 
   - **Type:** Integer
   - **Required:** No

6. **admin_password**
   - **Option:** `-pswd`, `--admin_password`
   - **Description:** New VM admin password
   - **Type:** String
   - **Required:** Yes