from maps.GakushokuSample import GakushokuSample
from maps.Itsuki_prefer import GakushokuSample as ItsukiGakushoku
from maps.minataniosusume import minataniosusume
from maps.AbstractGakushoku import AbstractGakushoku
from maps.momokaOsusume import momokaOsusume
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [
    GakushokuSample(),
    ItsukiGakushoku(),
    minataniosusume(),
    momokaOsusume(),
    AbstractGakushoku()
]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
