# Voice2Text

Voice2Text is transcript media file to txt file to use Google Speach API & 

## Installation

Voice2Text need GOOGLE_APPLICATION_CREDENTIALS files.
if you don't have this, please build google cloud projects and get from it.

#### Gcloud Project build

1. Google Cloud SDK Install

```
brew cask install google-cloud-sdk
```

2. Setting Gcloud Projects

```
gcloud auth login
gcloud alpha projects create voicetotext-123456 --name voice2text
```

3. Go to Projects URL and enable Google Speech API.
4. Please Enable (Billing)[https://support.google.com/cloud/answer/6293499?hl=en].
5. Create Service Key and Downlaod (Ref:[Service Acount](https://cloud.google.com/storage/docs/authentication#generating-a-private-key).)
5. set GOOGLE_APPLICATION_CREDENTIALS

```
export GOOGLE_APPLICATION_CREDENTIALS='/your/service/acount/key/xxx.json'
```

#### Install

```
pip install voicetotext
```

## Usage

This application has two commands.
splitvoice is convert the voice diving. 
voicetotext is voice existing in the folder into a text through google api.
(See help command)

```
splitvoice --help
voicetotext --help
```

## Sample

![sample_gif](https://github.com/kztka/voicetotext/raw/master/gif/split_audio_file.gif "Sample Gif")

#### Split Audio Files

Sample Japanese voices from [here](http://nergui.sakura.ne.jp/library.html)

```
$ splitvoice voices/hana_1.mp3 --relative
spliting /57
spliting Done!
File was separete 57 filesOutput Separeted files? [Y/n]:y
separeted done! Have a nice Day!⏎
```

#### Transript Japanese audio files

```
$ voicetotext results/ -s 22050 -l "ja_JP"
芥川龍之介
花
line
朗読池田秀雄
禅智内供の鼻といえば池で知らないものはない
長澤語録すがって上唇の上から顎の下まで下がっている
```

## Error Handling

#### "Sample rate in request does not match FLAC header."

You need to examine the sample rate.
I recommend ffprove to examine.

```
$ ffmprove results/000.flac
Input #0, flac, from 'results/000.flac':
  Metadata:
    ENCODER         : Lavf57.56.101
  Duration: 00:00:01.87, start: 0.000000, bitrate: 184 kb/s
    Stream #0:0: Audio: flac, 22050 Hz, mono, s16
```

You can get framerate. In this case, frame rate is 22050.
So, your commands is this.

```
$ voicetotext results -s 22050
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Debugging
```
# virtualenv
python3 -m venv env
source ./env/bin/activate

# python packages install
pip install -r requirements.txt
```

## History

# License

This software is released under the MIT License, see LICENSE.txt.

