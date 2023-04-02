import matplotlib.pyplot as plt


student = [1, 2, 3, 4, 5]

height = [30, 40, 10, 8, 40]

tick_label = ['Jamian', "Joshua", "Aryan", "Atputhan", "Leia"]

plt.bar(student, height, tick_label = tick_label,
        width = 0.9, color = ["lightgreen", "maroon", "darkgreen", "aqua", "violet"])

plt.xlabel("Name of Students")

plt.ylabel("Student Height")

plt.title("Student Heights Comparison")

plt.show