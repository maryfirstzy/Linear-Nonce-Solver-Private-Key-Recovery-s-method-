from ecdsa.numbertheory import inverse_mod
from ecdsa.ecdsa import generator_secp256k1

# Dane z transakcji
r1 = int("baf2aa695873ee637a1b23b53a78c512e4ea8ed72738badbdac3fe6b2a769176", 16)
r2 = int("d56a07721d620e6b3c64021713ae2cec9bc831c4d6d32501e347142bff70d078", 16)
s1 = int("b47bbe4d2e405452dfa95bbd6ac3804c38c25f838edafd5ceb3456f3b040b0a6", 16)
s2 = int("4c136bac45a92b2adfc0af27282b494f6dc416535433d36e04057de2bf7cc326", 16)
z1 = int("d20aff079cd86074eff889e1f4f0fbd0b97ef4eeff378147afc815d8a28552d5", 16)
z2 = int("17ea532a30334538c281467befb5fca7e66c6b1e760f5d17d77cb853c65a3c7d", 16)

# Moduł porządkowy krzywej secp256k1
n = generator_secp256k1.order()

# Różnice
delta_s = (s1 - s2) % n
delta_z = (z1 - z2) % n

# Obliczanie k – tylko jeśli delta_s ≠ 0
if delta_s != 0:
    k = (delta_z * inverse_mod(delta_s, n)) % n
    print(f"✅ Wykryto liniową zależność k! k = {hex(k)}")

    # Teraz obliczamy prywatny klucz d na podstawie wzoru:
    # s = (z + r*d)/k  =>  d = (s*k - z) / r
    d = ((s1 * k - z1) * inverse_mod(r1, n)) % n
    print(f"🔑 Odzyskany klucz prywatny: d = {hex(d)}")
else:
    print("❌ Brak zależności liniowej w k – delta_s = 0")
