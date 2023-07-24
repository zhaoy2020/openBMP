
# 提取
## aodaili
python faceswap.py extract -i  FaceSwapWorkStation/Raws/Video/AoDaiLi/AoDaiLi.mp4  -o FaceSwapWorkStation/ExtracOutput/AoDaiLiTem/
## ai
python faceswap.py extract -i  FaceSwapWorkStation/Raws/Picture/Ai/  -o FaceSwapWorkStation/ExtracOutput/AiTem/
## wuyanzu
python faceswap.py extract -i  FaceSwapWorkStation/Raws/Video/WuYanzu/WuYanzu.mp4  -o FaceSwapWorkStation/ExtracOutput/WuYanzuTem/

# 训练
python faceswap.py  train -A FaceSwapWorkStation/ExtracOutput/AoDaiLi -B  FaceSwapWorkStation/ExtracOutput/WuYanzu/ -m FaceSwapWorkStation/Models/

# 替换
## 只是图片
python faceswap.py convert -i ./Raws/video/AoDaiLi/AoDaiLi.mp4  -o ./Output -m ./Models/AiVSAoDaiLiModels
## 串联图片成视频
python tools.py effmpeg  -i  ./Output -r ./Raws/video/AoDaiLi/AoDaiLi.mp4 -o ./Output/Ai2AoDaiLi.mp4 -a gen-vid
