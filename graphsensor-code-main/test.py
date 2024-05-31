import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定字体
font = FontProperties(fname='/path/to/your/font.ttf')

# 使用指定字体绘图
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 或者你的其他中文字体
plt.rcParams['axes.unicode_minus'] = False  # 如果你的字体有减号字符，取消这行注释

plt.text(0.5, 0.5, '室', fontproperties=font)  # 以示例绘制一个中文字符
plt.show()