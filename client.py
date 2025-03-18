from twisted.internet import reactor, ssl

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS

import websocket
import json
import pyaudio
import wave
import threading

W3W_API_KEY ='058F5QVF'
VOICE_LANGUAGE = 'en'

class VoiceApiProtocol(WebSocketClientProtocol):
    def __init__(self):
        super().__init__()
        self.audio = pyaudio.PyAudio()
        self.sample_rate = 16000
        self.pyaudio_format = pyaudio.paInt16
        self.raw_encoding = "pcm_s16le"
        self.frames_per_buffer = 4096

    def onOpen(self):
        # Initiate the recognition
        start_recognition = {
            "message": "StartRecognition",
            "audio_format": {
                "type": "raw",
                "encoding": self.raw_encoding,
                "sample_rate": self.sample_rate
            }
        }
        self.sendMessage(json.dumps(start_recognition).encode('utf8'))

    def onMessage(self, payload, isBinary): # Message recieved from the Server
        message = json.loads(payload.decode('utf8'))

        message_type = message["message"]
        if message_type == "RecognitionStarted": # Begin speech recognition
            print("Say any 3 word address...")

            # Run the audio stream asynchronously
            self.audio_stream = self.audio.open(
            format=self.pyaudio_format,
            channels=1,
            rate=self.sample_rate,
            input=True,
            input_device_index=0,  # Explicitly select the first input device
            frames_per_buffer=self.frames_per_buffer,
            stream_callback=self.send_audio)

        elif message_type == "Suggestions": # Suggestions have been returned
            # Close the audio stream
            self.audio_stream.stop_stream()
            self.audio_stream.close()

            # Print the results
            print("\nSuggestions:")
            print("============\n")
            print(json.dumps(message, indent=4))

    def onClose(self, wasClean, code, reason): # Connection with the server closed
        if code != 1000:
            print("Connection closed with Error")
            print("Code: {}".format(code))
            print("Reason: {}".format(reason))

        reactor.stop()

    def send_audio(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the WebSocket."""
        reactor.callFromThread(
                self.sendMessage,
                in_data,
                isBinary=True
            )
        return None, pyaudio.paContinue


if __name__ == '__main__':
    # create a WS client factory with our protocol
    factory = WebSocketClientFactory(
       "wss://voiceapi.what3words.com/v1/autosuggest?key={}&voice-language={}".format(W3W_API_KEY, VOICE_LANGUAGE))
    factory.protocol = VoiceApiProtocol
    from twisted.internet.ssl import CertificateOptions
    from OpenSSL import SSL
    # from twisted.internet.ssl import optionsForClientTLS
    ssl_context = CertificateOptions(method=SSL.TLS_METHOD)
    # connectWS(factory, optionsForClientTLS("voiceapi.what3words.com"))
    connectWS(factory, ssl_context)


    reactor.run()