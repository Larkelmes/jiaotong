const CryptoJS = require('crypto-js');

function aes() {
            
                var e = CryptoJS.enc.Hex.parse('f8c7fd111dedb4c9cdfb99edf35e3db9'),
                f = CryptoJS.enc.Hex.parse('0a379ab1ee9cb40a40398a6d36b7a002'),
                b = 'q/svKjOVICNd0iGpYWuQMj4wk p0R137hg1LXPCDKJmEE1f/RmTJIkbZXIfTEH1NdQG1MS2CW/Shax88gHTZWxNs08AA3f0osqUhiBXkQylnn0cygVKke88QW0tQMSQ8//3YqI tAEFVVzxJL97SrZ3LFOuxgtfxkvnQupnpWJnuGLMitT9Pt8o4kWrj8eka',
                b = b.replace(/\s/g, '+'),
                c = CryptoJS.AES.decrypt(b, e, {
                    iv: f,
                    mode: CryptoJS.mode.CBC
                }),
                c = CryptoJS.enc.Utf8.stringify(c),
                a = c.split('#'),
                g = CryptoJS.MD5(a[4] + a[0] + a[2] + a[3]);
                return a[1];
        }

var decrypted = aes();


console.log('Decrypted text: ' + decrypted);