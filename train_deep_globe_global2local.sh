export CUDA_VISIBLE_DEVICES=0
python train_deep_globe.py \
--n_class 5 \
--data_path "/home1/xilu/projects/data_1_4/" \
--model_path "/home1/xilu/projects/savedmodels/" \
--log_path "/home1/xilu/projects/logs/" \
--task_name "fpn_deepglobe_global2local" \
--mode 2 \
--batch_size 6 \
--sub_batch_size 6 \
--size_g 508 \
--size_p 508 \
--path_g "fpn_deepglobe_global.pth" \