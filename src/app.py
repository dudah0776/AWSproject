import os
import sys
import json
import urllib.request
from flask import Flask, render_template, request, jsonify
import boto3
from boto.s3.connection import S3Connection, Bucket, Key

app = Flask(__name__)
def s3_connect():
    try:
        s3 = boto3.client('s3') #s3버킷과 연동
    except Exception as e:
        print(e)
        exit('ERROR_S3_CONNECTION_FAILED')
    else:
        print('bucket connected')
        return s3
def s3_put_object(s3, bucket, filepath, access_key):
    try:
        s3.upload_file(filepath, bucket, access_key)
    except Exception as e:
        print(e)
    return 'Success'

def detect_text(photo, bucket):
    str=''
    client = boto3.client('rekognition')
    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})
    textDetections = response['TextDetections']
    print('Detected text\n----------')
    for text in textDetections:
        print('Detected text:' + text['DetectedText'])
        # print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        # print('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            str+=(text['DetectedText']+' ')
            print('Parent Id: {}'.format(text['ParentId']))
            # print('Type:' + text['Type'])
            print()
    return str

def translate_text(full_text):
    client_id = "clientKey" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "clientSecret" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(full_text)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        res = json.loads(response_body.decode('utf-8'))
        trans_text = res['message']['result']['translatedText']
        print('res : ', trans_text)
        return trans_text
    else:
        print("Error Code:" + rescode)
        return False
        
def make_empty_bucket(s3, bucket):
    bucket=s3.Bucket(bucket)
    bucket.objects.all().delete()
    return 'bucket clear success'

s3=s3_connect()
bucket='koobucketest'
full_text=''
trans_text=''
count=0
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def file_upload(count):
    file=request.files['chooseFile']
    photo_name=file.filename
    s3.put_object(
        ACL='public-read',
        Bucket=bucket,
        Body=file,
        Key=file.filename,
        ContentType=file.content_type)
    print('file2:', photo_name)
    full_text=detect_text(photo_name, bucket)
    print('fulltext:',full_text)
    trans_text=translate_text(full_text)
    print('transtext:',trans_text)
    if count > 1000:
        make_empty_bucket(s3, bucket)
    return render_template('index.html', full_text=full_text, trans_text=trans_text, photo_name=photo_name), count
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")
