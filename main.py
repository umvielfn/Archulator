import time
#Introduction
print("Welcome to Archulator!")
print(" ")
print(" _____________________")
print("|  _________________  |")
print("| |   ARCHULATOR    | |")
print("| |_________________| |")
print("|  ___ ___ ___   ___  |")
print("| | 7 | 8 | 9 | | + | |")
print("| |___|___|___| |___| |")
print("| | 4 | 5 | 6 | | - | |")
print("| |___|___|___| |___| |")
print("| | 1 | 2 | 3 | | x | |")
print("| |___|___|___| |___| |")
print("| | . | 0 | = | | / | |")
print("| |___|___|___| |___| |")
print("|_____________________|")
print(" ")
# collection information
collection = str(input("What collection are you working on? "))
print(" ")
print(collection + "? Sounds fascinating! Let's get started then, shall we?")
print(" ")
time.sleep(1.5)
collection_size = float(input("Can you tell me how many GB is in your collection? "))
media_count = float(input("How many storage devices does the collection include? "))

print("Perfect! Let me crunch those numbers for you!")
# calculator variables and math
#Note: All values are just examples now and not based on real processing work
#Estimated Time per GB

accession_time = 1 * collection_size
appraisal_time = 1 * collection_size
transfer_time = 0.1425 * collection_size
processing_time = 0.75 * collection_size
preservation_time = 0.3 * collection_size
media_processing = 1 * media_count
supervision_time = 0.2 * collection_size
training_time = 20
time.sleep(1.5)
print(" ")
print("...")
print(" ")
time.sleep(1.5)
# Results
print("Your collection will take " + str(appraisal_time + accession_time + transfer_time + processing_time + preservation_time + media_processing + supervision_time + training_time) + " to process.")
print(" ")
print("This includes:")
print(" ")
print("Hours to appraise: " + str(appraisal_time))
print("Hours to accession: " + str(accession_time))
print("Hours to transfer files to your systems: " + str(transfer_time + media_processing))
print("Hours to process collection: " + str(processing_time))
print("Hours to preserve collection: " + str(preservation_time))
print("Hours to supervise staff: " + str(supervision_time))
print("Hours to train staff: " + str(training_time))
print("")
print("Don't forget, this is just an estimator!")
print(" ")
print("Please allow for more time if your collection includes a significant number of PII, larger types of file formats, or many formats that may need to be investigated and/or manually normalized.")
print(" ")
print("Your computer's processing speed, and the existence of analog records that need to be integrated into the final collection will also impact the time required for processing")
print("")
print("Goodbye for now!")

# Possible addtions could include adding a salary component to try and come up with a cost for hiring someone to process collection.
# add what the specs for the computer this program is based on our. See if you coudl add some methods of pulling specs from a computer and displaying them here if someone wants to know theirs
#Generate results as a report that can be printed/accessed?
#Build complementary tool to more accurately time some of the activities that occur, like imaging, reports generation, etc.
#Could a json file be helpful here, as a way for anyone repurposing this tool for their own estimations to more easily enter values that are more realistic to their institution?