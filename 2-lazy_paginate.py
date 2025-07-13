def paginate_users(page_size,offeset):
  all_users= [f"User_{i} for i in range(1,101)"]
  start = offset
  end = offset + page_size
  return all_users[start:end]

def lazy_paginate(page_size)
offset=0
current_page =[]
index= 0

while True:
  if index >= len(current_page):
    current_page= paginate_users(page_size,offset)
    if not current_page
    break
    offset +=page_size
    index=0

if index < len(current_page)
yield current_page[index]
index+= 1
