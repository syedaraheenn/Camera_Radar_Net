import mmcv
val_infos = mmcv.load('data/nuScenes/nuscenes_infos_val.pkl')
print(len(val_infos))  # Should print the number of scenes
