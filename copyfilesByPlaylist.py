import shutil
from pathlib import Path
from datetime import datetime
import pandas as pd


# ---------------------------------------------------------
# [テスト]プレイリストのパス
playlist_path = r''

# [テスト]コピー先のSDカードのパス
copy_destination_sdcard_path = r''
# ---------------------------------------------------------

print(f'copy start at {datetime.now()}')

# プレイリスト読み込み
df = pd.read_csv(playlist_path, sep='\t', encoding='utf-16')

# 「場所」列からコピー元のファイルパスを取得
pathlist = list(df['場所'])

# カウンター
cnt      = 0
file_cnt = len(pathlist)

# ファイルごとに繰り返し
for path in pathlist:
    cnt += 1

    # 元パスを表示
    print(f'{cnt}/{file_cnt} : {path}')

    # 元パスからアーティスト名、アルバム名、ファイル名を取得
    splited_path = path.split('/Media.localized/Music/')[1].split('/')
    artist_name  = splited_path[0]
    album_name   = splited_path[1]
    file_name    = splited_path[2]

    # フォルダ構成からコピー先フォルダパスを作成
    destination_parent = Path(copy_destination_sdcard_path, 'MUSIC/Music', artist_name, album_name)

    # ファイルの存在確認
    destination = destination_parent / Path(file_name)
    if destination.exists() :
        print("[-] SKIP : FILE EXIST")
        continue

    # コピー先フォルダパスを作成(存在してもエラーにしない)
    destination_parent.mkdir(parents=True, exist_ok=True)

    # ファイルをコピー
    shutil.copy(Path('/Volumes/', path), destination)
    print("[o] COPY SUCCESS")

print(f'copy end at {datetime.now()}')

'''
メモ:コピー先SDのフォルダ構成
% tree
.
├── DevIcon.fil
├── DevLogo.fil
├── MUSIC
|   ├── Music   // <-ここがルート(/Volumes/%SD_CARD_NAME%/MUSIC/Music)
│   └── MUSICCLIP
├── capability_00.xml
└── default-capability.xml
'''