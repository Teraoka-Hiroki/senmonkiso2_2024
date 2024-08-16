# Hiroki Teraoka 2024.08.16 Ver1

import os
import requests
import io
import streamlit as st
from PIL import Image
import urllib.request
from gtts import gTTS

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'onseigousei_secret.json'

def synthesize_speech(text, lang='日本語', gender='female'):
    gender_type = {
        'defalut': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male': texttospeech.SsmlVoiceGender.MALE,
        'female': texttospeech.SsmlVoiceGender.FEMALE,
        'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
    }
    lang_code = {
        '英語': 'en-US',
        '日本語': 'ja-JP'
    }
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender],name="ja-JP-Wavenet-D"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response


def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)


def mv_app(video_file_url, video_filename):
#    st.title('Video Player')
    if st.button('Play Video'):
#        video_file_url = 'https://drive.google.com/uc?export=download&id=YourFileID'  # Google Driveの動画ファイルのIDを指定してください
#        video_filename = 'video.mp4'
        download_file(video_file_url, video_filename)
        video_file = open(video_filename, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)


st.title('専門基礎２学期パーフェクトアプリ 2024年版')

st.write('')
st.write('')

input_data = '　　本アプリは、2学期中間考査対策用です。\
問い１から問い６までは、表計算アプリ、エクセルの問題です。\
各問い、動画を視聴してから後の問題にトライしてください。\
問い７からは、ノギスの問題です。\
ノギスの名称と測定値の求め方の問題にトライしてください。\
なお、考査では、基本統計量の計算問題もでますが、このアプリでは割愛しています。\
各自で確認しておいてください。\
ちなみに、考査で出題される基本統計量は、平均値、偏差、不偏分散、標準偏差、変動係数です。\
では、最後まで頑張って取り組んでください'
st.write('はじめに')
st.write('')
st.write(input_data)
# テキスト入力
text_input = st.text_area(input_data)

# 言語設定（デフォルトは日本語）
language = 'ja'

# ボタンをクリックしたときの処理
if st.button("音声で確認"):
    if text_input:
        tts = gTTS(text=text_input, lang=language)
        tts.save("output.mp3")
        
        # 音声ファイルの再生
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
        
        # 音声ファイルのダウンロードリンク
        st.download_button(label="音声をダウンロード", data=audio_bytes, file_name="output.mp3", mime="audio/mp3")
    else:
        st.warning("エラーが起こりました。もう一度アクセスしてください")


st.write('')
st.write('')
st.write('')


st.markdown('##### 問１　以下の動画を視聴してから問いに答えなさい')
if st.button('問１：Play Video'):
    file_id = "1zI1o33IiblGtTmogzuuRxNhRZbrRbIsd" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m1.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m1.mp4")

st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ３問全て選んでから判定します。')
input_option4_1 = st.selectbox(
    '問1.1　平均値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=AVERAGE()', '=MEDIAN()', '=MODE()')
)
input_option4_2 = st.selectbox(
    '問1.2　中央値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=AVERAGE()', '=MEDIAN()', '=MODE()')
)
input_option4_3 = st.selectbox(
    '問1.3　最頻値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=AVERAGE()', '=MEDIAN()', '=MODE()')
)
n_ok=0
input_data = None
if input_option4_1 == '=AVERAGE()':
    n_ok =n_ok+1 
if input_option4_2 == '=MEDIAN()':
    n_ok=n_ok+1 
if input_option4_3 == '=MODE()':
    n_ok=n_ok+1 
if n_ok==3:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')


st.markdown('##### 問２　以下の動画を視聴してから問いに答えなさい')
if st.button('問２：Play Video'):
    file_id = "1tYKDUikEnwG5sBU84nrYVBbh8HrJbSqh" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m2.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m2.mp4")

st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ３問全て選んでから判定します。')
input_option5_1 = st.selectbox(
    '問2.1　最大値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=MAX()', '=MIN()', '=(最大値)-(最小値)')
)
input_option5_2 = st.selectbox(
    '問2.2　最小値を求めるエクセルの関数を選びなさい',
    ('選んでください', '=MAX()', '=MIN()', '=(最大値)-(最小値)')
)
input_option5_3 = st.selectbox(
    '問2.3　範囲を求めるエクセルの関数を選びなさい',
    ('選んでください', '=MAX()', '=MIN()', '=(最大値)-(最小値)')
)

n_ok=0
input_data = None
if input_option5_1 == '=MAX()':
    n_ok =n_ok+1 
if input_option5_2 == '=MIN()':
    n_ok=n_ok+1 
if input_option5_3 == '=(最大値)-(最小値)':
    n_ok=n_ok+1 
