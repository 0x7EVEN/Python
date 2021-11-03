import subprocess
count = 1000

def visiter(count):
     if count == 0:
          print("Success !")
          return
     r = subprocess.run(['echo', 'hello timeout'], timeout=50)
     print(
          f'''type(r)={type(r)},
          r.args={r.args},
          r.returncode={r.returncode},
          r.stdout={r.stdout},
          r.stderr={r.stderr}'''
     )
     try:
          r = subprocess.run(['curl', 'https://visitor-badge.glitch.me/badge?page_id=0x7EVEN'], timeout=50)
          r = subprocess.run(['sleep', '10'], timeout=50)
          visiter(count-1)
     except subprocess.TimeoutExpired as e:
          print(e)
visiter(1000)