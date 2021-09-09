import argparse
import os
import requests
import re


"""
How to use:
download all the models:
    python main_download_pretrained_models.py --models "all"  --model_dir "model_zoo"

download DnCNN models:
    python main_download_pretrained_models.py --models "DnCNN" --model_dir "model_zoo"

download SRMD models:
    python main_download_pretrained_models.py --models "SRMD" --model_dir "model_zoo"

download BSRGAN models:
    python main_download_pretrained_models.py --models "BSRGAN" --model_dir "model_zoo"

download FFDNet models:
    python main_download_pretrained_models.py --models "FFDNet" --model_dir "model_zoo"

download DPSR models:
    python main_download_pretrained_models.py --models "DPSR" --model_dir "model_zoo"

download other models:
    python main_download_pretrained_models.py --models "others" --model_dir "model_zoo"

------------------------------------------------------------------

download 'dncnn_15.pth' and 'dncnn_50.pth'
    python main_download_pretrained_models.py --models "dncnn_15.pth dncnn_50.pth" --model_dir "model_zoo"

------------------------------------------------------------------

download DnCNN models and 'BSRGAN.pth'
    python main_download_pretrained_models.py --models "DnCNN BSRGAN.pth" --model_dir "model_zoo"

"""


def download_pretrained_model(model_dir='model_zoo', model_name='dncnn3.pth'):
    if os.path.exists(os.path.join(model_dir, model_name)):
        print(f'already exists, skip downloading [{model_name}]')
    else:
        os.makedirs(model_dir, exist_ok=True)
        if 'SwinIR' in model_name:
            url = 'https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/{}'.format(model_name)
        else:
            url = 'https://github.com/cszn/KAIR/releases/download/v1.0/{}'.format(model_name)
        r = requests.get(url, allow_redirects=True)
        print(f'downloading [{model_dir}/{model_name}] ...')
        open(os.path.join(model_dir, model_name), 'wb').write(r.content)
        print('done!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--models',
                        type=lambda s: re.split(' |, ', s),
                        default = "dncnn3.pth",
                        help='comma or space delimited list of characters, e.g., "DnCNN", "DnCNN BSRGAN.pth", "dncnn_15.pth dncnn_50.pth"')
    parser.add_argument('--model_dir', type=str, default='model_zoo', help='path of model_zoo')
    args = parser.parse_args()

    print(f'trying to download {args.models}')

    method_model_zoo = {'DnCNN': ['dncnn_15.pth', 'dncnn_25.pth', 'dncnn_50.pth', 'dncnn3.pth', 'dncnn_color_blind.pth', 'dncnn_gray_blind.pth'],
                        'SRMD': ['srmdnf_x2.pth', 'srmdnf_x3.pth', 'srmdnf_x4.pth', 'srmd_x2.pth', 'srmd_x3.pth', 'srmd_x4.pth'],
                        'DPSR': ['dpsr_x2.pth', 'dpsr_x3.pth', 'dpsr_x4.pth', 'dpsr_x4_gan.pth'],
                        'FFDNet': ['ffdnet_color.pth', 'ffdnet_gray.pth', 'ffdnet_color_clip.pth', 'ffdnet_gray_clip.pth'],
                        'USRNet': ['usrgan.pth', 'usrgan_tiny.pth', 'usrnet.pth', 'usrnet_tiny.pth'],
                        'DPIR': ['drunet_gray.pth', 'drunet_color.pth', 'drunet_deblocking_color.pth', 'drunet_deblocking_grayscale.pth'],
                        'BSRGAN': ['BSRGAN.pth', 'BSRNet.pth', 'BSRGANx2.pth'],
                        'others': ['RRDB.pth', 'ESRGAN.pth', 'FSSR_DPED.pth', 'FSSR_JPEG.pth', 'RealSR_DPED.pth', 'RealSR_JPEG.pth']
                        }

    method_zoo = list(method_model_zoo.keys())
    model_zoo = []
    for b in list(method_model_zoo.values()):
        model_zoo += b

    if 'all' in args.models:
        for method in method_zoo:
            for model_name in method_model_zoo[method]:
                download_pretrained_model(args.model_dir, model_name)
    else:
        for method_model in args.models:
            if method_model in method_zoo:
                for model_name in method_model_zoo[method_model]:
                    download_pretrained_model(args.model_dir, model_name)
            elif method_model in model_zoo:
                download_pretrained_model(args.model_dir, method_model)
            else:
                print(f'Do not find {method_model} from the pre-trained model zoo!')








       