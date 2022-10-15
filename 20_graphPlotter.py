import matplotlib.pyplot as plt

# x1= [2, 5, 9, 12, 17]
# y1= [2, 3, 5, 11, 15]

# # x2= [3, 4, 8, 11, 13]
# # y2= [2, 3, 5, 10, 12]

# plt.plot(x1, y1, color='green',linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)
# # plt.plot(x1, y1, label = 'Line 1')
# # plt.plot(x2, y2, label = 'Line 2')

# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.title('DemoGraphCustom')
# # plt.legend()
# plt.show()

left = [1,2,3,4,5,6,7,8,9]
height = [10,12,14,8,7,23,15,13,19]

tick_label = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['blue', 'orange'])

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('DemoBarChartCustom')

plt.show()