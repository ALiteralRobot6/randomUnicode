import unicodedata
import win10toast
from win10toast import ToastNotifier
toast = ToastNotifier()
f = open("unicodeName.txt", "a")
f.write('\n')
for i in range(917631):
    char = chr(i)
    name = unicodedata.name(char, 'UNNAMED')
    print(name)
    f.write(name + '\n')
f.close()
toast.show_toast(
    "Your list is ready, dipshit.",
    duration = 20,
    threaded = True,
)