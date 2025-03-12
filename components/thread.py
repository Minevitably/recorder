import wave
import pyaudio
from PySide6.QtCore import QThread, Signal


class RecorderThread(QThread):
    frames_ready = Signal(list)

    def __init__(self):
        super().__init__()
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.frames = []
        self.pyaudio_instance = pyaudio.PyAudio()
        self.stream = None
        self.recording = False

    def run(self):
        self.frames = []
        self.stream = self.pyaudio_instance.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        print("录音开始...")
        while self.recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
        self.stream.stop_stream()
        self.stream.close()
        print("录音停止...")
        self.frames_ready.emit(self.frames)

    def start_recording(self):
        self.recording = True
        self.start()

    def stop_recording(self):
        self.recording = False
        self.wait()  # 等待线程结束

    def save_recording(self, filename, frames):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.pyaudio_instance.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))
        print(f"录音已保存为 {filename}")
