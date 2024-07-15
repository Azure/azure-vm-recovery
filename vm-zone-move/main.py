import argparse

from cloud.cloud_factory import CloudFactory
from service.failover_service import FailoverService
from utils import get_confirmation


def main():
    parser = argparse.ArgumentParser(description="Example program to handle VM information.")
    parser.add_argument("-oldvm", "--old_vm_name", help="Name of the old virtual machine", type=str, required=True)
    parser.add_argument("-newvm", "--new_vm_name", help="Name of the new virtual machine", type=str, required=True)
    parser.add_argument("-subid", "--subscription_id", help="azure subscription ID", type=str, required=True)
    parser.add_argument("-rg", "--resource_group_name", help="Name of the resource group", type=str, required=True)
    parser.add_argument("-nz", "--new_zone", help="New availability zone", type=int, required=False)
    parser.add_argument("-pswd", "--admin_password", help="New VM admin password", type=str, required=True)

    args = parser.parse_args()
    old_vm_name = args.old_vm_name
    new_vm_name = args.new_vm_name
    subscription_id = args.subscription_id
    resource_group_name = args.resource_group_name
    new_zone = args.new_zone
    admin_password = args.admin_password

    print(f"Old VM Name: {old_vm_name}")
    print(f"New VM Name: {new_vm_name}")
    print(f"Subscription ID: {subscription_id}")
    print(f"Resource Group Name: {resource_group_name}")
    print(f"New Zone: {new_zone}")

    if not get_confirmation():
        print("Exiting")
        return

    cloud_factory: CloudFactory = CloudFactory(subscription_id)
    failover_service: FailoverService = FailoverService(
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
        old_vm_name=old_vm_name,
        new_vm_name=new_vm_name,
        new_zone=new_zone,
        admin_password=admin_password,
        cloud_factory=cloud_factory
    )

    failover_service.execute_failover()


main()