if n_ok==3:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')

#https://drive.google.com/file/d/1UnimUwdLjS4Y3TKSRtOsqq18cQERflbD/view?usp=sharing
st.markdown('##### 問３　以下の動画を視聴してから問いに答えなさい')
if st.button('問３：Play Video'):
    file_id = "1UnimUwdLjS4Y3TKSRtOsqq18cQERflbD" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m3.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m3.mp4")
image3 = Image.open('toi3.jpg')
st.image(image3,use_column_width=True)
st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ２問全て選んでから判定します。')
input_option6_1 = st.selectbox(
    '問3.1　C7セルに入れる関数を選びなさい',
    ('選んでください', '=IF(C7>=0,"OK","NG")', '=$B$4-$C$4*B7', '=IF(C7>=0,"NG","OK")')
)
input_option6_2 = st.selectbox(
    '問3.2　D7セルに入れる関数を選びなさい',
    ('選んでください', '=IF(C7>=0,"OK","NG")', '=$B$4-$C$4*B7', '=IF(C7>=0,"NG","OK")')
)
n_ok=0
input_data = None
if input_option6_1 == '=$B$4-$C$4*B7':
    n_ok =n_ok+1 
if input_option6_2 == '=IF(C7>=0,"OK","NG")':
    n_ok=n_ok+1 
if n_ok==2:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')

#https://drive.google.com/file/d/18Kwu9foqxlTzUSwdgbunvW4Nld_4ApW3/view?usp=sharing
st.markdown('##### 問４　以下の動画を視聴してから問いに答えなさい')
if st.button('問４：Play Video'):
    file_id = "18Kwu9foqxlTzUSwdgbunvW4Nld_4ApW3" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m4.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m4.mp4")

st.markdown('##### 適する用語をプルダウンからを選んでください。')
#st.markdown('##### ３問全て選んでから判定します。')
input_option7_1 = st.selectbox(
    '問4.1　相関係数を求めるエクセルの関数を選びなさい',
    ('選んでください', '=CORREL(C4:C8,D4:D8)', '=CORREL(C4,D4)', '=CORREL(C4:C8)')
)

n_ok=0
input_data = None
if input_option7_1 == '=CORREL(C4:C8,D4:D8)':
    n_ok =n_ok+1 
if n_ok==1:
    st.write('正解です。')
else :
    st.write('不正解です。動画を見直してください。')
st.write('')
st.write('')
st.write('')

# https://drive.google.com/file/d/1N4oz_jj1KfLtX_jCrLZCPb7sVmg52754/view?usp=sharing
st.markdown('##### 問５　以下の動画を視聴してから問いに答えなさい')
if st.button('問５：Play Video'):
    file_id = "1N4oz_jj1KfLtX_jCrLZCPb7sVmg52754" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m5.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m5.mp4")
image8 = Image.open('toi7.jpg')
st.image(image8,use_column_width=True)
st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ２問全て選んでから判定します。')
input_option8_1 = st.selectbox(
    '問5.1　エクセルのグラフにおいてオプションを追加するボタンはどれか',
    ('選んでください', '+', '-', '*')
)
input_option8_2 = st.selectbox(
    '問5.2　グラフにおいて外れ値は誰か',
    ('選んでください', 'A', 'B', 'C', 'D')
)
n_ok=0
input_data = None
if input_option8_1 == '+':
    n_ok =n_ok+1 
if input_option8_2 == 'D':
    n_ok=n_ok+1 
if n_ok==2:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')

# https://drive.google.com/file/d/1qa4j5mNrAKrGM_Zu_0W09NBZtKmEfnOa/view?usp=sharing
st.markdown('##### 問６　以下の動画を視聴してから問いに答えなさい')
if st.button('問６：Play Video'):
    file_id = "1qa4j5mNrAKrGM_Zu_0W09NBZtKmEfnOa" # 共有リンクからファイルIDを抽出
    download_link = f"https://drive.google.com/uc?id={file_id}" # ダウンロードリンクを生成
    response = requests.get(download_link)  # モデルをダウンロード
    with open("m6.mp4", "wb") as f: # モデルファイルを保存
        f.write(response.content)
    st.video("m6.mp4")
