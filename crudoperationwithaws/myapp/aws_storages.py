from storages.backends.s3boto3 import S3Boto3Storage


class DynamicFiles(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
