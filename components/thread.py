import wave
import pyaudio
from PySide6.QtCore import QThread, Signal


class RecorderThread(QThread):
    frames_ready = Signal(list)

    def __init__(self):
        """
        初始化 RecorderThread 对象。

        设置音频录制的参数，如块大小、格式、通道数、采样率等。
        初始化 PyAudio 实例和帧列表。
        """
        super().__init__()
        self.chunk = 1024  # 每次读取的音频数据块大小
        self.format = pyaudio.paInt16  # 音频格式，16位整数
        self.channels = 1  # 音频通道数，单声道
        self.rate = 44100  # 音频采样率，44100Hz
        self.frames = []  # 存储录制的音频帧的列表
        self.pyaudio_instance = pyaudio.PyAudio()  # PyAudio 实例，用于音频输入
        self.stream = None  # 音频流
        self.recording = False  # 录音状态，True 表示正在录音

    def run(self):
        """
        线程的主运行方法，执行音频录制。

        打开音频流，读取音频数据，并将其存储在帧列表中。
        录音停止后，关闭音频流，并发出 frames_ready 信号。
        """
        self.frames = []  # 清空帧列表，开始新的录音
        self.stream = self.pyaudio_instance.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,  # 设置为输入流
            frames_per_buffer=self.chunk
        )
        print("录音开始...")
        while self.recording:
            data = self.stream.read(self.chunk)  # 读取音频数据
            self.frames.append(data)  # 将数据添加到帧列表
        self.stream.stop_stream()  # 停止音频流
        self.stream.close()  # 关闭音频流
        print("录音停止...")
        self.frames_ready.emit(self.frames)  # 发出信号，传递帧列表

    def start_recording(self):
        """
        开始录音。

        设置录音状态为 True，并启动线程。
        """
        self.recording = True
        self.start()  # 启动线程

    def stop_recording(self):
        """
        停止录音。

        设置录音状态为 False，并等待线程结束。
        """
        self.recording = False
        self.wait()  # 等待线程结束

    def save_recording(self, filename, frames):
        """
        保存录音到 WAV 文件。

        将帧列表中的音频数据写入指定的文件。
        """
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)  # 设置通道数
            wf.setsampwidth(self.pyaudio_instance.get_sample_size(self.format))  # 设置采样宽度
            wf.setframerate(self.rate)  # 设置采样率
            wf.writeframes(b''.join(frames))  # 写入音频数据
        print(f"录音已保存为 {filename}")
