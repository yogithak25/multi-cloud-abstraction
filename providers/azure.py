from core.base import CloudProvider

class AzureProvider(CloudProvider):

    def create_resource(self, resource_type: str, **kwargs):
        if resource_type == "vm":
            return self._create_vm(**kwargs)
        elif resource_type == "blob":
            return self._create_blob(**kwargs)
        else:
            raise ValueError(f"Azure resource not supported: {resource_type}")

    def _create_vm(self, **params):
        return {
            "cloud": "Azure",
            "resource": "VM",
            "params": params
        }

    def _create_blob(self, **params):
        return {
            "cloud": "Azure",
            "resource": "Blob Storage",
            "params": params
        }
