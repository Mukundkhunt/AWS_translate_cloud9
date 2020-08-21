import boto3

client = boto3.client('translate', region_name='ap-south-1')
text = "Hola mi nombre es Noah"
result=client.translate_text(Text=text, SourceLanguageCode='auto', TargetLanguageCode='en')
print(result['TranslatedText'])
