from datetime import datetime

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

tag=open('/tag.txt', 'r')
tag=tag.read()

with open('log.md', 'w') as f:
    f.write(f'# {timestamp, tag}')
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
