# =====================================================================
#  자체 제작 캐릭터 시트 생성기 — Kenney roguelike 팩과 같은 규격(16×16, 1px 간격, 외곽선 없는 부드러운 색)
#  실행: python make_characters.py  → characters.png (게임용) + characters_preview.png (확인용 6배)
#  프레임 순서(0부터): hero0 hero1 slime0 slime1 bat0 bat1 skel0 skel1 gob0 gob1 mage0 mage1 ghost0 ghost1 chest0 chest1
#  한 글자 = 한 픽셀. '.' 은 투명. 팔레트는 아래 PAL.
# =====================================================================
from PIL import Image

PAL = {
    'f': (242, 198, 160), 'F': (217, 166, 121),   # 피부 / 피부 그늘
    'h': (107, 74, 43),                            # 머리카락
    'b': (77, 124, 201),  'B': (52, 90, 154),      # 파랑 옷 / 그늘
    'r': (217, 83, 79),   'R': (166, 58, 55),      # 빨강
    'g': (124, 201, 107), 'G': (79, 154, 66),      # 초록
    'w': (165, 121, 79),  'W': (122, 86, 54),      # 갈색(나무·가죽)
    'e': (244, 244, 244), 's': (184, 184, 192), 'S': (125, 125, 136),  # 흰 / 회색 / 짙은 회색
    'k': (58, 58, 70),                             # 눈·짙은 선
    'p': (155, 111, 208), 'P': (110, 74, 158),     # 보라
    'y': (242, 209, 90),  'Y': (201, 160, 50),     # 노랑(금)
    'o': (233, 226, 207), 'O': (189, 179, 154),    # 뼈
    'c': (200, 230, 245), 'C': (150, 190, 220),    # 유령(하늘빛)
}

def spread_legs(rows, top=12):
    """걷기 프레임: 아래 다리 부분(top행부터)을 왼쪽 절반은 1칸 왼쪽, 오른쪽 절반은 1칸 오른쪽으로 벌린다"""
    out = list(rows[:top])
    for r in rows[top:]:
        left = r[:8].lstrip('.'); right = r[8:].rstrip('.')
        l = (r[:8][1:] + '.') if r[:8][0] == '.' else r[:8]          # 왼쪽 절반을 한 칸 왼쪽으로
        rr = ('.' + r[8:][:-1]) if r[8:][-1] == '.' else r[8:]       # 오른쪽 절반을 한 칸 오른쪽으로
        out.append(l + rr)
    return out

HERO = [
    '................',
    '.....hhhhhh.....',
    '....hhhhhhhh....',
    '....hffffffh....',
    '....ffkffkff....',
    '.....ffffff.....',
    '....bbbbbbbb....',
    '...bbbbbbbbbb...',
    '..fbbbbbbbbbbf..',
    '..f.bBBBBBBb.f..',
    '....bbbbbbbb....',
    '....yyyyyyyy....',
    '....BBB..BBB....',
    '....BBB..BBB....',
    '....www..www....',
    '...WWWW..WWWW...']
SLIME0 = [
    '................', '................', '................', '................', '................',
    '......gggg......',
    '....gggggggg....',
    '...gggggggggg...',
    '..ggekggggekgg..',
    '..gggggggggggg..',
    '..gggggggggggg..',
    '.GGGGGGGGGGGGGG.',
    '.GGGGGGGGGGGGGG.',
    '..GGGGGGGGGGGG..',
    '................', '................']
SLIME1 = [
    '................', '................', '................', '................', '................', '................',
    '.....gggggg.....',
    '...gggggggggg...',
    '..ggekggggekgg..',
    '.gggggggggggggg.',
    'gggggggggggggggg',
    'GGGGGGGGGGGGGGGG',
    '.GGGGGGGGGGGGGG.',
    '..GGGGGGGGGGGG..',
    '................', '................']
BAT0 = [
    '................', '................', '................',
    '..P..........P..',
    '.PPP........PPP.',
    '.PPPP......PPPP.',
    '..PPPP.pp.PPPP..',
    '...PPPppppPPP...',
    '....PPprrppPP...',
    '.....pppppp.....',
    '......pppp......',
    '.......pp.......',
    '................', '................', '................', '................']
BAT1 = [
    '................', '................', '................', '................', '................',
    '.......pp.......',
    '......pppp......',
    '.....pprrpp.....',
    '..PPPppppppPPP..',
    '.PPPPPppppPPPPP.',
    '.PPPP......PPPP.',
    '..PP........PP..',
    '................', '................', '................', '................']
