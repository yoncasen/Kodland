import discord

# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
# f = open('Python/M2L1/file_read_write/text.txt', 'r', encoding='utf-8')
# text = f.read()
# print(text)
# f.close()

# Ve işte bir metin dosyasının tamamını nasıl yeniden yazabileceğimiz:
# f = open('Python/M2L1/file_read_write/metinbelgesi.txt', 'w', encoding='utf-8')
# text = 'Yeni Yazı'
# f.write(text)
# f.close()

# Kısa hali:
# with open('Python/M2L1/file_read_write/text.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

with open('/Users/yonca/Library/Mobile Documents/com~apple~CloudDocs/Kodland/Python/M2L1/file_read_write/cat.jpg', 'rb') as f:
        print("Image is processing...")
        picture = discord.File(f)

        