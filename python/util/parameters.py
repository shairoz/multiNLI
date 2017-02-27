import argparse

parser = argparse.ArgumentParser()
parser.add_argument("model_name", type=str, help="Give model name. For example cbow, cbow-2, spinn etc.")
parser.add_argument("--data_type", type=str, default="snli", help="Give dataset name, example snli, multiNLI etc.")
parser.add_argument("--datapath", type=str, default="../data")
parser.add_argument("--logpath", type=str, default="../logs")
parser.add_argument("--emb_to_load", type=int, default=None, help="Number of embeddings to load")
parser.add_argument("--test", action='store_true', help="Call if you want to only test on the best checkpoint.")

args = parser.parse_args()

def load_parameters():
    FIXED_PARAMETERS = {
        "data_type": "{}".format(args.data_type),
        "model_name": args.model_name,
        "training_data_path": "{}/snli_1.0/snli_1.0_train.jsonl".format(args.datapath),
        "dev_data_path": "{}/snli_1.0/snli_1.0_dev.jsonl".format(args.datapath),
        "test_data_path": "{}/snli_1.0/snli_1.0_test.jsonl".format(args.datapath),
        "embedding_data_path": "{}/glove.840B.300d.txt".format(args.datapath),
        "log_path": "{}".format(args.logpath),
        "ckpt_path":  "{}".format(args.logpath),
        "embeddings_to_load": args.emb_to_load,
        "word_embedding_dim": 300, #50
        "hidden_embedding_dim": 300, #50
        "seq_length": 25,
        "keep_rate": 0.5, 
        "batch_size": 32,
        "learning_rate": 0.0004,
    }

    return FIXED_PARAMETERS

def train_or_test():
    return args.test