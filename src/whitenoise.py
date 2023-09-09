import argparse
import numpy as np
import scipy.fftpack as fft


def get_whitenoise(
    sampling_rate: int = 44100,
    duration_sec: int = 600
):

    num_samples = int(sampling_rate*duration_sec)
    random_phase = np.exp(
        1j* np.random.uniform(0, 2*np.pi, num_samples)
    )
    # white_noise = fft.ifft(spectrum)
    white_noise = np.real(
        fft.ifft(random_phase)
    )

    
    return white_noise

# def get_time(
#     sampling_rate: int = 44100,
#     duration_sec: int = 6010
# ):
    
#     return np.linspace(
#         0,
#         duration_sec,
#         int(sampling_rate * duration_sec),
#         endpoint=False
#     )


def visualize_noise(
    data: np.ndarray,
    export_path: str
):
    import matplotlib
    from matplotlib import pyplot as plt
    plt.figure(1, figsize=(6.4, 3))
    plt.subplot(1, 1, 1)
    # plt.imshow(I1)
    plt.plot(data)
    # plt.axis('off')
    # plt.title('Image 1')
    plt.savefig(export_path)

def main(
    args: argparse.Namespace
):
    import export_mp3

    whitenoise = get_whitenoise(
        args.sampling_rate,
        args.duration_sec
    )

    export_mp3.use_pydub(
        args.sampling_rate,
        whitenoise,
        args.export_path
    )

    visualize_noise(
        whitenoise,
        'noise.png'
    )
    


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='export generated white noise as mp3.'
    )
    parser.add_argument(
        '--sampling_rate', '-P1', type=int, default=44100, help=''
    )
    parser.add_argument(
        '--duration_sec', '-P2', type=int, default=10, help=''
    )
    parser.add_argument(
        '--export_path', '-EP', type=str, default='./whitenoise.mp3', help='path for image2'
    )
    args = parser.parse_args()

    main(args)
