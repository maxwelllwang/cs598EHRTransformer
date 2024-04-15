from transformers import DataCollatorForLanguageModeling
from torch.utils.data.dataloader import default_collate


class DataCollatorForICDBERT(DataCollatorForLanguageModeling):
    def __init__(self, tokenizer, mlm=True, mlm_probability=0.15):
        super().__init__(tokenizer=tokenizer, mlm=mlm, mlm_probability=mlm_probability)

    def collate_batch(self, examples):
        # If your model needs a special way to handle labels or inputs, modify here
        # This is a simple extension of the MLM collator that uses the parent class's functionality
        batch = super().collate_batch(examples)

        # Example extension: Add custom processing
        # For instance, if you need to add a domain-specific adaptation

        return batch
    
class DataCollatorForICDBERTFINALPRED(DataCollatorForLanguageModeling):
    def __init__(self, tokenizer, mlm_probability=0.15, pad_to_multiple_of=None):
        # Assuming the final prediction stage does not use masking
        super().__init__(tokenizer=tokenizer, mlm=False, mlm_probability=mlm_probability, pad_to_multiple_of=pad_to_multiple_of)

    def __call__(self, examples):
        # As no masking is needed for prediction, handle padding and attention mask creation
        batch = super().__call__(examples)
        return batch
    
from transformers import DataCollatorForSeq2Seq

class DataCollatorForICDBART(DataCollatorForSeq2Seq):
    def __init__(self, tokenizer, mlm_probability=0.15, pad_to_multiple_of=None):
        super().__init__(tokenizer=tokenizer, model=None, label_pad_token_id=-100, pad_to_multiple_of=pad_to_multiple_of)

    def __call__(self, examples):
        # Here, prepare masked inputs for encoder and plain inputs for decoder
        batch = super().__call__(examples)
        return batch
    

def prepare_dataset(model_args, data_args, training_args, tokenizer):
    # Example: Load your data here
    # train_data = load_data(data_args.train_data_file)
    # eval_data = load_data(data_args.eval_data_file)
    # test_data = load_data(data_args.test_data_file)

    train_dataset = None
    eval_dataset = None
    test_datasets = None

    # Assume `load_data` is a function that reads a text file and processes it into the required format
    # train_dataset = [tokenizer(text) for text in train_data]
    # eval_dataset = [tokenizer(text) for text in eval_data]
    # test_datasets = [tokenizer(text) for text in test_data]

    return train_dataset, eval_dataset, test_datasets

# def load_data(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = file.readlines()
#     return data