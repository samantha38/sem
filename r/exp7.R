
# EXPERIMENT 7: DATA ANALYSIS AND VISUALIZATION USING R

# PART A: LOAD DATASET

students <- read.csv("students.csv")

# PART B: DATA EXPLORATION

print(dim(students))
str(students)
head(students)
summary(students)
print(colSums(is.na(students)))

# PART C: DATA ANALYSIS

# Average marks by department
marks_by_dept <- aggregate(Marks ~ Department,
                           data=students, FUN=mean)
print(marks_by_dept)

# Students by gender
gender_count <- table(students$Gender)
print(gender_count)

# Correlation
print(cor(students$Study_Hours, students$Marks))

# Linear regression
model <- lm(Marks ~ Study_Hours, data=students)
print(summary(model))

# PART D: DATA VISUALIZATION

dir.create("plots", showWarnings=FALSE)

# 1. BAR CHART

png("plots/01_barchart.png", width=900, height=650)

barplot(marks_by_dept$Marks,
        names.arg=marks_by_dept$Department,
        main="Average Marks by Department",
        xlab="Department",
        ylab="Average Marks",
        col="grey70")

dev.off()

# 2. PIE CHART

png("plots/02_piechart.png", width=900, height=650)

pie(gender_count,
    labels=names(gender_count),
    main="Student Distribution by Gender",
    col=c("grey60", "grey85"))

dev.off()

# 3. LINE CHART

png("plots/03_linechart.png", width=900, height=650)

plot(students$Student_ID, students$Marks,
     type="b",
     main="Student Marks",
     xlab="Student ID",
     ylab="Marks",
     pch=19)

dev.off()

# 4. HISTOGRAM

png("plots/04_histogram.png", width=900, height=650)

hist(students$Marks,
     breaks=seq(30, 100, by=10),
     main="Distribution of Student Marks",
     xlab="Marks",
     ylab="Frequency",
     col="grey70")

dev.off()

# PART E: OUTPUT

cat("All four plots generated successfully!\n")
print(list.files("plots"))

# Rscript exp7.R