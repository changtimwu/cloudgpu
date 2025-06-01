# cloudgpu
## setup runpod
* get api key: console -> `Settings` -> `API Keys` -> `Create API key`
* do the setup
```
% runpod config
Please enter your RunPod API Key.
You can find it at https://www.runpod.io/console/user/settings
    > RunPod API Key: rpa_JCUXVFY13G8DCJ7B6OUFZBEOPQPKJV7Z950RF5XQ1axzum
Credentials set for profile: default in ~/.runpod/config.toml
```
* first time use
```
% sky status
Failed to connect to SkyPilot API server at http://127.0.0.1:46580. Starting a local server.
✓ SkyPilot API server started.
Clusters
No existing clusters.

Managed jobs
No in-progress managed jobs. (See: sky jobs -h)

Services
No live services. (See: sky serve -h)
```

* check runpod connectivity

```
% sky check
🎉 Enabled clouds 🎉
  GCP [compute, storage]
  RunPod [compute]
```

* list all GPU options
```
% sky show-gpus -a --cloud runpod 
COMMON_GPU  AVAILABLE_QUANTITIES
A100-80GB   1, 2, 4, 8
H100        1, 2, 4, 8
L4          1, 2, 4, 8

OTHER_GPU      AVAILABLE_QUANTITIES
A100-80GB-SXM  1, 2, 4, 8
A40            1, 2, 4, 8
B200           1, 2, 4, 8
H100-NVL       1, 2, 4, 8
H100-SXM       1, 2, 4, 8
H200-SXM       1, 2, 4, 8
L40            1, 2, 4, 8
MI300X         1, 2, 4, 8
RTX3090        1, 2, 4, 8
RTX4000-Ada    1, 2, 4, 8
RTX4090        1, 2, 4, 8
RTX6000-Ada    1, 2, 4, 8
RTXA4000       1, 2, 4, 8
RTXA4500       1, 2, 4, 8
RTXA5000       1, 2, 4, 8
RTXA6000       1, 2, 4, 8
```
