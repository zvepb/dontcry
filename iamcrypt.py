import os

import eel
import pyAesCrypt


def crypt_file(file, password):
        fileprint = file
        bufferSize = 512 * 1024
        try:
            pyAesCrypt.encryptFile(str(file), str(file) + ".hsal$wetkbfuhrtugkBJVmbfdjg$Soljdy",
                                   password, bufferSize)
            os.remove(file)
            eel.print_res('encrypted file $  ' + str(fileprint))
        except Exception as e:
            pass

@eel.expose
def crypt_disk(dir, password):
    try:
        for file in os.listdir(dir):
            if os.path.isdir(dir + '\\' + file):
                crypt_disk(dir + '\\' + file, password)
            if os.path.isfile(dir + '\\' + file):
                try:
                    if file[-35::] == ".hsal$wetkbfuhrtugkBJVmbfdjg$Soljdy":
                        pass
                    else:
                        crypt_file(dir + '\\' + file, password)
                except Exception as ex:
                    pass
        return "$ all files was encrypted $"
    except Exception as e:
        pass

def decrypt_file(file, password):
    fileprint = file
    bufferSize = 512 * 1024
    try:
        pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]),
                               password, bufferSize)
        os.remove(file)
        eel.print_res('decrypted file $  ' + str(fileprint))
    except Exception as e:
        pass

@eel.expose
def decrypt_disk(dir, password):
    try:
        for file in os.listdir(dir):
            if os.path.isdir(dir + '\\' + file):
                decrypt_disk(dir + '\\' + file, password)
            if os.path.isfile(dir + '\\' + file):
                try:
                    decrypt_file(dir + '\\' + file, password)
                except Exception as ex:
                    pass
        return "$ all files was decrypted $"
    except Exception as e:
        pass


eel.init("style")
eel.start("iamcrypth.html", host="localhost", port=13000, mode='my_portable_chromium', block=True, size=(730, 370))
