import numpy as np


def use_pydub(
    sampling_rate: int,
    audio_data: np.ndarray,
    export_path: str
):
    import pydub

    
    max_audio_data = np.max(np.abs(audio_data))
    audio_data = (audio_data / max_audio_data * 32767.0).astype(np.int16)
    # audio_data = (audio_data * 32767.0).astype(np.int16)

    audio_segment = pydub.AudioSegment(
        audio_data.tobytes(),
        frame_rate=sampling_rate,
        sample_width=audio_data.dtype.itemsize,
        channels=1
    )
    audio_segment.export(
        export_path, format='mp3'
    )

