# This is a config file for training a character-level GPT model on the shakespeare dataset

out_dir = 'out-shakespeare-char'
eval_interval = 250 
eval_iters = 200
log_interval = 10 

always_save_checkpoint = False

wandb_log = False 
wandb_project = 'shakespeare-char'
wandb_run_name = 'shakespeare-char_hp'

dataset = 'shakespeare_char'
gradient_accumulation_steps = 1
batch_size = 16 #64
block_size = 512 #256

n_layer = 12 #6
n_head = 12 #6
n_embd = 384
dropout = 0.2

learning_rate = 1e-2 #1e-3
max_iters = 8000 #5000
lr_decay_iters = 8000 #5000 # make equal to max_iters usually
min_lr = 1e-3 #1e-4 # learning_rate / 10 usually
beta2 = 0.99 

warmup_iters = 200 #100