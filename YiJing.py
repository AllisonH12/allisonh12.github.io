import random
from flask import Flask, render_template, request


app = Flask(__name__)

class YiJing:

    HEXAGRAMS = { 
    "111111": "乾 - Qián - The Creative",
    "000000": "坤 - Kūn - The Receptive",
    "010001": "震 - Zhèn - The Arousing",
    "100010": "巽 - Xùn - The Gentle",
    "010111": "坎 - Kǎn - The Abysmal",
    "111010": "离 - Lí - The Clinging",
    "001010": "艮 - Gèn - Keeping Still",
    "101111": "兑 - Duì - The Joyous",
    "111011": "涉 - Shè - The Army",
    "110111": "泰 - Tài - The Clinging Fire",
    "111110": "否 - Pǐ - The Arousing Thunder",
    "010010": "小过 - Xiǎo Guò - The Gentle Wind",
    "101001": "履 - Lǚ - The Penetrating",
    "110000": "泰 - Tài - The Joyous Lake",
    "000011": "乾 - Qián - The Creative Heaven",
    "111000": "夬 - Guài - The Joyous Earth",
    "000111": "大壮 - Dà Zhuàng - The Great Accumulating",
    "100000": "颐 - Yí - The Penetrating Wind",
    "000001": "蛊 - Gu - The Joyous Lake",
    "100110": "临 - Lín - Approach",
    "011001": "观 - Guān - The Clinging",
    "010011": "剥 - Bō - Dispersion",
    "110100": "复 - Fù - Return",
    "001100": "小畜 - Xiǎo Xù - The Gentle",
    "101101": "大畜 - Dà Xù - The Great Possessing",
    "001111": "归妹 - Guī Mèi - The Abysmal Water",
    "111100": "仙姑 - Xiān Gū - The Sojourning",
    "000100": "节 - Jié - The Clinging Fire",
    "001000": "葵 - Kuí - Opposition",
    "100111": "归妹 - Guī Mèi - The Joyous Lake",
    "111001": "萃 - Cuì - The Taming Power of the Great",
    "100101": "兑 - Duì - The Joyous Lake",
    "101100": "恒 - Héng - Duration",
    "001110": "遁 - Dùn - Retiring",
    "011100": "大有 - Dà Yǒu - The Great Taming",
    "001001": "升 - Shēng - Pushing Upward",
    "110110": "观 - Guān - The Keeping Still Mountain",
    "011010": "否 - Pǐ - The Arousing Fire",
    "101010": "解 - Jiě - The Clinging Wood",
    "010100": "坎 - Kǎn - The Abysmal Water",
    "110010": "离 - Lí - The Clinging Flame",
    "010011": "渐 - Jiàn - The Infiltrating",
    "110101": "大壮 - Dà Zhuàng - The Joyous Lake",
    "001101": "晋 - Jìn - The Gentle Wind",
    "101100": "明夷 - Míng Yí - The Clinging Brightness",
    "001011": "家人 - Jiā Rén - The Family",
    "110100": "睽 - Kuí - Opposition",
    "010110": "蹇 - Jiǎn - Obstruction",
    "011100": "解 - Jiě - The Great Accumulating",
    "001010": "损 - Sǔn - The Gentle",
    "101011": "益 - Yì - Increase",
    "010100": "夬 - Guài - The Clinging Brightness",
    "001001": "姤 - Gòu - The Taming Power of the Small",
    "100010": "萃 - Cuì - The Gathering",
    "010001": "升 - Shēng - The Clinging Wind",
    "110110": "泰 - Tài - The Sojourning",
    "011010": "否 - Pǐ - The Taming Power of the Great",
    "010010": "同人 - Tóng Rén - The Joyous",
    "101101": "大有 - Dà Yǒu - The Keeping Still Mountain",
    "011001": "谦 - Qiān - The Modest",
    "100110": "豫 - Yù - The Receptive Earth",
    "010111": "随 - Suí - The Following",
    "111010": "蛊 - Gu - The Clinging Wood",
    "010011": "临 - Lín - The Gentle",
    "110010": "观 - Guān - The Joyous",
    "100101": "噬嗑 - Shì Kè - The Clinging Fire",
    "101001": "贲 - Bì - The Abysmal Water",
    "100000": "剥 - Bō - The Joyous Lake",
    "000001": "复 - Fù - The Clinging Thunder",
    "111100": "无妄 - Wú Wàng - The Clinging Mountain",
    "000100": "大畜 - Dà Xù - The Clinging Wind",
    "110001": "颐 - Yí - The Joyous Earth",
    "100011": "大过 - Dà Guò - The Preponderance of the Great",
    "111110": "坎 - Kǎn - The Abysmal Wind",
    "011111": "离 - Lí - The Clinging",
    "101101": "咸 - Xián - The Gentle Wind",
    "111010": "恒 - Héng - The Clinging Fire",
    "010111": "遯 - Dùn - The Abysmal Water",
    "111000": "大壮 - Dà Zhuàng - The Joyous Heaven",
    "000111": "晋 - Jìn - The Joyous Earth",
    "101111": "明夷 - Míng Yí - The Arousing Thunder",
    "111101": "家人 - Jiā Rén - The Arousing Wind",
    "001110": "睽 - Kuí - The Clinging Water",
    "011100": "蹇 - Jiǎn - The Keeping Still Mountain",
    "000010": "解 - Jiě - The Receptive Earth",
    "010000": "损 - Sǔn - The Joyous Lake",
    "111111": "益 - Yì - The Creative Heaven",
    "000000": "夬 - Guài - The Creative Earth",
    "101000": "姤 - Gòu - The Clinging Fire",
    "000101": "萃 - Cuì - The Arousing Thunder",
    "110111": "升 - Shēng - The Clinging Mountain",
    "111011": "泰 - Tài - The Joyous Lake",
    "010010": "否 - Pǐ - The Clinging Water",
    "101101": "同人 - Tóng Rén - The Abysmal Water",
    "110101": "大有 - Dà Yǒu - The Arousing Thunder",
    "001011": "谦 - Qiān - The Gentle Wind",
    "101100": "豫 - Yù - The Gentle Earth",
    "110001": "随 - Suí - The Clinging Wind",
    "100011": "蛊 - Gu - The Clinging Fire",
    "111100": "临 - Lín - The Abysmal Water"
    }

    @staticmethod
    def get_binary_code(word):
        binary_code = ""
        for char in word:
            binary_code += bin(ord(char))[2:].zfill(8)
        return binary_code

    @staticmethod
    def get_fragments(binary_code):
        fragments = []
        for i in range(0, len(binary_code), 6):
            fragments.append(binary_code[i:i+6])
        return fragments

    @staticmethod
    def lookup_hexagram(fragment):
        if fragment in YiJing.HEXAGRAMS:
            return YiJing.HEXAGRAMS[fragment]


def get_luck():
    #word = input("Enter a word: ")
    word = ''
    #word = request.form['word']
    #word = 'abc'
    #a = request.form['word1']
    print(request.form)
    a = request.form['word1']
    print(a)
    word = a
    word += str(random.randint(0, 65))
    #binary_code = YiJing.get_binary_code(word)
    binary_code = YiJing.get_binary_code(word)
    fragments = YiJing.get_fragments(binary_code)
    luck = {}
    for fragment in fragments:
        if YiJing.lookup_hexagram(fragment) in luck:
            luck[YiJing.lookup_hexagram(fragment)] += 1
        else:
            luck[YiJing.lookup_hexagram(fragment)] = 1

    sorted_dict = {k: v for k, v in sorted(luck.items(), key=lambda item: item[1], reverse=True)}
    ct = 0
    out = ""
    for key, value in sorted_dict.items():
        ct += 1 
        if ct < 4 and key is not None:
            out += key + "    "
    return out

@app.route('/', methods=['GET', 'POST'])
def home():
    luck = get_luck()
    return render_template('home.html', luck=luck)

if __name__ == '__main__':
    app.run(debug=True)
