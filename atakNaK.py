from ecdsa.numbertheory import inverse_mod
from ecdsa.ecdsa import generator_secp256k1

# Dane z transakcji
r1 = int("f06c2455e7fc6e4bcc73ce05a4de8906794082e4ba298d4647c50a7d6ebfe988", 16)
r2 = int("1cd5156d9a3eb0fca2e28244467cb29af6cf5617ba3be9e277879e3ad6421de1", 16)
s1 = int("f2ad6ad6791612a5c3a5094c358ee459dbad1821345a008dc9856feb7d142036", 16)
s2 = int("eb4b452ed360722c9b9b2050e306ed1195e66ed16355c9c95792a3c4701e270c", 16)
z1 = int("bcf16bdfc712aeb511592ecc73d9c5a4c3a756307d9c00e3a8ed31f7b5bf90c7", 16)
z2 = int("6cd6b4607b73d5933de63f7f3abe7df79bebb13df549eb9c686d7770784c8661", 16)

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
