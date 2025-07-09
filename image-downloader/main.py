import requests


def main():
    with open('links.txt','r') as links_file:
        links = links_file.read().splitlines() 
    for i,link in enumerate(links, start=1):
        download_Img(link,i)

    
def get_extension(url) -> str|None:
   extensions = ['.png', '.jpg', '.jpeg']

   for ext in extensions:
      if ext in url:
         return ext

   
   


def download_Img(url,i):
  try:  
    response = requests.get(url)
    extension = get_extension(url)
    if not extension: 
       extension = '.png'
    file_name = 'image'+str(i) + extension

    with open(file_name, 'wb') as image:
        image.write(response.content)

  except Exception as e:
     print(f'Error saving the image: {e}')

main()