import basic_operator as bo
import wave
import scipy.io.wavfile

# f = wave.open('./wav/我爱南开.wav', 'rb')
# print(type(f))
sample_rate,signal = scipy.io.wavfile.read('./wav/我爱南开.wav')
# print(type(signal))
# bo.plot_freq(signal,sample_rate,'频域图')
# bo.plot_time(signal,sample_rate,'时域图')
signal = bo.pre_emphasis(signal) # 预加重
signal = bo.framing(signal,sample_rate) # 分帧
signal = bo.add_window(signal, sample_rate) # 加窗
# signal = bo.my_fft(signal) # FFT
signal = bo.stft(signal) # FFT+幅值平方
# signal = bo.mel_filter(signal,sample_rate) # Mel滤波器
signal = bo.log_pow(signal) # 对数功率
bo.plot_spectrogram(signal,"spec","spec")
# bo.plot_spectrogram(signal,"fbank","fbank")
signal=bo.discrete_cosine_transform(signal)
# bo.plot_spectrogram(signal,"mfcc","mfcc")

