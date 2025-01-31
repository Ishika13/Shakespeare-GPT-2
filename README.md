This repository contains the implementation of GPT-2 model from scratch on the Shakespeare dataset and then finetuning it on the same.

- prepare.py: Downloads the dataset, tokenises it using tiktoken and BPE like the GPT paper implements it and exports the train, test and validation bins.
- train_shakespeare_char.py: Trains the GPT model and tunes the parameters as required.
- finetune_shakespeare.py: Finetunes the model on top of train_shakespeare_char.py.
