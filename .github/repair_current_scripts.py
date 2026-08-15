from pathlib import Path
import re

files = sorted(Path('.').glob('OOTB_*.md'))
if len(files) != 49:
    raise SystemExit(f'Expected 49 OOTB scripts, found {len(files)}')

def field_value(text, names):
    for name in names:
        m = re.search(r'^\|\s*' + re.escape(name) + r'\s*\|\s*(.*?)\s*\|\s*$', text, re.M)
        if m:
            return m.group(1).strip()
        m = re.search(r'^-\s*\*\*' + re.escape(name) + r'\*\*\s*[：:]\s*(.*?)\s*$', text, re.M)
        if m:
            return m.group(1).strip()
    return ''

def insert_header_fields(text, regions):
    if '核心任務目標' in text and '劇本範圍與任務放棄條件' in text:
        return text
    goal = '完成本劇本核心衝突所描述的核心事件：查明或確認客觀真相，處理與核心事件直接相連的危機／人物／證物，並把事件推進至正文一個明確結局。'
    scope = f'核心範圍為「{regions or "規格頭所列主要地區"}」及核心衝突的直接因果後續。跳場景、另走路線、與敵方合作或以武學／人脈繞過障礙，只要仍在處理核心事件都不算離題；若全隊明確不再處理核心事件並離開範圍，GM 先作越界警告，再依「現行規則補充：任務邊界、放棄與場景裁定」進入任務放棄結局。'
    lines = text.splitlines()
    out = []
    inserted = False
    for line in lines:
        out.append(line)
        if inserted:
            continue
        if re.match(r'^\|\s*核心衝突(?:一句話摘要|摘要)?\s*\|', line):
            out.append(f'| 核心任務目標 | {goal} |')
            out.append(f'| 劇本範圍與任務放棄條件 | {scope} |')
            inserted = True
        elif re.match(r'^-\s*\*\*核心衝突(?:一句話摘要|摘要)?\*\*\s*[：:]', line):
            out.append(f'- **核心任務目標**：{goal}')
            out.append(f'- **劇本範圍與任務放棄條件**：{scope}')
            inserted = True
    if not inserted:
        raise RuntimeError('Could not locate core conflict header field')
    return '\n'.join(out) + ('\n' if text.endswith('\n') else '')

def supplement(core, regions):
    core = core or '以規格頭「核心衝突」所述事件為準。'
    regions = regions or '以規格頭「主要地區」及核心事件直接因果後續為準。'
    return f'''# 現行規則補充：任務邊界、放棄與場景裁定

本節是本劇本正文的一部分，與各場景既有專用資料合併使用；若與 Handbook 當前規則衝突，以 Handbook 為準。

## 核心任務與範圍

- **核心事件**：{core}
- **主要範圍**：{regions}
- 玩家跳過場景、反向追查、先解終局、與原對手合作、使用高階輕功／名望／人脈／武學繞過障礙，只要仍在處理上述核心事件，都屬於範圍內合法解法，GM 不得為把流程拉回預定順序而否定。

## 越界警告與任務放棄

當全隊明確表示**不再處理核心事件**，並準備離開上述範圍或永久轉去與核心事件無直接關係的目標時，GM 必須先明說：

> 「若你們確認離開並不再處理本事件，本劇本會在此進入任務放棄結局；世界將依目前狀態及『玩家不介入』後續繼續，本劇本不再為範圍外行動生成新的主線內容。是否確認？」

只有玩家確認後才進入放棄結局。單純拒絕原委託人、換方法、離開一個場景、暫時撤退或與原敵方合作，不等於放棄，只要仍實際介入核心事件。

### 任務放棄／推進來源永久失效結局

- **成立條件**：全隊在越界警告後確認不再處理核心事件；或玩家明知後果而永久毀損所有仍可合理推進的來源，且正文已無任何替代來源可讓事件收斂。
- **世界後果**：從當前危機格、NPC 已採取的行動與已造成的損失繼續，之後依本檔「玩家不介入」發展；若玩家已觸發正文更嚴重且具體的後果，保留該後果，不倒帶。
- **銀兩／物質**：所有尚未完成條件的委託報酬與完成加成為 0；已合理取得且沒有被追回理由的既有物件不憑空消失。
- **名望／關係**：不取得「完成本案」帶來的正面名望／關係；玩家在離開前已實際造成的正負關係照常保留。
- **基礎歷練**：若離開時尚未達成正文任何一個明確結局的成立條件，基礎歷練為 **0**。若離開前其實已達成正文某一主要／部分結局的成立條件，直接按該結局結算，不再疊加本放棄結局。

## 所有主要場景共同裁定

以下規則補足各主要場景的可行性、成本與重試邊界；場景正文已列出的專用 DC、資源、地形、敵人反應與失敗後果仍優先使用。

- **可直接成立**：方法與既定世界因果相符、已有足夠能力／工具／位置，且不存在有意義的不確定性或失敗成本時，直接取得該方法合理範圍內的結果，不擲骰。
- **需要判定**：存在真實成立途徑但結果仍不確定時才擲骰。場景已有 DC 就使用該 DC；未另列 DC 時，依 `遊玩規則/00_遊戲核心.md` 在擲骰前公開採用常用 DC：容易10、一般13、困難16、極難20、傳奇25+，並先鎖定方法、投入、成功範圍及可預見失敗風險。
- **極難但仍可能**：只有角色確有能力／武學／物品／環境路徑時才可用 DC20 或傳奇25+；不能用高 DC 把沒有因果途徑的宣告變成可能。
- **不能成立**：若方法違反已建立物理條件、正式武學／物品效果、距離、時間或因果關係，GM 直接說明阻礙並否決結果，不讓自然20憑空創造能力。
- **行動成本與協助**：擲骰前鎖定所需時間／動作、消耗品、位置、協助者與其他真實成本；多人不能只為刷高骰面輪流重擲同一問題，按核心規則使用合理協助或團體檢定。
- **成功範圍**：成功只取得擲骰前說明的效果；高出 DC 或自然20不自動附送額外真相、額外傷害、額外控制或超出正式能力的結果。
- **失敗後果**：使用該場景正文已建立的風險；若沒有額外風險而且可無代價重試，則原本就不應要求擲骰。不得臨時以無預警死亡或抹除核心線索作懲罰。
- **重試條件**：失敗後只有方法、工具、情報、位置、時機或世界狀態實質改變，或角色承擔新的真實成本／風險，才可重試；否則同一嘗試的失敗結果維持。
- **正式資源核對**：凡方法引用拿手、絕活、武學、物品、毒藥、丹藥、敵人能力或狀態，先查 `內容庫/` 與相關 `遊玩規則/` 的正式條目，不按名稱或玩家描述自行擴張效果。
- **NPC 與危機後續**：成功或失敗後，按場景已寫明的 NPC 目的、下一步、危機時鐘與世界狀態繼續；不得因玩家用非預期方法成功便令 NPC 停止行動，也不得為延長流程重置已解決問題。

'''