image9 = Image.open('toi9.jpg')
st.image(image9,use_column_width=True)
st.markdown('##### 適する用語をプルダウンからを選んでください。')
st.markdown('##### ３問全て選んでから判定します。')
input_option9_1 = st.selectbox(
    '問6.1　C4セルに入れる乱数の関数を選びなさい',
    ('選んでください', '=RANDBETWEEN(10)', '=RANDBETWEEN(1)', '=RANDBETWEEN(1,10)')
)
input_option9_2 = st.selectbox(
    '問6.2　D4セルに入れる関数を選びなさい',
    ('選んでください', '=IF(C4=0,"OK","NG")', '=IF(C4=1,"OK","NG")', '=IF(C4=1,"NG","OK")')
)
input_option9_3 = st.selectbox(
    '問6.3　再試行させる場合のキーを選びなさい',
    ('選んでください', 'F4', 'F7', 'F9')
)
n_ok=0
input_data = None
if input_option9_1 == '=RANDBETWEEN(1,10)':
    n_ok =n_ok+1 
if input_option9_2 == '=IF(C4=1,"OK","NG")':
    n_ok=n_ok+1 
if input_option9_3 == 'F9':
    n_ok=n_ok+1 
if n_ok==3:
    st.write('全問正解です。')
else :
    st.write('不正解です。何処かが間違っています。動画を見直してください。')
st.write('')
st.write('')
st.write('')


st.write('問７　以下の図で示したノギスの各部の名称を答えよ')
image = Image.open('nogisu_name.jpg')
st.image(image,use_column_width=True)

input_option4_1 = st.selectbox(
    '①の名称',('選んでください','スライダー', '外側用ジョウ', 'バーニヤ目盛り',\
    '内側用ジョウ','止めねじ', 'デプスバー', '本尺')
)
input_option4_2 = st.selectbox(
    '②の名称',('選んでください','スライダー', '外側用ジョウ', 'バーニヤ目盛り',\
    '内側用ジョウ','止めねじ', 'デプスバー', '本尺')
)
input_option4_3 = st.selectbox(
    '③の名称',('選んでください','スライダー', '外側用ジョウ', 'バーニヤ目盛り',\
    '内側用ジョウ','止めねじ', 'デプスバー', '本尺')
)
input_option4_4 = st.selectbox(
    '④の名称',('選んでください','スライダー', '外側用ジョウ', 'バーニヤ目盛り',\
    '内側用ジョウ','止めねじ', 'デプスバー', '本尺')
)
input_option4_5 = st.selectbox(
    '⑤の名称',('選んでください','スライダー', '外側用ジョウ', 'バーニヤ目盛り',\
    '内側用ジョウ','止めねじ', 'デプスバー', '本尺')
)
input_option4_6 = st.selectbox(
    '⑥の名称',('選んでください','スライダー', '外側用ジョウ', 'バーニヤ目盛り',\
    '内側用ジョウ','止めねじ', 'デプスバー', '本尺')
)
input_option4_7 = st.selectbox(
    '⑦の名称',('選んでください','スライダー', '外側用ジョウ', 'バーニヤ目盛り',\
    '内側用ジョウ','止めねじ', 'デプスバー', '本尺')
)

n_ok=0
input_data = None
if input_option4_1 == '内側用ジョウ':
    n_ok =n_ok+1 
if input_option4_2 == '止めねじ':
    n_ok=n_ok+1 
if input_option4_3 == '本尺':
    n_ok=n_ok+1 
if input_option4_4 == 'デプスバー':
    n_ok=n_ok+1
if input_option4_5 == '外側用ジョウ':
    n_ok=n_ok+1 
if input_option4_6 == 'スライダー':
    n_ok=n_ok+1 
if input_option4_7 == 'バーニヤ目盛り':
    n_ok=n_ok+1  
if n_ok==7:
    st.write('ノギスの名称、全問正解です。')
else :
    st.write('不正解です。見直してください。')
st.write('')
st.write('')
st.write('')
st.write('')

st.markdown('##### 適する数値を入力してください。')
st.write('問８　以下の図で示したノギスの測定値を答えよ')
image = Image.open('nogisu_ex.jpg')
st.image(image,use_column_width=True)

input_option5_1=st.number_input('問１',20.00,80.00,25.00,step=0.05)
input_option5_2=st.number_input('問２',20.00,80.00,35.00,step=0.05)
input_option5_3=st.number_input('問３',20.00,80.00,20.00,step=0.05)

n_ok=0
input_data = None
if input_option5_1 == 28.40:
    n_ok =n_ok+1 
if input_option5_2 == 39.85:
    n_ok=n_ok+1 
if input_option5_3 == 21.25:
    n_ok=n_ok+1  
if n_ok==3:
    st.write('ノギスの計測、全問正解です。')
    st.markdown('### お疲れ様でした。')
else :
    st.write('不正解です。見直してください。')
st.write('')
st.write('')
st.write('')

st.markdown('### 問題は以上です。お疲れさまでした。では、皆さまの考査での健闘をお祈りしています。')










