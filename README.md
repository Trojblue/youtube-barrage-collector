# youtube-barrage-collector





适用于独轮车的youtube评论下载器

- 去除表情和日语评论
- 评论去重, 只保留不相同的评论 (大小写视为相同)
- 输出到txt, 方便复制进独轮车使用

修改自 https://github.com/shughes-uk/python-youtubechat



## 使用:

```bash
python barrage.py <youtube视频地址> -o <name>.txt
```







## 例子:

`demo.txt` 节选 (来自面包狗直播间):

```
YEY CATTO AND DOGGO
HOI HOI HOI HOI HOI
SEMONGKO BEST
yeh
OKAYU LANG SAKALAM
L-O-L L-O-L
OKAYUUU WOW
YOOOOO OKAYU
i forgot the song name. can someone tell me?
WONDERFUL
YAAAAAAAASSS
bravoooooo
Semongko mulu lah oii
Tereeek ses
these two are so cute i love it
AAAAAAAA SO CUTEEEEE
Sugoiiiiiii
indo hadir mang
BEST SINGING EVER
ah yes
cmon s
```





## TODO

1. NLP判断词语情感, 只输出负面感情的
2. 加入日语支持