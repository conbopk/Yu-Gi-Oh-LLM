from torch import accelerator


def fetch_device():
    current_accelerator = accelerator.current_accelerator()
    if current_accelerator and accelerator.is_available():
        return current_accelerator.type
    return "cpu"


if __name__=="__main__":
    import torch

    print("PyTorch:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA version:", torch.version.cuda)
    print("Device count:", torch.cuda.device_count())

    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))

    device = fetch_device()
    print(device)