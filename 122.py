from Crypto.Cipher import AES
import base64
import binascii


iv = binascii.a2b_hex(b'0a379ab1ee9cb40a40398a6d36b7a002')
key = binascii.a2b_hex(b'f8c7fd111dedb4c9cdfb99edf35e3db9')
# iv =b'0a379ab1ee9cb40a'
# key = b'f8c7fd111dedb4c00a379ab1ee9cb40a'
# key = b'\x00'*32
# iv = b'\x4e'*32
# key = AES.parse_hex('0a379ab1ee9cb40a40398a6d36b7a002')
mode = AES.MODE_CBC
token = 'qU136eVGd4j6wTjEd402WiT2vtRUgwZId+rkQ7J6xiaDgEW667EXFU1jlYtl+8IjjIaTfIJkZIeeMsM4+qJm2jq0d2S1vFLC5sT3Ts1N0GeNwHinmJZNO7j0kQGRbaFoy/UmBD5u5O4Dg6zn74Lt+MhrPjKjnqfRm8rSiSM/dlriGotge8iU9Etrck4SNnZD'

# token = token.replace(' ','+')
cipher = AES.new(key,AES.MODE_CBC, iv )
ciphertext= cipher.decrypt(token)
ciphertext_base64=base64.b64encode(ciphertext)
print(ciphertext_base64,type(ciphertext_base64))