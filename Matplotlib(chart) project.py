import matplotlib.pyplot as plt


study_hours = [1, 2, 3, 4, 5, 6, 7]
marks = [35, 40, 50, 60, 70, 80, 90]

subjects = ["Math", "Science", "English", "Computer"]
subject_marks = [85, 78, 72, 90]

attendance = [60, 65, 70, 75, 80, 85, 90]

time_spent = [30, 25, 20, 25]  

marks_distribution = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# ------------------ Subplots ------------------
plt.figure(figsize=(10, 8))

# Line Chart
plt.subplot(2, 3, 1)
plt.plot(study_hours, marks, color="blue", marker="o")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid()

#  Bar Chart
plt.subplot(2, 3, 2)
plt.bar(subjects, subject_marks, color=["red", "green", "blue", "orange"])
plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Scatter Chart
plt.subplot(2, 3, 3)
plt.scatter(attendance, marks, color="purple")
plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")

# Pie Chart
plt.subplot(2, 3, 4)
plt.pie(time_spent, labels=subjects, autopct="%1.1f%%")
plt.title("Time Spent on Subjects")

# Histogram
plt.subplot(2, 3, 5)
plt.hist(marks_distribution, bins=5, color="cyan", edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


