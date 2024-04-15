CUDA_VISIBLE_DEVICES=0 python3 main_bart.py \
                --do_pos_emb --icd_training --load_cui_leng \
                --output_dir ./output \
                --logging_dir ./logging  \
                --model_type=bart \
                --do_train --train_data_file '../train_data/dict.txt' \
                --tokenizer_name 'bert-base-uncased' \
                --per_device_train_batch_size 24 \
                --per_device_eval_batch_size 48 \
                --block_size 512 \
                --mlm --mlm_probability 0.5 \
                --logging_first_step \
                --logging_steps 470 --save_steps 100000 \
                --num_train_epochs 12 \
                --learning_rate 1e-4 \
                --warmup_steps 470 \
                --weight_decay 0.05


# CUDA_VISIBLE_DEVICES=0 python main_bart.py \
#                 --do_pos_emb --icd_training --load_cui_leng \
#                 --output_dir PATHTOOUTPUT \
#                 --logging_dir PATHTOLOG  \
#                 --model_type=bart --config_name=PATHTOLOAD \
#                 --do_train --train_data_file=PATHTOTRAIN \
#                 --per_device_train_batch_size 24 \
#                 --do_eval --eval_data_file=PATHTODEV \
#                 --per_device_eval_batch_size 48 \
#                 --test_data_file=PATHTOTEST \
#                 --block_size 512 \
#                 --mlm --mlm_probability 0.5 \
#                 --logging_first_step \
#                 --logging_steps 470 --save_steps 100000 \
#                 --num_train_epochs 12 \
#                 --learning_rate 1e-4 \
#                 --warmup_steps 470 \
#                 --weight_decay 0.05