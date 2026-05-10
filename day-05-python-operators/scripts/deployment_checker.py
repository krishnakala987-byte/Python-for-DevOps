import sys

deployment_status = sys.argv[1]

if deployment_status != "success":
    print("Rollback Deployment")

else:
    print("Deployment Successful")