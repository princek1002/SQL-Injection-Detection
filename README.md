# SQL-Injection-Detection
SQL Injection is one of the most common and dangerous web application vulnerabilities that allows attackers to interfere with the queries an application makes to its database. Detecting and preventing such attacks is a critical aspect of securing any application that relies on a backend database. This project aims to develop a Machine Learning-based detection system that can classify SQL injection attempts from benign inputs, offering a proactive layer of defense.

🧠 Objective
The main goal of this project is to build an intelligent and automated system that can effectively detect SQL injection attempts in user inputs using machine learning. By training models on pre-labeled data, the system can learn the patterns and signatures typical of SQL attacks, and distinguish them from legitimate user behavior.

🗂️ Dataset
The original dataset used is named sql.csv. It contains both malicious and benign SQL queries labeled accordingly.

The dataset includes various SQL query patterns typically used in injection attacks such as tautologies, union-based attacks, piggybacked queries, etc., as well as normal user input samples.

🧹 Data Cleaning & Preprocessing
The raw dataset sql.csv was first cleaned to remove noise, duplicate entries, and missing values.

Text-based features were preprocessed using techniques such as:

Lowercasing

Removing special characters (where applicable)

Tokenization or vectorization (e.g., TF-IDF, CountVectorizer)

The cleaned dataset was saved as sqll.csv and used for training and testing ML models.

🤖 Machine Learning Pipeline
The following models were trained and evaluated:

Logistic Regression

Random Forest Classifier

Support Vector Machine (SVM)

Decision Tree

Feature extraction was applied to convert textual SQL input into numerical format suitable for training.

The dataset was split into training and testing sets (typically 80/20 split).

Model performance was evaluated using accuracy, precision, recall, and F1-score.

📈 Results
The best performing model achieved an accuracy of XX% (replace with your actual results).

Confusion matrix and classification report were generated to analyze false positives/negatives.

Models demonstrated good generalization capability on unseen SQL input patterns.

🛠️ Tech Stack
Python

Pandas, NumPy (for data handling and preprocessing)

Scikit-learn (for ML models and evaluation)

Jupyter Notebook / Streamlit (optional, if used for demo or visualization)

✅ Outcomes
Successfully developed a lightweight SQL Injection detection system using ML.

Demonstrated that ML models can be effective in identifying injection patterns.

The approach can be integrated into web applications for real-time threat detection.
