OKUWCY_SANAWY = []

def okuwcy_gos(okuwcy_id, ady, familiyasy, yasy, kursy):
    OKUWCY_SANAWY.append({
        "id": okuwcy_id,
        "ady": ady,
        "familiyasy": familiyasy,
        "yasy": yasy,
        "kursy": kursy,
    })

def maglumatlary_gorkez():
    print("\n" + "=" * 55)
    print("         GIRIZILEN OKUWÇYLARYŇ SANAWY         ")
    print("=" * 55)
    print(f"{'ID':<10} {'Ady':<12} {'Familiyasy':<15} {'Ýaşy':<8} {'Kursy':<8}")
    print("-" * 55)
    for o in OKUWCY_SANAWY:
        print(f"{o['id']:<10} {o['ady']:<12} {o['familiyasy']:<15} {o['yasy']:<8} {o['kursy']:<8}")
    print("=" * 55)

print("=== Okuwçy Maglumat Ulgamy ===")
print("Täze okuwçy goşmak üçin ID ornuna 'stop' ýazyň.\n")

while True:
    o_id = input("ID giriziň: ")
    if o_id.lower() == "stop":
        break
    ady = input("Adyny giriziň: ")
    familiyasy = input("Familiýasyny giriziň: ")
    yasy = input("Ýaşyny giriziň: ")
    kursy = input("Kursyny giriziň: ")
    okuwcy_gos(o_id, ady, familiyasy, yasy, kursy)
    print("--> Okuwçy üstünlikli goşuldy!\n")

maglumatlary_gorkez()