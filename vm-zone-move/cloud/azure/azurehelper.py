import random
from azure.mgmt.compute.v2023_09_01.models import VirtualMachine


class AzureHelper:

    @classmethod
    def get_zone_for_newvm(cls, azure_old_vm: VirtualMachine, location: str) -> str:
        account_types_ZRS = ["PREMIUM_ZRS", "STANDARDSSD_ZRS"]
        #checking if the disk are zrs or not -- all disk need to be zrs for zonal vm otherwise even if one is lrs then logic according to lrs
        disks_ZRS = True
        for azure_data_disk in azure_old_vm.storage_profile.data_disks:
            if azure_data_disk.managed_disk.storage_account_type.upper() not in account_types_ZRS:
                disks_ZRS = False
        print(azure_data_disk.managed_disk.storage_account_type.upper())
        if disks_ZRS:
            # Each region that supports Availability Zones has 3+ such zones, denoted as 1, 2, 3...
            av_zones = ["1", "2", "3"]
            current_zone = azure_old_vm.zones[0]
            filtered_list = [value for value in av_zones if value != current_zone]
            new_zone = random.choice(filtered_list)
            return new_zone
        else:
            # in case of LRS disk, creating a regional vm
            return None