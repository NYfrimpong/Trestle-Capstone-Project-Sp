[AWS]
access_key_id = CAPSTONE PROJECT
secret_access_key = @NAt0244

[IAM]
role_name = KinesisFirehoseWritesToS3
policy_name = KinesisWritesToS3frimpongbucket  

[Firehose]
region = eu-north-1 
stream_name = PUT-S3-p3zSR 
delivery_stream_type = 'DirectPut'
size_in_mb = 5 
interval_in_seconds = 60
compression_format = 'GZIP' 

[s3] 
bucket_name = frimpongbucket 