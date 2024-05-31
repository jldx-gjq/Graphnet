import matplotlib.pyplot as plt
import numpy as np

font_path = '/path/to/your/chinese/font.ttf'

# 设置中文显示字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 你也可以替换成其他中文字体
plt.rcParams['axes.unicode_minus'] = False  # 如果字体有减号字符，取消这行注释

np.random.seed(0)

# Create time slots data points
time_slots = np.arange(0, 800)

# Create a base line with linear growth
base_line = time_slots * 0.4  # assuming each time slot cost increases by 0.4 on average

# Add sinusoidal fluctuations with faster frequency and smaller amplitude
fluctuations = 5 * np.sin(0.1 * np.pi * time_slots)  # increasing the frequency

# Combine the base line growth and fluctuations
costs = base_line + fluctuations
plt.figure(figsize=(10, 6))
plt.plot(time_slots, costs, label='Cost')
plt.xlabel('时间段t')
plt.ylabel('总成本')
plt.title('不同时间段的成本曲线')
plt.legend()
plt.savefig('2')
plt.show()
