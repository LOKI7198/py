import boto3
ec2 = boto3.resource('ec2')

# create a file to store the key locally
outfile = open('D:/testing123.pem','w')

# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName='testing123')

# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)
outfile.close()
