
from parameter import *
from trainer import Trainer
# from tester import Tester
from data_loader import Data_Loader
from torch.backends import cudnn
from utils import make_folder
from sagan_models import Self_Attn

def main(config):
    # For fast training
    cudnn.benchmark = True


    # Data loader
    data_loader = Data_Loader(config.train, config.dataset, config.image_path, config.imsize,
                             config.batch_size, shuf=config.train)

    # Create directories if not exist
    make_folder(config.model_save_path, config.version)
    make_folder(config.sample_path, config.version)
    make_folder(config.log_path, config.version)
    make_folder(config.attn_path, config.version)


    if config.train:
        trainer = Trainer(data_loader.loader(), config)
        trainer.train()



#attn = Self_Attn(128, 'relu')
