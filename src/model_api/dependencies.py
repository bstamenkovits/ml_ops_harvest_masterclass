from model_api.dataloaders import DataLoader

data_loader = DataLoader()


async def get_data() -> DataLoader:
    return data_loader
