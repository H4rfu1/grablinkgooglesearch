from googlesearch import search 
import csv  

def main():
  links = []
  type = input('Save type? csv | txt | (blank for console print out) :')
  query = input('Query Search: ')
  filename = input('File Name: ')
  count = int(input('Max Search: '))
  # 101
  for j in search(query, tld="co.id", num=10, stop=count, pause=2): 
      links.append(j)
  # print(len(links))
  if(type == 'csv'):
    with open(f'{filename}.csv', 'w') as f:
      # using csv.writer method from CSV package
      write = csv.writer(f)
      write.writerow(['url'])
      write.writerows([ [i] for i in links ])
  elif(type == 'txt'):
    with open(f'{filename}.txt', 'w') as f:
      f.write("%s :\n" % query)
      for item in links:
          f.write("%s\n" % item)
  else:
      print("%s :\n" % query)
      for item in links:
          print("%s\n" % item)
  return links

if __name__ == "__main__":
 main()