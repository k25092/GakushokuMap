from maps.GakushokuSample import GakushokuSample
from maps.k25092Osusume import k25092Osusume
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(), 
        k25092Osusume()
    ]
from maps.GakushokuSample import GakushokuSample
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(), ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(), ]
for rank, d in enumerate(data, start=1):
  print(f"{rank}位: {d.get_menu()}")
  print("---------------------------------")
  print(d.get_summary())
  print(d.get_author())
  print()
