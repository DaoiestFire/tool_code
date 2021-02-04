# MP4toPNG
convert a .mp4 video to .png image,save all images to same name folder

# 作用
* 视频训练数据转换成png格式的图片可以加快网络的训练。实际使用时，我的训练速度快了一倍。说明处理压缩的视频数据确实花费了很多的计算资源。
* 所以与处理好数据集可以方便数据加载，batch也可以更大
# 用法
* 如果一个文件夹A，包含多个文件夹如1，2，3.直接运行该python文件，像这样：

```python MP4topng.py --root 文件夹a的路径```
* 程序会在文件夹A下面创建1_processed等文件夹，包含处理好的数据
