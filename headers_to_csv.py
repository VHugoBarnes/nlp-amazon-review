# We read the existing text from the file in READ MODE
train_source_file = open("train.csv", "r")
test_source_file = open("test.csv", "r")

#New headers
headers_both_files = "index,review_title,review_text\n"

# Read files
lines_train_source_file = train_source_file.readlines()
lines_test_source_file = test_source_file.readlines()

# Prepend `headers_both_files` on the first line of both files
lines_train_source_file.insert(0, headers_both_files)
train_source_file.close()

lines_test_source_file.insert(0, headers_both_files)
test_source_file.close()

# Open the files in WRITE MODE
train_source_file = open("train.csv", "w")
test_source_file = open("test.csv", "w")

train_source_file.writelines(lines_train_source_file)
train_source_file.close()

test_source_file.writelines(lines_test_source_file)
test_source_file.close()

print('Done')