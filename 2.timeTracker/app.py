import time

# Request the name of the job
job_name = input("What are you doing right now? : \n")
# Get start time of the app and job
job_start_time = time.time()
# Loop and check if the job is end

try:
    while True:

        # Check if the job is end
        user_input = input(f'Are you done with {job_name}? y/n :')
        if(user_input == 'y'):
        # diff the time and show the time taking for a job
            job_end_time = time.time()
            time_spend = job_end_time - job_start_time

            print(f"{round(time_spend,2)} seconds was taken for {job_name}")
            # check if user want to start another job and ask for the job name if needed
            job_name = input(f"So, what are you going to do next? \n")
            job_start_time = time.time()
        else:
            print("Okay, we will keep waiting")
     # end the job on keyboard interrupt as well for Ctrl+C Exist
except KeyboardInterrupt:
    print("\nQuitting...")
# create a shell/bat file to run from anywhere

# chmod +x in linux to execute the script
