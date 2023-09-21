'''
给定一个字符串s，s包括以空格分隔的若干个单词，请对s进行如下处理后输出：
1、单词内部调整：对每个单词字母重新按字典序排序
2、单词间顺序调整：
    1）统计每个单词出现的次数，并按次数降序排列
    2）次数相同，按单词长度升序排列
    3）次数和单词长度均相同，按字典升序排列
'''


def sort_words(input_str):
    # 将输入字符串分割成单词列表
    words = input_str.split()

    # 根据频率、长度和字典序对单词进行排序
    word_count = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_count:
            word_count[sorted_word] += 1
        else:
            word_count[sorted_word] = 1
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], len(x[0]), x[0]))

    # 打印排序后的单词
    for word, count in sorted_words:
        print((word + ' ') * count, end='')

    # 示例用法
    sort_words(input())
