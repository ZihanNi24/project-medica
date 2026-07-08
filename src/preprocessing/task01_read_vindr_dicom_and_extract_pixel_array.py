# Ⅰ. 确认数据集主路径

# 从 pathlib 工具箱导入路径工具 Path
from pathlib import Path

# DATA_ROOT 是数据集主路径
# Path(...) 的作用是：把长得像路径的一长串字符串变成路径对象
# 并把它命名为 DATA_ROOT
DATA_ROOT = Path("/kaggle/input/competitions/vinbigdata-chest-xray-abnormalities-detection")

# 打印数据集路径，确认当前使用的是哪个数据集文件夹
print("数据集路径：", DATA_ROOT)

# DATA_ROOT.exists() 用来检查这个路径是否真的存在
print("这个路径是否存在：", DATA_ROOT.exists())

# \n 是换行符，用来让输出更清楚
print("\n数据集里面有这些东西：")

# DATA_ROOT.iterdir() = 查看 DATA_ROOT 文件夹第一层内容
# for item in ... 表示把文件夹里的内容一个一个取出来
for item in DATA_ROOT.iterdir():
    # 打印每一个第一层文件或文件夹
    print(item)


# Ⅱ. 找到训练图像文件夹

# 在 DATA_ROOT 数据集总文件夹下面，找到 train 这个子文件夹
# 并把它保存为 TRAIN_DIR
# 这里的 / 不是除法，而是 Path 里的路径拼接
TRAIN_DIR = DATA_ROOT / "train"

# 打印训练图像文件夹路径
print("\n训练图像文件夹：", TRAIN_DIR)

# 检查 train 文件夹是否真的存在
print("这个文件夹是否存在：", TRAIN_DIR.exists())


# Ⅲ. 找出所有 DICOM 图像

# TRAIN_DIR.glob("*.dicom") 用来在 train 文件夹里查找所有 .dicom 文件
# *.dicom 的意思是：任意文件名 + .dicom 后缀
# glob 找到的是“可以逐个取出的对象”
# list(...) 把它整理成真正的 Python 列表
# dicom_files 里面保存所有训练 DICOM 图像路径
dicom_files = list(TRAIN_DIR.glob("*.dicom"))

# len(dicom_files) 用来计算 dicom_files 这个列表里有多少个元素
# 这里就是统计找到了多少张 DICOM 图像
print("\n找到训练 DICOM 数量：", len(dicom_files))

# 打印前 5 张 DICOM 的路径，方便检查是否真的找到了图像文件
print("前 5 张 DICOM：")

# dicom_files[:5] 表示从 dicom_files 列表里取前 5 个元素
# for path in ... 表示把前 5 个路径一个一个取出来
for path in dicom_files[:5]:
    # 打印当前这一个 DICOM 路径
    print(path)


# Ⅳ. 读取第一张 DICOM

# pydicom 是专门用来读取 DICOM 医学影像文件的工具包
import pydicom

# numpy 是 Python 里处理矩阵、数组、图像像素值最常用的工具
# as np 表示以后把 numpy 简写成 np
import numpy as np

# dicom_files[0] 表示取 dicom_files 列表里的第一个元素
# 也就是第一张 DICOM 图像的路径
first_dicom_path = dicom_files[0]

# 打印提示文字
print("\n准备读取这一张：")

# 打印准备读取的 DICOM 文件路径
print(first_dicom_path)

# 使用 pydicom 读取 first_dicom_path 这张 DICOM 文件
# 读取到的完整 DICOM 数据对象保存为 ds
# ds 里面既有图像像素数据，也有 DICOM 元数据
ds = pydicom.dcmread(first_dicom_path)

# 从 ds 这个 DICOM 对象中提取图像像素数组
# 也就是把 DICOM 文件里的图像部分拿出来，变成一个矩阵
# 并存到 pixel_array 这个变量里
pixel_array = ds.pixel_array

# 如果程序运行到这里，说明 DICOM 文件读取成功，pixel_array 也提取成功
print("\n读取成功")

# type(pixel_array) 用来查看 pixel_array 的数据类型
# 正常情况下应该是 numpy.ndarray
print("pixel_array 类型：", type(pixel_array))

# pixel_array.shape 用来查看图像矩阵的形状
# 对灰度图来说，一般是 height, width
# 例如 (3000, 3000) 表示高 3000 像素，宽 3000 像素
print("pixel_array 形状：", pixel_array.shape)

# pixel_array.dtype 用来查看像素值的数据类型
# 医学 DICOM 图像常见是 uint16
print("pixel_array 数据类型：", pixel_array.dtype)

# np.min(pixel_array) 用来查看整张图像里的最小像素值
print("最小像素值：", np.min(pixel_array))

# np.max(pixel_array) 用来查看整张图像里的最大像素值
print("最大像素值：", np.max(pixel_array))


# Ⅴ. 显示图像

# matplotlib 是 Python 里常用的画图工具
# matplotlib.pyplot 是 matplotlib 里的绘图接口
# as plt 表示以后把 matplotlib.pyplot 简写成 plt
import matplotlib.pyplot as plt

# 创建一个显示画布
# figsize=(6, 6) 表示画布宽 6，高 6
# 注意这里是显示画布大小，不是图像真实像素大小
plt.figure(figsize=(6, 6))

# imshow = image show，用来把图像矩阵显示成图片
# pixel_array 是前面从 DICOM 中提取出来的图像矩阵
# cmap="gray" 表示用灰度颜色表显示图片
plt.imshow(pixel_array, cmap="gray")

# 关闭坐标轴，因为我们现在只是查看胸片，不需要 x/y 坐标
plt.axis("off")

# 给显示出来的图片加标题
plt.title("Raw DICOM pixel_array")

# 真正把图片显示出来
plt.show()
