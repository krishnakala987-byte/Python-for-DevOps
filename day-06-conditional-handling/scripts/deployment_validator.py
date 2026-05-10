import sys

deployment_status = sys.argv[1]

if deployment_status == "success":
    print("Deployment Successful")

else:
    print("Rollback Deployment")