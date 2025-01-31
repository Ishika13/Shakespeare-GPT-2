import time

out_dir = 'out-shakespeare'
eval_interval = 5
eval_iters = 40
wandb_log = False 
wandb_project = 'shakespeare'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'shakespeare'
init_from = 'gpt2-medium' 

always_save_checkpoint = False

batch_size = 16 #1
gradient_accumulation_steps = 16
max_iters = 50 #20

learning_rate = 3e-5
decay_lr = True #False