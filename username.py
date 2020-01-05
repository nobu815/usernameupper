"""
データ型宣言:UserName
    属性:
        実際のユーザー名
    ルール:
        ・ユーザー名は４文字以上２０文字以下である
    できること
        ・ユーザー名を大文字に変換する
"""


class UserName:
    def __init__(self, name):
        #        print('hello', name)
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}は文字数の違反です')

        self.name = name

    def screen_name(self):
        return self.name.upper()


# UserNameクラスのインスタンス化

hibiki = UserName(name='hibiki')

print(hibiki.name.upper())
print(hibiki.screen_name())

# print(hibiki)
# print(type(hibiki))
# print(hibiki.name)
# .nameで値にアクセスできる

# sho = UserName('sho')
