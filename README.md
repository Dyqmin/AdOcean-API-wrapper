## What is it?
This is a Python API wrapper to help you manage and automate work with AdOcean.



## Local installation
#### From Source
- Clone the repository
- Use `pip install -r requirements.txt` to install the required packages
## Quick start
Pull the module into your namespace and create a class instance.
```python
from adocean_api import AdOcean


api = AdOcean("login", "password")
api.open_session()

placements_list = api.get('GetPlacementsList')  
print(placement_list.json())

api.close_session()                             
```
# Docs
You can check official docs here https://support.adocean-global.com/docapi