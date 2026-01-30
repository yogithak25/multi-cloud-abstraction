from core.base import CloudProvider

class GCPProvider(CloudProvider):

    def create_resource(self, resource_type: str, **kwargs):
        if resource_type == "compute":
            return self._create_compute(**kwargs)
        elif resource_type == "storage":
            return self._create_storage(**kwargs)
        else:
            raise ValueError(f"GCP resource not supported: {resource_type}")

    def _create_compute(self, **params):
        return {
            "cloud": "GCP",
            "resource": "Compute Engine",
            "params": params
        }

    def _create_storage(self, **params):
        return {
            "cloud": "GCP",
            "resource": "Cloud Storage",
            "params": params
        }
