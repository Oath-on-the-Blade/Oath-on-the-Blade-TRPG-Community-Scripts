# 《六道漕簽有一道總在驗貨後少半角》關連樹目錄

> 關係索引文檔；不是資料夾或固定戰役。個別劇本正文仍是客觀真相與 state 的權威來源。

- **根任務**：《六道漕簽有一道總在驗貨後少半角》
- **根 `script_id`**：`ootb-six-cargo-tallies-missing-corner-v1`

## 節點與直接關連

| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《六道漕簽有一道總在驗貨後少半角》 | `ootb-six-cargo-tallies-missing-corner-v1` | — | 根任務 | 無 |
| 《蘆汀埠四本封艙簿有一本先寫了離埠》 | `ootb-linked-luting-seal-ledger-001` | 《六道漕簽有一道總在驗貨後少半角》 | 後續／封艙交接與離埠記錄責任 | 非必要 |
| 《蘆汀埠五張退貨單有一張總先沾到河水》 | `ootb-linked-luting-five-return-slips-wet-v1` | 《六道漕簽有一道總在驗貨後少半角》＋《蘆汀埠四本封艙簿有一本先寫了離埠》 | 後續／貨損追溯與退貨交接 | 兩者均非必要 |

## 關連圖
```text
六道漕簽有一道總在驗貨後少半角
├─→ 蘆汀埠四本封艙簿有一本先寫了離埠
└─→ 蘆汀埠五張退貨單有一張總先沾到河水
     ↑
     └──── 蘆汀埠四本封艙簿有一本先寫了離埠
```

第三節點同時讀取根任務與《四本封艙簿》的既有 state；兩條直接邊都屬可選 overlay，不構成必要前置。

## 共同背景基線
- 三篇均位於江南道河埠「蘆汀埠」這個根任務建立的局部地點；不把蘆汀埠升格成世界知識庫固定城市。
- 根任務曾出現漕簽缺角與驗貨後掉包風險；後續只承接其可能造成的貨運追溯習慣，不把任何特定 ending 強制定為全世界正史。
- 《四本封艙簿》的四本封艙簿、第三船、纜樁、新任書手與腳夫均為該篇新事件；《五張退貨單》的退貨單、退貨棚、舊染布場與本篇 NPC 亦為新事件。
- 各篇不得把前作 NPC 改名重用，也不得把前作責任無證據轉嫁給新人物。
- 普通漕運行、腳店與船戶不是新相對名譽對象；後續只使用 Handbook 已登錄的正式社會名譽對象。

## branch-specific state
### 根任務
- `tally-ring-broken`：共同作案與掉包手法已被可靠揭露並阻止本次貨損。
- `loss-proved-ring-escapes`：手法／至少一名責任者已被證明，但本次貨損或主要逃犯仍留後果。
- `cargo-sails-unresolved`：夜船離埠時責任仍未可靠解決。
- 無紀錄：依共同基線開始。

以上四種狀態互斥，因同一角色／同一運行只會保存一個根任務 `ending_id`。

### 《蘆汀埠四本封艙簿有一本先寫了離埠》
- `luting_seal_ledger_chain_restored=true`：實際離埠改為解纜時雙人記錄，原冊改痕保留。
- `luting_seal_ledger_safe_hold=true`：貨物安全，原冊封存待核。
- `luting_seal_ledger_incident=true`：錯誤記錄／不安全解纜造成事故或失據。
- `luting_seal_ledger_abandoned=true`：未完成安全交接便離場。

本篇四個 ending state 互斥。

### 《蘆汀埠五張退貨單有一張總先沾到河水》
- `luting_return_chain_restored=true`：今日真貨保全，濕單／半印／換箱合作鏈已可靠建立。
- `luting_return_cargo_saved=true`：今日真貨安全，但合作責任鏈未完整建立。
- `luting_return_method_exposed=true`：真貨已離埠，但換貨手法已被可靠證明。
- `luting_return_chain_unresolved=true`：真貨離埠且手法仍未形成可交付證據。

本篇四個 ending state 互斥。

## 可累積 state
- 根任務 ending 與《四本封艙簿》ending 可依實際角色履歷同時保存。
- 上述兩組來源 state 亦可與《五張退貨單》的 ending state 同時保存；新篇不覆寫舊篇。
- 目前沒有要求玩家必須先完成任何前作才能進入後續。

## 主要 ending／state → 後續映射
### 根任務 → 《四本封艙簿》
- `tally-ring-broken`：第一次要求查看四冊直接獲准。
- `loss-proved-ring-escapes`：守門較緊，但不提高調查 DC。
- `cargo-sails-unresolved`：第一次要求延船須先指出可見矛盾或成功說服。
- 無紀錄：使用「近期貨損促成地方交叉核對」的無前作基線。

### 根任務 → 《五張退貨單》
- `tally-ring-broken`：第一次調取近五次退貨單直接獲准。
- `loss-proved-ring-escapes`：退貨棚守貨較嚴，不提高調查 DC。
- `cargo-sails-unresolved`：先指控人物時，NPC 要求至少一項物證。
- 無紀錄：使用本篇獨立基線。

### 《四本封艙簿》 → 《五張退貨單》
- `luting_seal_ledger_chain_restored=true`：棧橋離埠查核由 40 分鐘縮至 20 分鐘，並可直接排除今日目標箱已隨船離埠。
- `luting_seal_ledger_safe_hold=true`：第一次要求暫停退貨外運可直接獲准 1 小時。
- `luting_seal_ledger_incident=true`：要求停貨前須先指出退貨單濕痕或貨箱繩結的一項可見異常。
- `luting_seal_ledger_abandoned=true`：棧橋查核維持 40 分鐘，須同時核對船牌與腳夫口供。
- 無紀錄：使用本篇獨立基線。

《五張退貨單》各 ending 目前沒有已建立的下一節點；不得由本目錄預先創造未存在任務。

## 多來源條件
《蘆汀埠五張退貨單有一張總先沾到河水》有兩個直接來源，組合規則如下：
- 兩份來源均有紀錄：兩組 overlay **AND 疊加**，各自只改其明列的合作／查核效果。
- 只有根任務紀錄：套用根任務 overlay；《四本封艙簿》按無紀錄基線。
- 只有《四本封艙簿》紀錄：套用其 overlay；根任務按無紀錄基線。
- 兩者都無紀錄：完整使用《五張退貨單》無前作基線。
- 任何來源 ending 都不改寫《五張退貨單》的核心真相，也不互相排斥新篇可達性。

## 維護註記
- 後續不得把根任務 NPC 狀態、物權或前作 ending 當作未寫明前置；三篇皆為 `once_per_character`。
- 若日後讓前作 NPC 再登場，必須回來源全文核對實際 NPC 編號並使用 `NPC#前作編號@前作劇名`。
- 前作物件、證物與貨物只有在來源正文／receipt 明確仍存在且可調取時才能帶入；目前《五張退貨單》不要求帶入任何前作專用物件。
- 新增、刪除或改變直接邊、ending/state 路由或共同背景時，同步更新本檔；劇本檔維持原路徑，不建立同名資料夾。
