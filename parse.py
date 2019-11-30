import sys
import re

LANG_B = ["<f26", "<f31", "<f33", "<f34", "<f39", "<f40", "<f41", "<f43", "<f46", "<f48",
          "<f50", "<f55", "<f57", "<f66", "<f75", "<f76", "<f77", "<f78", "<f79", "<f80",
          "<f81", "<f82", "<f83", "<f84", "<f85", "<f86", "<f94", "<f95", "<f103", "<f104",
          "<f105", "<f106", "<f107", "<f108", "<f111", "<f112", "<f113", "<f114", "<f115", "<f115"]

LANG_UNK = ["<f12", "<f59", "<f60", "<f61", "<f62", "<f63", "<f64", "<f65", "<f67", "<f68",
            "<f69", "<f70", "<f71", "<f72", "<f73", "<f74", "<f91", "<f92", "<f97", "<f98",
            "<f101", "<f109", "<f110", "<f116"]


PIC_PATTERN = re.compile(r"-{[^{}]+}")

"""memo
-: 行末(画像が挟まれた場合も-を入れる)
=: 段落終了
.: 単語境界
,: 単語境界

-と=の直後に出る{[^{}]+}は文の途中もしくは前後に挿入されている画像を表す

"""


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if line.startswith('#'):
            continue
        else:
            lang = ""
            # 言語B
            if any([line.startswith(x) for x in LANG_B]):
                lang = "B"
            # 言語?
            elif any([line.startswith(x) for x in LANG_UNK]):
                lang = "UNK"
            else:  # 言語A
                lang = "A"
            ret = re.match(r'^<(\w\d+\w\.\w\.\d+;F)>(.+)$', line)
            if ret:
                meta = ret.group(1).strip()
                sentence = ret.group(2).strip()
                pics = [re.sub("[-{}]", "", x) for x in PIC_PATTERN.findall(sentence)]
                print(meta, lang, sentence, pics)
