# 딕셔너리를 활용해 알파벳 - 모스부호 변환
chr_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--",
    ",": ".-.-",
    ".": "---.",
    "?": "----",
}
morse_chr = {v: k for k, v in chr_morse.items()}
ans = []

# open(0)으로 입력으로 주어진 파일을 읽음, 0은 input을 의미함.
for message in open(0):
    morse_code = [chr_morse[m] for m in message.strip()]  # 문자열을 모드 부호로 바꿈
    lengths, i = (
        reversed(tuple(map(len, morse_code))),
        0,
    )  # 모스부호 길이 역순으로 저장
    no_pause = "".join(morse_code)  # 빈칸없이 모스부호 이어 붙이기
    # 저장된 길이 순서대로 모스부호를 끊고 알파벳으로 변환, 문자열 이어붙여서 저장
    ans.append("".join((morse_chr[no_pause[i : (i := i + j)]] for j in lengths)))
print("\n".join(ans))  # 줄바꿈으로 이어붙여 출력
