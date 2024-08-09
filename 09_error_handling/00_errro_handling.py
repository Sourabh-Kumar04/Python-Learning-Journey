
file = open('youtube_manager.py', 'w')

try:
    file.write('raso aur code')
finally:
    file.close()


with open('youtube_manager.py', 'w') as file:
    file.write('raso aur code')