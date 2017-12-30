import execjs


JS = '''function aes() {
            try {
                var e = CryptoJS.enc.Hex.parse('f8c7fd111dedb4c9cdfb99edf35e3db9'),
                f = CryptoJS.enc.Hex.parse('0a379ab1ee9cb40a40398a6d36b7a002'),
                b = 'bzZRYtv0d/OJ+ZmFWC8rIZ2ZC/+TTdn/CeIBCXxThctJk+r3RgUFS2X77lby4BOAKMyLwbEl2pLnnItl879lB1btax1pjtws6KiB8KTBPihMbNgnSAdt9TKJcPuCD1PaAK4Ps1oiNBkakNIaJBT+dXUaT+TRcjFX5cfMv3wSCTqiYo8i9vOvJWI0mxaK2R8I',
                b = b.replace(/\s/g, '+'),
                c = CryptoJS.AES.decrypt(b, e, {
                    iv: f,
                    mode: CryptoJS.mode.CBC
                }),
                c = CryptoJS.enc.Utf8.stringify(c),
                a = c.split('#'),
                g = CryptoJS.MD5(a[4] + a[0] + a[2] + a[3]);
                return {
                    md5key: a[1],
                    md5Value: g
                }
            } catch (t) {
                return 'Error:Main code is NOT run'
            }
        }'''

ctx = execjs.compile(JS)
print(ctx.call('aes'))

