from essentia.standard import MonoLoader, TensorflowPredictFSDSINet

audio = MonoLoader(filename="audio.wav", sampleRate=22050)()
model = TensorflowPredictFSDSINet(graphFilename="fsd-sinet-vgg42-tlpf_aps-1.pb")
predictions = model(audio)