SKEL = [
    '................',
    '.....oooooo.....',
    '....oooooooo....',
    '....okoookoo....',
    '....oooooooo....',
    '.....oOOOOo.....',
    '......oooo......',
    '...O.oooooo.O...',
    '...OoOOOOOOoO...',
    '...O.oOOOOo.O...',
    '.....oOOOOo.....',
    '.....oooooo.....',
    '.....oo..oo.....',
    '.....oo..oo.....',
    '.....OO..OO.....',
    '....OOO..OOO....']
GOB = [
    '................',
    '....G......G....',
    '...GG......GG...',
    '...GGggggggGG...',
    '....gggggggg....',
    '....grggggrg....',
    '....gggggggg....',
    '.....gggggg.....',
    '...gg.wwww.gg...',
    '..g.wwwwwwww.g..',
    '....wwwwwwww....',
    '....WWWWWWWW....',
    '.....gg..gg.....',
    '.....gg..gg.....',
    '.....GG..GG.....',
    '....GGG..GGG....']
MAGE = [
    '.......pp.......',
    '......pppp......',
    '.....pppppp.....',
    '....pppppppp....',
    '...PPPPPPPPPP...',
    '....hffffffh....',
    '....ffkffkff....',
    '.....ffffff.....',
    '....pppppppp....',
    '...ppppppppppy..',
    '..fpppppppppp.y.',
    '..f.pPPPPPPp..y.',
    '....pppppppp..y.',
    '....pppppppp....',
    '....PPPPPPPP....',
    '...PPPP..PPPP...']
GHOST0 = [
    '................', '................',
    '.....cccccc.....',
    '....cccccccc....',
    '...cccccccccc...',
    '...ckccccckcc...',
    '...cccccccccc...',
    '...cccckkccc....',
    '...cccccccccc...',
    '...cccccccccc...',
    '...cccccccccc...',
    '...CcCCcCCcCC...',
    '...C.CC.CC.CC...',
    '................', '................', '................']
GHOST1 = [
    '................',
    '.....cccccc.....',
    '....cccccccc....',
    '...cccccccccc...',
    '...ckccccckcc...',
    '...cccccccccc...',
    '...cccckkccc....',
    '...cccccccccc...',
    '...cccccccccc...',
    '...cccccccccc...',
    '...CCcCCcCCcC...',
    '...CC.CC.CC.C...',
    '................', '................', '................', '................']
CHEST0 = [
    '................', '................', '................', '................',
    '...wwwwwwwwww...',
    '..wWWWWWWWWWWw..',
    '..wWWWWWWWWWWw..',
    '..wwwwwwwwwwww..',
    '..wWWWWyyWWWWw..',
    '..wWWWWyyWWWWw..',
    '..wWWWWWWWWWWw..',
    '..wwwwwwwwwwww..',
    '................', '................', '................', '................']
CHEST1 = [
    '................', '................',
    '...wwwwwwwwww...',
    '..wWWWWWWWWWWw..',
    '..wyyyyyyyyyyw..',
    '..wYYYYYYYYYYw..',
    '..wwwwwwwwwwww..',
    '..wWWWWyyWWWWw..',
    '..wWWWWyyWWWWw..',
    '..wWWWWWWWWWWw..',
    '..wwwwwwwwwwww..',
    '................', '................', '................', '................', '................']

FRAMES = [HERO, spread_legs(HERO), SLIME0, SLIME1, BAT0, BAT1, SKEL, spread_legs(SKEL), GOB, spread_legs(GOB), MAGE, spread_legs(MAGE), GHOST0, GHOST1, CHEST0, CHEST1]
NAMES = ['hero0', 'hero1', 'slime0', 'slime1', 'bat0', 'bat1', 'skel0', 'skel1', 'gob0', 'gob1', 'mage0', 'mage1', 'ghost0', 'ghost1', 'chest0', 'chest1']

for rows in FRAMES:
    assert len(rows) == 16 and all(len(r) == 16 for r in rows), rows

T = 17
sheet = Image.new('RGBA', (len(FRAMES) * T - 1, 16), (0, 0, 0, 0))
for i, rows in enumerate(FRAMES):
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch != '.': sheet.putpixel((i * T + x, y), PAL[ch] + (255,))
sheet.save('characters.png')
prev = sheet.resize((sheet.width * 6, sheet.height * 6), Image.NEAREST)
bg = Image.new('RGBA', prev.size, (40, 40, 60, 255)); bg.alpha_composite(prev); bg.save('characters_preview.png')
print('frames:', len(FRAMES), 'sheet', sheet.size, '|', ' '.join(f'{i}:{n}' for i, n in enumerate(NAMES)))
