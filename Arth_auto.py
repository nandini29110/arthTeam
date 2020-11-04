import os
print("----------------------------------------WELCOME!--------------------------------------- ")
os.system("aws configure")
print("""
          CHOOSE THE SERVICES OF AWS -
          PRESS- 
          1. EC2 
          2. EBS
          3. S3
          4. CloudFront
          5. CloudTrial

""")
service = int(input())
if service == 1:
    print("""
                  PRESS:
                        1: LAUNCH THE OS
                        2: START THE EXISTING OS
    """)
    ec2_input=int(input())
    if ec2_input == 1:
             key_name=input("Enter key name")
             os.system("aws ec2 create-key-pair –key-name {}".format(key_name))
        else :
             key_name=input("Enter key name")     
        print(""""
                PRESS:
                1. CREATE SECURITY GROUP
                2. USE EXISTING SECURITY GROUP
        """)
        security = int(input())
        if security == 1:
                 security_group_name = input("Enter security group name")
                 security_description = input("Enter Security Group Description")
                 os.system("aws ec2 create-security-group --group-name {0} --description {1}".format(security_group_name,security_description))
        #else :
            #list the existing security groups
        print("""
                       SELECT THE IMAGE FOR LAUNCHING THE OS , PRESS -
                       1. Amazon Linux 2 AMI (HVM)
                       2. Red Hat Enterprise Linux 8 (HVM)
                       3. SUSE Linux Enterprise Server 15 SP2 (HVM)
                       4. Ubuntu Server 20.04 LTS (HVM)
                       5. Microsoft Windows Server 2019 Base

        """)
        image = int(input())
        print(""""
                   Choose an Instance Type , PRESS -
                   1. t2.nano
                   2. t2.micro
                   3. t2.small
                   4. t2.medium
                   5. t2.large
        """)
        instance_type_no=int(input())
        if instance_type_no ==1:
            instance_type="t2.nano"
        elif instance_type_no ==2:
            instance_type="t2.micro"
        elif instance_type_no ==3:
            instance_type="t2.small"
        elif instance_type_no ==4:
            instance_type="t2.medium"
        elif instance_type_no ==5: 
            instance_type="t2.large"               
        instance_no = int(input())
        no_of_instance=input("Enter no of instances")
        os.system("aws ec2 run-instances –image-id ami-03cfb5e1fb4fac428 –instance-type {1} –count {2} –subnet-id subnet-6b050003 –security-group-ids sg-0a21d2c1e37e172f4 –key-name {0}".format(key_name,instance_type,no_of_instance))

    else:
        instance_id=input("Enter the correct instance ID ")
        os.system("aws ec2 start-instances --instance-ids {}".format(instance_id))
        print("\n\t\t INSTANCE HAS BEEN STARTED\n")
#elif service ==2:
#elif service == 3:
#elif service == 4:
#elif service == 5:
else :
    print("SERVICE NOT AVAILABLE")    
print("hello")                    
