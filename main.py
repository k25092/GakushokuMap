from maps.GakushokuSample import momokaOsusume
from maps.Itsuki_prefer import GakushokuSample as ItsukiGakushoku
from maps.minataniosusume import minataniosusume
from maps.k25092Osusume import GakushokuSample as k25092Gakushoku
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [
    momokaOsusume(),
    ItsukiGakushoku(),
    minataniosusume(),
    k25092Gakushoku(),
]
# ↓のリストには、メンバーの各オススメ学食が格納されます。
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
