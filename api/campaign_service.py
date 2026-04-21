import json
import os
from typing import List, Dict, Any, Optional

CATALOGS_FILE = "catalogs.json"
CAMPAIGNS_FILE = "campaigns.json"

class CampaignService:
    def __init__(self):
        self.catalogs_file = CATALOGS_FILE
        self.campaigns_file = CAMPAIGNS_FILE

    def _load_data(self, file_path: str) -> List[Dict[str, Any]]:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return json.load(f)
        return []

    def _save_data(self, file_path: str, data: List[Dict[str, Any]]):
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_all_catalogs(self) -> List[Dict[str, Any]]:
        return self._load_data(self.catalogs_file)

    def create_catalog(self, catalog_data: Dict[str, Any]) -> Dict[str, Any]:
        catalogs = self.get_all_catalogs()
        catalog_data["id"] = len(catalogs) + 1
        catalogs.append(catalog_data)
        self._save_data(self.catalogs_file, catalogs)
        return catalog_data

    def get_all_campaigns(self) -> List[Dict[str, Any]]:
        return self._load_data(self.campaigns_file)

    def create_campaign(self, campaign_data: Dict[str, Any]) -> Dict[str, Any]:
        campaigns = self.get_all_campaigns()
        campaign_data["id"] = len(campaigns) + 1
        campaigns.append(campaign_data)
        self._save_data(self.campaigns_file, campaigns)
        return campaign_data