anchors = [
    '# 交付前反大綱覆檢矩陣',
    '# 最終運行核對',
    '# 完整性覆檢',
    '# 完整性檢查',
    '# 最終覆檢',
    '# 反大綱覆檢',
]

changed = []
for path in files:
    text = path.read_text(encoding='utf-8')
    original = text
    text = text.replace('遊玩遊玩規則/', '遊玩規則/')
    core = field_value(text, ['核心衝突一句話摘要', '核心衝突摘要'])
    regions = field_value(text, ['主要地區'])
    text = insert_header_fields(text, regions)
    if '# 現行規則補充：任務邊界、放棄與場景裁定' not in text:
        block = supplement(core, regions)
        positions = [text.find(a) for a in anchors if text.find(a) >= 0]
        if positions:
            pos = min(positions)
            text = text[:pos].rstrip() + '\n\n---\n\n' + block + text[pos:]
        else:
            text = text.rstrip() + '\n\n---\n\n' + block

    if path.name == 'OOTB_入門任務_丟失的藥簍.md':
        pat = r'(## 終局 D：替惡少私下調解\s*\n)(?!\s*\*\*基礎歷練)'
        text, n = re.subn(pat, r'\1\n**基礎歷練**：江湖 2、計略 2（總計 4）。\n', text, count=1)
        sec = text.split('## 終局 D：替惡少私下調解',1)[1].split('\n## ',1)[0]
        if '基礎歷練' not in sec:
            raise RuntimeError('Failed to patch 藥簍 ending D')

    if path.name == 'OOTB_入門任務_河堤夜火.md':
        pat = r'(## D｜錯抓興隆木號的人\s*\n)(?!\s*\*\*基礎歷練)'
        text, n = re.subn(pat, r'\1\n**基礎歷練**：江湖 2、計略 2（總計 4）。\n', text, count=1)
        sec = text.split('## D｜錯抓興隆木號的人',1)[1].split('\n## ',1)[0]
        if '基礎歷練' not in sec:
            raise RuntimeError('Failed to patch 河堤 ending D')

    if path.name == 'OOTB_入門任務_瓷窯夜火.md' and '只完成護送，不回頭處理火場' in text and '部分完成／退出結局' not in text:
        text = text.replace('只完成護送，不回頭處理火場', '只完成護送，不回頭處理火場（部分完成／退出結局）', 1)

    path.write_text(text, encoding='utf-8')
    if text != original:
        changed.append(path.name)

for path in files:
    text = path.read_text(encoding='utf-8')
    required = [
        '核心任務目標',
        '劇本範圍與任務放棄條件',
        '# 現行規則補充：任務邊界、放棄與場景裁定',
        '## 越界警告與任務放棄',
        '**基礎歷練**：若離開時尚未達成正文任何一個明確結局的成立條件，基礎歷練為 **0**',
        '**重試條件**',
    ]
    missing = [x for x in required if x not in text]
    if missing:
        raise RuntimeError(f'{path}: missing {missing}')
if '遊玩遊玩規則/' in ''.join(p.read_text(encoding='utf-8') for p in files):
    raise RuntimeError('Typo 遊玩遊玩規則 remains')

print(f'Updated {len(changed)} scripts')
for x in changed:
    print(x)
