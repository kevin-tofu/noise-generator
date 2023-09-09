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
    white_noise = np.abs(
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
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='export generated white noise as mp3.'
    )
    parser.add_argument(
        '--sampling_rate', '-P1', type=int, default=44100, help=''
    )
    parser.add_argument(
        '--duration_sec', '-P2', type=int, default=600, help=''
    )
    parser.add_argument(
        '--export_path', '-EP', type=str, default='./whitenoise.mp3', help='path for image2'
    )
    args = parser.parse_args()

    main(args)
